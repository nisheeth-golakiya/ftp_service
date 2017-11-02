
var express = require('express');
var app=express();
var http = require('http').Server(app);
var io=require('socket.io')(http);
var pyshell = require('python-shell');
var shell = new pyshell('server.py');
app.set('port',(process.env.PORT||3000));
http.listen (app.get('port'),function() {
  console.log("listening to port number "+app.get('port'));
});
app.get('/',function(req,res){
  res.sendFile(__dirname + '/index.html');
});
io.sockets.on("connection",function(socket){
  socket.on("servpath",function(data){
    shell.send(data);
  });

  socket.on("servip",function(data){
    shell.send(data);
    console.log(data);
  });

  socket.on("servport",function(data){
    shell.send(data);
    console.log(data);
  });

});
