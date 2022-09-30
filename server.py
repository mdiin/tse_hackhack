import http.server
from http.server import HTTPServer, BaseHTTPRequestHandler, SimpleHTTPRequestHandler
import drone

class MyHttpRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        print("yAY")
        self.send_response(200)
        self.send_header("content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("Fly, biatch!", "utf-8"))
        drone.start_the_drone()
def run(server_class=HTTPServer):
    server_address = ("", 8000)
    httpd = server_class(server_address, MyHttpRequestHandler)
    httpd.serve_forever()
run()
