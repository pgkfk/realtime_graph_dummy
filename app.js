//UDP from  iot_wifi.py
var PORT = 8081;
var HOST = '127.0.0.1';


var dgram = require('dgram');
var server = dgram.createSocket('udp4');

//Graph SetUp
var express = require('express');
var app = express();
var http_server = require('http').Server(app);
var socketio = require('socket.io')(http_server);
http_server.listen(3000);

app.use(express.static(__dirname + '/public'));

var temp = 0

server.on('listening', function () {
    var address = server.address();
    console.log('UDP Server listening on ' + address.address + ":" + address.port);
});

server.on('message', function (message, remote) {
    // console.log(remote.address + ':' + remote.port +' - ' + message);
    var data = message.toString('utf8').split('_');
    //For Graph
    socketio.emit("paramData", {temperature:data[0],id:data[1]});
    console.log(data)

});
// 
server.bind(PORT, HOST);
module.exports = app;
