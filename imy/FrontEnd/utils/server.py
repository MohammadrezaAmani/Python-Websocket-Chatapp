import http

# http server
import http.server

# send html, css and js
import os
import jinja2

# parse url
import urllib.parse

class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        # parse url
        parsed_path = urllib.parse.urlparse(self.path)
        # get path
        path = parsed_path.path
        # get query
        query = parsed_path.query

        # get html
        if path == "/":
            # get html
            html = self.get_html()
            # send response
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(html.encode("utf-8"))
        # get css
        elif path == "/style.css":
            # get css
            css = self.get_css()
            # send response
            self.send_response(200)
            self.send_header("Content-type", "text/css")
            self.end_headers()
            self.wfile.write(css.encode("utf-8"))
        # get js
        elif path == "/script.js":
            # get js
            js = self.get_js()
            # send response
            self.send_response(200)
            self.send_header("Content-type", "text/javascript")
            self.end_headers()
            self.wfile.write(js.encode("utf-8"))
        # get json
        elif path == "/data.json":
            # get json
            json = self.get_json()
            # send response
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.encode("utf-8"))
        # get favicon
        elif path == "/favicon.ico":
            # send response
            self.send_response(200)
            self.send_header("Content-type", "image/x-icon")
            self.end_headers()
            self.wfile.write(b"")
        # get 404
        else:
            # send response
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"404 Not Found")

    def get_html(self):
        # get template
        template = self.get_template("index.html")
        # render template
        html = template.render()
        # return html
        return html

    def get_css(self):
        # get template
        template = self.get_template("style.css")
        # render template
        css = template.render()
        # return css
        return css
    
    def get_js(self):
        # get template
        template = self.get_template("app.js")
        # render template
        js = template.render()
        # return js
        return js

    def get_json(self):
        # get template
        template = self.get_template("data.json")
        # render template
        json = template.render()
        # return json
        return json

    def get_template(self, path):
        # get template
        template = self.env.get_template(path)
        # return template
        return template
    
    def baseTemplate(self):
        jinjahtml = """
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <title>imy</title>
            <link rel="stylesheet" href="style.css">
        </head>
        <body>
            <div id="app"></div>
            <h1> hello world! </h1>
            <script src="script.js"></script>
        </body> 
        </html>
        """
        return jinja2.Template(jinjahtml)
    
    def __init__(self, *args, **kwargs):
        # get current directory
        current_dir = os.path.dirname(os.path.abspath(__file__))
        # get template directory
        template_dir = os.path.join(current_dir, "templates")
        # set template environment
        self.env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir))
        # call super
        super().__init__(*args, **kwargs)
    
    
web = http.server.HTTPServer(("localhost", 8080), MyHandler)
web.serve_forever()