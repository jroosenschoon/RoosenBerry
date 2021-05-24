import yaml
from dns_server import DNS_Server
def start_server():
    with open("config.yaml", 'r') as f:
        config = yaml.safe_load(f)
    print("Welcome to RoosenBerry!")
    print("WARNING: This is a developmental server that is for experimental purposes only")

    print(config)
    dns_server = DNS_Server(config['dns_servers'], config['tld'], "192.168.1.29")
    dns_server.run_server()




if __name__ == '__main__':
    start_server()

