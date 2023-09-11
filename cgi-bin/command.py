#!/usr/bin/python3
print("content-type: text/html")
print()

import cgi
import subprocess
form = cgi.FieldStorage()
cmd = form.getvalue("c")

if "date" in cmd:
    output = subprocess.getoutput("date")
    print(output)
elif "cal" in cmd:
    output = subprocess.getoutput("cal")
    print(output)
elif "docker" in cmd:
    output = subprocess.getoutput("sudo docker ps")
    print(output)
elif "df" in cmd:
    output = subprocess.getoutput("sudo df")
    print(output)
elif "ifconfig" in cmd:
    output=subprocess.getoutput("ifconfig")
    print(output)
elif "ls" in cmd:
    output=subprocess.getoutput("ls")
    print(output)
elif "whoami" in cmd:
    output=subprocess.getoutput("whoami")
    print(output)
elif "pwd" in cmd:
    output=subprocess.getoutput("pwd")
    print(output)
elif "useradd" in cmd:
    output=subprocess.getoutput("useradd")
    print(output)
elif "tail" in cmd:
    output=subprocess.getoutput("tail command.py")
    print(output)
elif "env" in cmd:
    output=subprocess.getoutput("env")
    print(output)
elif "uptime" in cmd:
    output = subprocess.getoutput("uptime")
    print(output)
elif "ps" in cmd:
    output = subprocess.getoutput("ps aux")
    print(output)
elif "top" in cmd:
    output = subprocess.getoutput("top -n 1")
    print(output)
elif "netstat" in cmd:
    output = subprocess.getoutput("netstat -tuln")
    print(output)
elif "free" in cmd:
    output = subprocess.getoutput("free -m")
    print(output)
else:
    print("Invalid command")
