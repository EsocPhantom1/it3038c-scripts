const http = require('http');

const data = [
  { name: 'Widget1', color: 'blue' },
  { name: 'Widget2', color: 'green' },
  
];

const server = http.createServer(function (req, res) {
  if (req.url === "/") {
    res.writeHead(200, { "Content-Type": "application/json" });
    res.end(JSON.stringify(data));
  } else if (req.url === "/blue") {
    const blueWidgets = data.filter(widget => widget.color === 'blue');
    res.writeHead(200, { "Content-Type": "application/json" });
    res.end(JSON.stringify(blueWidgets));
  } else {
    res.writeHead(404, { "Content-Type": "text/plain" });
    res.end("Data not found");
  }
});

const PORT = 3000; 

server.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
