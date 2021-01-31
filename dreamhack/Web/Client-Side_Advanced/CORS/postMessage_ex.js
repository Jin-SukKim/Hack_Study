window.onmessage = function (e) {
    var dialog = document.getElementById('my-dialog');
    if (dialog == null) {
        dialog = document.createElement('dialog');
        dialog.id = 'my-dialog';
        document.body.appendChild(dialog);
    }
    dialog.setAttribute('open', '');
    dialog.innerHTML = e.data;
};

// =========== IFrame functions ==============

function bob(targetOrigin) {
    parent.postMessage('<strong>안내</strong> 작업이 완료되었습니다.', targetOrigin);
}

function attacker(targetOrigin) {
    parent.postMessage('XSS attack<img src=about:invalid onerror=alert(document.domain)>', targetOrigin);
}

// =========== launcher ==============

function inside(fn) {
    document.addEventListener('DOMContentLoaded', function() {
        var b = document.createElement('button');
        b.type = 'button';
        b.addEventListener('click', function () {
            fn('*');
        });
        b.textContent = fn.name;
        document.body.appendChild(b);
    });
}

// ============ Main =============

function cdata(x) {
    return (''+x)
        .replace(/\//g, '\\/')
        .replace(/\u2028/g, '\\u2028')
        .replace(/\u2029/g, '\\u2029');
}


function toButton(fn) {
    var f = document.createElement('iframe');
    f.sandbox = 'allow-scripts';
    f.srcdoc = `<style>
html,body{margin:0;padding:0;}
body>button:only-child{
display:block;position:absolute;
width:100%;
left:0;right:0;top:0;bottom:0;
}
    </style>
    <script>
    (${cdata(inside)})(${cdata(fn)})
    <\/script>`;
    document.body.appendChild(f);
}

document.addEventListener('DOMContentLoaded', function () {
    toButton(bob);
    toButton(attacker);
});