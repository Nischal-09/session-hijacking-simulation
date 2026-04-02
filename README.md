# Session Hijacking Simulation Project

This project demonstrates how session cookies can be captured using a Chrome extension and logged to a local server. This is part of a security simulation to understand cookie-based vulnerabilities.

## ⚠️ Educational Purpose Only
This repository is for educational and security research purposes only. **Do not use this for any unauthorized or illegal activities.**

## Project Structure
- `/extension`: The Chrome extension used for capturing cookies.
- `/server`: The Flask server (`stealer.py`) that receives and logs the cookie data.

## How to Set Up
1. **Server**: 
    - Navigate to the `/server` folder.
    - **SSL/TLS Setup**: This project requires HTTPS. Generate your local certificates (ignored by Git) by running:
      ```bash
      openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes
      ```
    - Run `python stealer.py`.
2. **Extension**: 
   - Open Chrome and go to `chrome://extensions`.
   - Enable "Developer mode" in the top right.
   - Click "Load unpacked" and select the `/extension` folder.
   - **Important**: Go to details and enable "Allow in Incognito" to capture cookies in private windows.

## How to Use
- Once the extension is loaded, log into a test site or similar in an Incognito window.
- The extension will capture the session cookies and send them to your local Flask server.
- Review the server logs to see the captured session headers.
