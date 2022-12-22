const uploadForm2 = document.getElementById('setting-form')
const input2 = document.getElementById('id_photo_background')
console.log(input2)

const progressBox2 = document.getElementById('progress-box')
const csrf2 = document.getElementsByName('csrfmiddlewaretoken')

input2.addEventListener('change', ()=>{
    progressBox2.classList.remove('not-visible')
    const img_data2 = input2.files[0]
    const fd2 = new FormData()
    fd2.append('csrfmiddlewaretoken', csrf2[0].value)
    fd2.append('photo_background', img_data2)

    $.ajax({
        type: 'POST',
        url: uploadForm2,
        enctype: 'multipart/form-data',
        data: fd2,
        beforeSend: function() {

        },
        xhr: function() {
            const xhr2 = new window.XMLHttpRequest();
            xhr2.upload.addEventListener('progress', e=> {
                if (e.lengthComputable) {
                    const percent2 = e.loaded / e.total * 100
                    console.log(percent2)
                    progressBox2.innerHTML = `<div class="progress__block2">
                                                  <div class="progress">
                                                      <div class="progress-bar" role="progressbar" style="width: ${percent2}%" aria-valuenow="${percent2}%" aria-valuemin="0" aria-valuemax="100"></div>
                                                  </div>
                                                  <p class="progress__int">${percent2.toFixed(0)}%</p>
                                             </div>`
                }
            })
            return xhr2
        },
        success: function(response) {
            console.log(response)
        },
        error: function(error) {
            console.log(error)
        },
        cache: false,
        contentType: false,
        processData: false
    })
})
