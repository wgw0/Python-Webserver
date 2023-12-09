import http.server
import socketserver

# Set the port number you want the server to run on
PORT = 8080

# Define a custom handler to handle incoming requests
class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Check if the request is for '/'
        if self.path == '/':
            self.path = '/index.html'  # Serve index.html by default

        # Call the parent class's method to handle the request
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

# Create a socket server with the defined port and handler
with socketserver.TCPServer(("", PORT), MyHttpRequestHandler) as httpd:
    print(f"Server started on port {PORT}")
    # Keep the server running until interrupted
    httpd.serve_forever()
