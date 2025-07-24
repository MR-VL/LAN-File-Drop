document.getElementById('upload-form').addEventListener('submit', async function(e){
    e.preventDefault();
    const input = document.getElementById('file-input');
    const formData = new FormData();

    for (let file of input.files){
        formData.append('files[]', file);
    }

    const result = await fetch('/upload', {
        method: 'POST',
        body: formData,
    })

    const status = document.getElementById('status');

    if (result.ok){
        status.innerText = "Upload Completed";
        input.value = '';
    }
    else{
        status.innerText = "Upload Failed";
    }
})