/// xmlhttprequest to get graph data
function xhr(){
    line(labels, data)
    line2()
}

xhr()
// Line chart
function line ()
{
    var ctx = document.getElementById('line').getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [{
                label: 'Weekly trend',
                data: data,
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

//second line chart

function line2() {
    var ctx2 = document.getElementById('line2').getContext('2d');
    var myChart3 = new Chart(ctx2, {
        type: 'line',
        data: {
            labels: ["April", "May", "June", "July", "August", "September"],
            datasets: [{
                label: 'Monthly trend',
                borderDash: [5, 5],
                data: [12, 19, 3, 5, 2, 3],
                backgroundColor: 'transparent',
                borderColor: 'red',
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
