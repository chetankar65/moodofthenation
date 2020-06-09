///line chart data
function line (days, moods)
{
    var load = document.getElementById('load')
    load.remove()
    var ctx = document.getElementById('line').getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: days,
            datasets: [{
                label: 'Weekly "mood" trend',
                data: moods,
                backgroundColor: '#8080ff',
                borderColor: 'black',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    });
}


/// xmlhttprequest to get graph data
function xhr()
{
    const request = new XMLHttpRequest();
    request.open('GET', '/timeline_data');

        // Callback function for when request completes
    request.onload = () => {
        // Extract JSON data from request
        const data = JSON.parse(request.responseText);
        // Update the result div
        if (data.success) {
            line(data.days, data.moods)
            var content = ''
                for (var i = 1; i < data.timeline.length; i++){
                //console.log(data.current[i])
                    if (data.timeline[i] == 3){
                        content += `
                            <div class="col-3 col-sm-3 col-lg-3">
                            Before ${i + 1} hours <br><br>
                                <img src="/static/download.png" style="width: 80px;height: 80px;"><br><br>
                            </div>
                        `
                    } else if (data.timeline[i] == 1){
                        content += `
                        <div class="col-3 col-sm-3 col-lg-3">
                            Before ${i + 1} hours <br><br>
                            <img src="/static/terrified.png" style="width: 80px;height: 80px;"><br><br>
                        </div>
                        `   
                    } else {
                        content += `
                            <div class="col-3 col-sm-3 col-lg-3">
                                Before ${i + 1} hours <br><br>
                                <img src="/static/neutral.png" style="width: 80px;height: 80px;"><br><br>
                            </div>
                        `
                    }
                }
                document.getElementById('emojis').innerHTML = content
        }
    }
        // Add data to send with request
        // Send request
    request.send(null);
    return false;

}
// run function
xhr()


/// xmlhttprequest to get timeline data
