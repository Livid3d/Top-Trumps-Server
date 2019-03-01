import http.server
import socketserver
import os
import zipfile

PORT = 8000

def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))

import os
os.remove("PythonCode.zip")

zipf = zipfile.ZipFile('PythonCode.zip', 'w', zipfile.ZIP_DEFLATED)
zipdir('/coder/mnt/LividPython/TopTrumps2/', zipf)
zipf.close()

# Server
Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", PORT), Handler)
print("serving at port", PORT)
httpd.serve_forever()
#input("")
#print(f"closing server on port {PORT}")
#httpd.server_close()

