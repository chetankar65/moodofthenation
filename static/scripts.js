function sleep(milliseconds) {
    var start = new Date().getTime();
    for (var i = 0; i < 1e7; i++) {
      if ((new Date().getTime() - start) > milliseconds){
        break;
        }
    }
}
////////////////////////
document.addEventListener('DOMContentLoaded', () => {
        sleep(3000);
        const request = new XMLHttpRequest();
        request.open('GET', '/latestnews');

            // Callback function for when request completes
        request.onload = () => {
            document.querySelector('#latestnews').innerHTML = ''
                // Extract JSON data from request
            const data = JSON.parse(request.responseText);
                // Update the result div
            if (data.success) {
                var contents = '';
                for (var i = 0 ; i < data.top_headlines.length; i++){
                    contents += `
                    <div style="border-style: solid;">
                        <div align="left">
                            <b>${new Date()}</b><br><br>
                        </div>
                        <div align="left">
                            ${data.top_headlines[i]}
                        </div>
                    </div><br>
                    `
                }
                document.querySelector('#latestnews').innerHTML = contents;
                
                if (data.mood == 3){
                    document.getElementById('emoji').innerHTML = `<img src="/static/download.jpeg" style="width: 150px;height: 150px;">`
                    document.getElementById('mood_description').innerHTML = `The nation seems very happy!
                    Let's keep it up!
                    `
                    document.getElementById('mood_description').style.color = "green"
                } else if (data.mood == 1){
                    document.getElementById('emoji').innerHTML = `<img src="/static/terrified.jpeg" style="width: 150px;height: 150px;">`
                    document.getElementById('mood_description').innerHTML = `Not in a very good shape, but keep your chin up!
                    `
                    document.getElementById('mood_description').style.color = "red"
                } else {
                    document.getElementById('emoji').innerHTML =`<img src="/static/neutral.png" style="width: 150px;height: 150px;">`
                    document.getElementById('mood_description').innerHTML = `It's doing ok!Neither too good, neither too bad!
                    `
                    document.getElementById('mood_description').style.color = "orange"
                }

                }
                else {
                    document.querySelector('#latestnews').innerHTML = 'There was an error.';
                }

                var content = ''
                for (var i = 1; i < data.current.length;i++){
                //console.log(data.current[i])
                    if (data.current[i] == 3){
                        content += `
                            <div class="col-4 col-sm-4 col-lg-4">
                                <img src="/static/download.jpeg" style="width: 80px;height: 80px;">
                            </div>
                        `
                    } else if (data.current[i] == 1){
                        content += `
                        <div class="col-4 col-sm-4 col-lg-4">
                            <img src="/static/terrified.jpeg" style="width: 80px;height: 80px;">
                        </div>
                        `   
                    } else {
                        content += `
                            <div class="col-4 col-sm-4 col-lg-4">
                                <img src="/static/neutral.png" style="width: 80px;height: 80px;">
                            </div>
                        `
                    }
                }
                document.getElementById('time').innerHTML = content
            }
        // Add data to send with request
        // Send request
        request.send(null);
        return false;
});
