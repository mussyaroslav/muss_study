const uploadForm1 = document.getElementById('setting-form')
const input1 = document.getElementById('upload-photo-profile')
console.log(input1)

const progressBox1 = document.getElementById('progress-box')
const csrf1 = document.getElementsByName('csrfmiddlewaretoken')

input1.addEventListener('change', ()=>{
    progressBox1.classList.remove('not-visible')
    const img_data1 = input1.files[0]
    const fd1 = new FormData()
    fd1.append('csrfmiddlewaretoken', csrf1[0].value)
    fd1.append('photo', img_data1)

    $.ajax({
        type: 'POST',
        url: uploadForm1,
        enctype: 'multipart/form-data',
        data: fd1,
        beforeSend: function() {

        },
        xhr: function() {
            const xhr1 = new window.XMLHttpRequest();
            xhr1.upload.addEventListener('progress', e=> {
                if (e.lengthComputable) {
                    const percent1 = e.loaded / e.total * 100
                    console.log(percent1)
                    progressBox1.innerHTML = `<div class="progress__block2">
                                                  <div class="progress">
                                                      <div class="progress-bar" role="progressbar" style="width: ${percent1}%" aria-valuenow="${percent1}%" aria-valuemin="0" aria-valuemax="100"></div>
                                                  </div>
                                                  <p class="progress__int">${percent1.toFixed(0)}%</p>
                                             </div>`
                }
            })
            return xhr1
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
