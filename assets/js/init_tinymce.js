(function () {
    // ساخت لودر
    var loader = document.createElement('div');
    loader.id = 'editor-loader';
    loader.style.position = 'relative';
    loader.style.height = '500px';
    loader.style.display = 'flex';
    loader.style.alignItems = 'center';
    loader.style.justifyContent = 'center';

    var spinner = document.createElement('div');
    spinner.style.width = '50px';
    spinner.style.height = '50px';
    spinner.style.border = '5px solid #f3f3f3';
    spinner.style.borderTop = '5px solid #3498db';
    spinner.style.borderRadius = '50%';
    spinner.style.animation = 'spin 1s linear infinite';

    loader.appendChild(spinner);
    document.addEventListener('DOMContentLoaded', function () {
        var textarea = document.querySelector('textarea');
        if (textarea) {
            textarea.style.visibility = 'hidden';
            textarea.parentNode.insertBefore(loader, textarea);
        }
    });

    // اضافه کردن استایل انیمیشن چرخش
    var style = document.createElement('style');
    style.innerHTML = `
    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    `;
    document.head.appendChild(style);

    // لود tinymce
    var script = document.createElement('script');
    script.src = "https://cdn.jsdelivr.net/npm/tinymce@6/tinymce.min.js";
    script.referrerPolicy = "origin";

    script.onload = function () {
        tinymce.init({
            selector: 'textarea',
            height: 500,
            menubar: true,
            plugins: [
                'advlist', 'autolink', 'lists', 'link', 'image', 'charmap', 'preview',
                'anchor', 'searchreplace', 'visualblocks', 'code', 'fullscreen',
                'insertdatetime', 'media', 'table', 'help', 'wordcount'
            ],
            toolbar: 'undo redo | blocks | bold italic underline strikethrough | ' +
                     'alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | ' +
                     'link image media table | code preview fullscreen',
            content_style: 'body { font-family:Helvetica,Arial,sans-serif; font-size:14px }',
            relative_urls: false,
            remove_script_host: false,
            branding: false,
            base_url: "https://cdn.jsdelivr.net/npm/tinymce@6",
            setup: function (editor) {
                editor.on('init', function () {
                    var loaderEl = document.getElementById('editor-loader');
                    if (loaderEl) loaderEl.remove();
                    var textarea = document.querySelector('textarea');
                    if (textarea) textarea.style.visibility = 'visible';
                });
            }
        });
    };

    document.head.appendChild(script);
})();
