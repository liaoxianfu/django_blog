//config.js
KindEditor.ready(function(K) {
    //通过浏览器调试查看富文本相关信息，如id，name
    window.editor = K.create('textarea[name=body]',{

        // 指定大小
        width:'1200px',
        height:'500px',
    });
});