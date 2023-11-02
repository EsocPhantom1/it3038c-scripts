const http = require('http');
const fs = require('fs');

const data = [
  { name: 'Widget1', color: 'blue' },
  { name: 'Widget2', color: 'green' },
  // Add more widget data as needed
];

const server = http.createServer(function (req, res) {
  if (req.url === "/") {
    serveHtmlPage(res, data.map(widget => `${widget.name} is ${widget.color}.`).join('<br>'));
  } else if (req.url === "/blue") {
    const blueWidgets = data.filter(widget => widget.color === 'blue');
    serveHtmlPage(res, blueWidgets.map(widget => `${widget.name} is ${widget.color}.`).join('<br>'));
  } else if (req.url === "/green") {
    const greenWidgets = data.filter(widget => widget.color === 'green');
    serveHtmlPage(res, greenWidgets.map(widget => `${widget.name} is ${widget.color}.`).join('<br>'));
  } else {
    res.writeHead(404, { "Content-Type": "text/plain" });
    res.end("Data not found");
  }
});

function serveHtmlPage(res, content) {
  res.writeHead(200, { "Content-Type": "text/html" });

  // Create an HTML page with widget information
  const htmlContent = `
    <!DOCTYPE html>
    <html>
    <head>
      <title>Widget Information</title>
    </head>
    <body>
      <h1>Widget Information</h1>
      <p>${content}</p>
    </body>
    </html>
  `;

  res.end(htmlContent);
}

const PORT = 3001;

server.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});

