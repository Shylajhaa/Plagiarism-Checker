/*var express = require('express');
var app = express();
var path = require('path');
//var routes = require('.api//routes');
var PythonShell = require('python-shell');
var bodyParser = require('body-parser');
app.set('port',3000);
app.use(express.static(path.join(__dirname,'public')));
app.use(bodyParser.urlencoded({ extended : true}));
app.use(bodyParser.json());
var abs;
app.post('/', function(request, response){
    abs = request.body.abstract;
    
});
var data = abs;
console.log(data);


PythonShell.run('sample.py', function (err) {
  if (err) throw err;
  console.log('finished');
});
//app.use('/api',routes);
/*app.get('/',function(req,res){
	console.log('get the homepage');
	res.sendFile(path.join(__dirname,'public','index.html'));
});
app.get('/file',function(req,res){
	console.log('get the file');
	res.sendFile(path.join(__dirname,'app.js'));
	});
app.listen(app.get('port'),function(){
	console.log('hii');
});*/

var express = require('express');
var app = express();
var path = require('path');
//var routes = require('.api//routes');
var PythonShell = require('python-shell');
var spawn = require('child_process').spawn;
var py    = spawn('python', ['sample.py']);
var bodyParser = require('body-parser');
app.set('port',3000);
app.use(express.static(path.join(__dirname,'public')));
app.use(bodyParser.urlencoded({ extended : true}));
app.use(bodyParser.json());
app.post('/', function(req, res){
    var abs = req.body.abstract;
    var spawn = require('child_process').spawn;
     var py=spawn('python', ['sample.py']);
     py.stdout.on('data',function(data){
      console.log(data.toString());
      res.write(data);
      res.end('end');

     });
    res.send(abs);
    
});

/*PythonShell.run('/sample.py', function (err) {
  if (err) throw err;
  console.log('finished');
});*/

//app.use('/api',routes);
/*app.get('/',function(req,res){
console.log('get the homepage');
res.sendFile(path.join(__dirname,'public','index.html'));
});*/

app.get('/file',function(req,res){
console.log('get the file');
res.sendFile(path.join(__dirname,'app.js'));
});
app.listen(app.get('port'),function(){
console.log('hii');
});

