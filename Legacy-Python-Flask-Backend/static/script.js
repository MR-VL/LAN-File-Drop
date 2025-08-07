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
        const data = await result.json();
        let message = `Uploaded: ${data.uploaded.length} file(s).`;

        if (data.failed.length > 0){
            message += `\nFailed: ${data.failed.length} file(s).\n`;
            data.failed.forEach(f => {
                message += ` - ${f.filename}: ${f.reason}\n`;
            });
        }

        status.innerText = message;
        input.value = '';
    }
    else{
        status.innerText = "[ERROR]: Upload Failed Entirely. Please see log and try again.";
    }
});

document.getElementById('clear-selection').addEventListener('click', function(){
    document.getElementById('file-input').value = '';
    document.getElementById('status').innerText = 'Selection Cleared.';
});