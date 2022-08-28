import datetime
import time
endtime=datetime.datetime(2022,7,14)
siteblock=["kspaceinterior.com"]
host="C:/Windows/System32/drivers/etc/hosts"
redirect="127.0.0.1 "

while True:
    if endtime<datetime.datetime.now()<endtime:
        print("Start Blocking")
        with open(host,"r+") as host_file:
            content=host_file.read()
        for website in siteblock:
            if website not in content:
                host_file.write(redirect +" "+website+"/n")

    else:
        with open(host, "r+") as host_file:

            content=host_file.readlines()
            host_file.seek(0)
            for lines in content:
                if not any(website in lines for website in siteblock):
                    host_file.write(lines)

            host_file.truncate()
            time.sleep(5)

