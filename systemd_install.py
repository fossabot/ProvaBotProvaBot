import os
os.system("git clone https://github.com/fuomag9/ProvaBotProvaBot")
testo="""[Unit]
Description=ProvaBotProvaBot
After=multi-user.target

[Service]
Type=idle
ExecStart=/root/ProvaBotProvaBot/start.sh
ExecStop=killall python3
Restart=always
RestartSec=2
StandardOutput=journal

[Install]
WantedBy=multi-user.target"""
os.system("touch /lib/systemd/system/ProvaBotProvaBot.service")
with open('/lib/systemd/system/ProvaBotProvaBot.service') as f:
    f.write(testo)
path=os.getcwd()
os.system("touch "+path+"/start.sh")
key=input("Enter here your telegram bot api key\n")
testo2=("""#!/bin/sh\npython3 -u /root/ProvaBotProvaBot/ProvaBotProvaBot.py -k """+key)
with open(path+"/start.sh") as f:
    f.write(testo2)
os.system("chmod +x "+path+"/start.sh; systemctl daemon-reload; systemctl enable ProvaBotProvaBot; systemctl start ProvaBotProvaBot"")
risposta=input("Do you want to delete this install script?\n")
if ("yes" or "YES" in risposta):
    os.system("rm "+path+"/systemd_install.py")