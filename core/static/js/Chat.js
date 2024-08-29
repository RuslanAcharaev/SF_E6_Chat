document.querySelector('#room-name-input').focus();

document.querySelector('#room-name-input').onkeyup = function(e) {
    if (e.keyCode === 13) {  // enter, return
        document.querySelector('#room-name-submit').click();
    }
};

document.querySelector('#room-name-submit').onclick = function(e) {
    var roomName = document.querySelector('#room-name-input').value;
    window.location.pathname = '/' + roomName + '/';
};

const roomName = JSON.parse(document.getElementById('room-name').textContent);

//const chatSocket = new WebSocket('ws://' + window.location.host + '/ws/' + roomName + '/');
const chatSocket = new WebSocket('ws://localhost:8000/ws/' + roomName + '/');

//chatSocket.onmessage = function(e) {
//    const data = JSON.parse(e.data);
//    document.querySelector('#chat-log').value += (data.message + '\n');
//};
chatSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    console.log(data);
    document.querySelector('#chat').innerText = data.message;
};

chatSocket.onclose = function(e) {
    console.error('Chat socket closed unexpectedly');
};

document.querySelector('#chat-message-input').focus();
document.querySelector('#chat-message-input').onkeyup = function(e) {
    if (e.keyCode === 13) {  // enter, return
        document.querySelector('#chat-message-submit').click();
    }
};

document.querySelector('#chat-message-submit').onclick = function(e) {
    const messageInputDom = document.querySelector('#chat-message-input');
    const message = messageInputDom.value;
    chatSocket.send(JSON.stringify({
        'message': message
    }));
    messageInputDom.value = '';
};
