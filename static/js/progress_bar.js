const uploadForm = document.getElementById('add__news__form')
const input = document.getElementById('id_photo_news')
console.log(input)

const progressBox = document.getElementById('progress-box')
const csrf = document.getElementsByName('csrfmiddlewaretoken')

input.addEventListener('change', ()=>{
    progressBox.classList.remove('not-visible')
    const img_data = input.files[0]
    const url = URL.createObjectURL(img_data)
    const fd = new FormData()
    fd.append('csrfmiddlewaretoken', csrf[0].value)
    fd.append('photo_news', img_data)

    $.ajax({
        type: 'POST',
        url: uploadForm.action,
        enctype: 'multipart/form-data',
        data: fd,
        beforeSend: function() {

        },
        xhr: function() {
            const xhr = new window.XMLHttpRequest();
            xhr.upload.addEventListener('progress', e=> {
                if (e.lengthComputable) {
                    const percent = e.loaded / e.total * 100
                    console.log(percent)
                    progressBox.innerHTML = `<div class="progress__block">
                                                  <div class="progress">
                                                      <div class="progress-bar" role="progressbar" style="width: ${percent}%" aria-valuenow="${percent}%" aria-valuemin="0" aria-valuemax="100"></div>
                                                  </div>
                                                  <p class="progress__int">${percent.toFixed(0)}%</p>
                                             </div>`
                }
            })
            return xhr
        },
        success: function(response) {
            console.log(response)
            imageBox.innerHTML = `<img src="${url}" class="edit__news__photo">`
        },
        error: function(error) {
            console.log(error)
        },
        cache: false,
        contentType: false,
        processData: false
    })
})