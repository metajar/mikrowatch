from librouteros import connect
from datetime import datetime
from tinydb import TinyDB, Query
from pushover import init, Client

app_key = "shs8088d0f88908dsf8098390jkdfj20323"
user_key = "ds809f89320890if9d0s8fa09830928f09ad"

db = TinyDB('mikrowatch.json')

class MikroWatcher:
    def __init__(self, host, username, password):
        init(app_key)
        self.host = host
        self.username = username
        self.password = password
        self.api = connect(host=host, username=username, password=password)

    @property
    def watch(self):
        s = Query()
        arps = self.api(cmd='/ip/arp/print')
        leases = self.api(cmd='/ip/dhcp-server/lease/print')
        for x in arps:
            try:
                if db.search(s['mac-address'] == x['mac-address']):
                    print("ALREADY KNOWN {}".format(x['mac-address']))
                else:
                    print("FOUND NEW MAC ADDRESS {}".format(x['mac-address']))
                    db.insert(x)
                    try:
                        ip = x['address']
                    except:
                        ip = "Not Available"
                    try:
                        for l in leases:
                            if x['mac-address'] == l['mac-address']:
                                deets = l
                    except:
                        deets = {}
                    Client(user_key).send_message("New Device On The Network {} - {}\n\n{}".format(ip, x['mac-address'], deets), title="New MAC Address Found")
            except:
                pass

if __name__ == '__main__':
    m = MikroWatcher('192.168.88.1','api','api')
    m.watch