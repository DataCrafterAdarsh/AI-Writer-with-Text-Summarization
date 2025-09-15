AI Text Summarizer – How to Run and Use
=======================================

Requirements
------------
• Windows PC with Python / Anaconda installed
• Project files:
    - app.py
    - summarizer.py  (or your AI model code)
    - templates/index.html

Folder Layout
-------------
D:\summarizer_project\
│
├─ app.py
├─ summarizer.py
└─ templates\
    └─ index.html

How to Start the App
--------------------
1. Open a terminal inside the project folder:
   - Right-click inside the folder → “Open in Terminal”
   - Or open *Anaconda Prompt* and run:
        cd D:\summarizer_project

2. Start Flask:
   - If Python is on your PATH:
        python app.py
   - If not, use the full path:
        "D:\anaconda_projects\Newclnda\python.exe" app.py

3. Wait for the message:
       Running on http://127.0.0.1:5000

4. Open a browser and go to:
       http://127.0.0.1:5000

How to Use
----------
1. Paste or type text into the box on the page.
2. Click **Summarize**.
3. The summary will appear instantly on the page.

Stopping the App
----------------
• Press CTRL + C in the terminal window to stop the server.

Optional (Easy Start)
---------------------
Create a file named `start_summarizer.bat` with:

    cd /d D:\summarizer_project
    "D:\anaconda_projects\Newclnda\python.exe" app.py

Save it on your desktop.  
Double-click it any time to start the server.

Support
-------
If the app doesn’t open:
• Make sure `app.py` is inside the correct folder.
• Check that Python / Anaconda is installed and working:
      python --version
• Keep the terminal window open while using the app.
