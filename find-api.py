import httpx, json
from rich import print
from rich.table import Table
from rich.panel import Panel
from rich.align import Align
from rich import box
import socket
import time
import subprocess

# banner
banner = Align.center("""
           ╔═╗  ╦  ╔╗╔  ╔╦╗  ╔═╗  ╔═╗  ╦
           ╠╣   ║  ║║║   ║║  ╠═╣  ╠═╝  ║
           ╚    ╩  ╝╚╝  ═╩╝  ╩ ╩  ╩    ╩

  Alat Menggunakan Seneu. silahkan daftar https://ipfind.co/
""")
class Main:
    def __init__(self):
        subprocess.call('clear',shell=False)
        print(Panel(banner,highlight=True,border_style="gray23 bold"))
        self.ip_address = input('hostname : ')
        time.sleep(1)
        self.so = socket.gethostbyname(self.ip_address)
        self.auth = '6ea90bb3-e2cf-4648-b44e-f7466909f2da'
        self.url = f'https://ipfind.co/?auth={self.auth}&ip={self.so}'
        self.response = httpx.get(self.url)
        self.data = json.loads(self.response.text)
        self.ip_address = self.data['ip_address']
        self.country = self.data['country']
        self.country_code = self.data['country_code']
        self.continent = self.data['continent']
        self.continent_code = self.data['continent_code']
        self.city = self.data['city']
        self.county = self.data['county']
        self.region = self.data['region']
        self.region_code = self.data['region_code']
        self.postal_code = self.data['postal_code']
        self.timezone = self.data['timezone']
        self.owner = self.data['owner']
        self.longitude = self.data['longitude']
        self.latitude = self.data['latitude']
        self.currency = self.data['currency']
        self.languages = self.data['languages']
    
    @classmethod
    def tables(self):
        ap = Main()
        x = Table(box=box.SQUARE_DOUBLE_HEAD,border_style='gray23 bold')
        super_x = Align.center(x)
        x.add_column('column1',style='blue bold')
        x.add_column('column2',style='green bold')
        x.add_row('ip_address',ap.ip_address)
        x.add_row('country',ap.country)
        x.add_row('country_code',ap.country_code)
        x.add_row('continent',ap.continent)
        x.add_row('country_code',ap.continent_code)
        x.add_row('city',ap.city)
        x.add_row('county',ap.county)
        x.add_row('region',ap.region)
        x.add_row('region_code',ap.region_code)
        x.add_row('postal_code',ap.postal_code)
        x.add_row('timezone',ap.timezone)
        x.add_row('owner',ap.owner)
        x.add_row('currency',ap.currency)
        print(x)

if __name__ == "__main__":
    Main.tables()


