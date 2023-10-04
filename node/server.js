var http = require("http");
var fs = require("fs");
var os = require("os");
var ip = require('ip');

http.createServer(function(req, res){

    if (req.url === "/") {
        fs.readFile("./public/index.html", "UTF-8", function(err, body){
            res.writeHead(200, {"Content-Type": "text/html"});
            res.end(body);
        });
    }
    else if(req.url.match("/sysinfo")) {
        myHostName = os.hostname();
        uptime = os.uptime();
        totalMemory = os.totalmem();
        freeMemory = os.freemem();
        numCPUs = os.cpus().length;
		
		const days = Math.floor(uptime / (60 * 60 * 24));
		const hours = Math.floor((uptime % (60 * 60 * 24)) / (60 * 60));
		const minutes = Math.floor((uptime % (60 * 60)) / 60);
		const seconds = Math.floor(uptime % 60);

        html = `    
        <!DOCTYPE html>
        <html>
          <head>
            <title>Node JS Response</title>
          </head>
          <body>
            <p>Hostname: ${myHostName}</p>
            <p>IP: ${ip.address()}</p>
            <p>Server Uptime: Days: ${days},Hours: ${hours}, Minutes: ${minutes},Seconds: ${seconds}</p>
            <p>Total Memory: ${(totalMemory / (1024 * 1024)).toFixed(3)} MB</p>
            <p>Free Memory: ${(freeMemory / (1024 * 1024)).toFixed(2)} MB</p>
            <p>Number of CPUs: ${numCPUs}</p>            
          </body>
        </html>`;

        res.writeHead(200, {"Content-Type": "text/html"});
        res.end(html);
    }
    else {
        res.writeHead(404, {"Content-Type": "text/plain"});
        res.end(`404 File Not Found at ${req.url}`);
    }
}).listen(3000);

console.log("Server listening on port 3000");