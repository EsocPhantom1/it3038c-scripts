This is a script that uses NodeJS to display the contents of a log file to the web page. To use this script properly you want to have both server.js and logfile.txt in the same folder in your file explorer. Then you want to install Node.js on their website (https://nodejs.org/en). Next you want to open your terminal and use the cd command followed by your path to your folder that contains both the server.js and logfile.txt files then you want to install the required Node.js packages (http, fs, path) using the npm command (nmp init -y) and (npm install) next you want to run the server.js script by running (node server.js), and finally you want to open your web browser and go to http://localhost:3000 and you should see the contents of logfile.txt. 
In the server.js file I first imported the required Node.js modules.
const http = require('http');
const fs = require('fs');
const path = require('path');

Next I created the HTTP server that listens on the port
const server = http.createServer((req, res)

Then I defined the request handler which reads the logfilepath contents.
fs.readFile(logFilePath, 'utf8', (err, data)

after that I handled read file callback that checks if there is any error when reading the file and if there is an error the script will send a 500 internal server response

if (err) {
      res.writeHead(500, { 'Content-Type': 'text/plain' });
      res.end('Internal Server Error');
      return;
    }

then next in my script is to send the file contents as a http response which sends the content as plain text because this is a log file

res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end(data);

this line of code defines the server port as 3000 in which the server will listen
const PORT = 3000;

 and finally the script will start listening for requests on port 3000 and also print a message saying that Server is running on http://localhost:${PORT}
server.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
