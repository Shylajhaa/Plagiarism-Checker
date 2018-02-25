var express = require('express');
var app = express();
var path = require('path');     
var fs = require('fs');
//var sleep = require('sleep');

//var routes = require('.api//routes');
var PythonShell = require('python-shell');
//var spawn = require('child_process').spawn;
//var py    = spawn('python', ['sample.py']);
var bodyParser = require('body-parser');
app.set('port',3000);
app.use(express.static(path.join(__dirname,'public')));
app.use(bodyParser.urlencoded({ extended : true}));
app.use(bodyParser.json());
app.post('/', function(req, res)
{
    var abs = req.body.abstract;
    fs.writeFile('abstract.txt', abs, (err) => {  
    // throws an error, you could also catch it here
    if (err) throw err;

    // success case, the file was saved
    console.log('abstract saved!');
});


     
  var spawn = require('child_process').spawn;
  var py=spawn('python', ['main.py']);
  py.stdout.on('data',function(data,err){
          if (err) throw err;
          });



setTimeout(writeFunc(),50000);

        function writeFunc()
        {
        console.log(data.toString());
        res.write(data);
        res.end('end');
      }

    //res.send(abs);
    /*fs.readFile('output.txt', {encoding: 'utf-8'}, function(err,data){
    if (!err) {
        console.log('received data: ' + data);
        res.writeHead(200, {'Content-Type': 'text/html'});
        res.write(data);
        
    } else {
        console.log(err);
    }
});
*/
    

     
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
































/*var pyshell = new PythonShell('sample.py');
            pyshell.send(JSON.stringify(abstract.txt))
            pyshell.on('message', function (message) {
    // received a message sent from the Python script (a simple "print" statement)
            var jsondata = message
            console.log(jsondata);
            });

// end the input stream and allow the process to exit
            pyshell.end(function (err) {
             if (err)
                throw err;
                
                });*/

  /* var options = {
  mode: 'text',
  pythonPath: 'sample.py',
  pythonOptions: ['-u'],
  scriptPath: '/',
  args: ['abstract.txt']
};

PythonShell.run('sample.py', options, function (err, results) {
  if (err) throw err;
  // results is an array consisting of messages collected during execution
  console.log(results);
});*/