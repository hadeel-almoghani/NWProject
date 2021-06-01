from http.server import BaseHTTPRequestHandler, HTTPServer

class Serv(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        try:
            File_to_open = open(self.path[1:]).read()
            self.send_response(200)
        except:
            self.path =  '/404.html'
            File_to_open = open(self.path[1:]).read()
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(File_to_open,'utf-8'))




httpd = HTTPServer(('localhost', 8888), Serv)
httpd.serve_forever()

