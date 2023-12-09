import http.server
import socketserver

# Set the port number you want the server to run on
PORT = 8080

# Define a custom handler to handle incoming requests
class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Send a response indicating success and provide content
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"Hello, this is a simple web server!")

# Create a socket server with the defined port and handler
with socketserver.TCPServer(("", PORT), MyHttpRequestHandler) as httpd:
    print(f"Server started on port {PORT}")
    # Keep the server running until interrupted
    httpd.serve_forever()