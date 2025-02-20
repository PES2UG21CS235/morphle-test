from django.http import HttpResponse
import getpass
import time
import pytz
from subprocess import check_output

def htop(request):
    name = "Kotapati Gowtham Sai Ram Reddy"
    username = getpass.getuser()
    tz = pytz.timezone('Asia/Kolkata')
    server_time = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())
    top_output = check_output(['top', '-b', '-n', '1']).decode('utf-8')
    response = f"""
    <html>
    <body>
    <h1>System Information</h1>
    <p>Name: {name}</p>
    <p>Username: {username}</p>
    <p>Server Time (IST): {server_time}</p>
    <pre>{top_output}</pre>
    </body>
    </html>
    """
    return HttpResponse(response)