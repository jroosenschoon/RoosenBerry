import serializeme
from serializeme import Serialize
import socket


class DNS_Server:
    def __init__(self, domain_servers, tld, addr, port=53):
        self.tld = tld
        self.domain_servers = domain_servers
        self.addr = addr
        self.port = port

        self.dns_request = {
            "ID": "2B",
            "!!2B": {
                'QR': '1b',
                'OPCODE': '4b',
                'AA': '1b',
                'TC': '1b',
                'RD': '1b',
                'RA': '1b',
                "Z": "3b",
                "RCODE": "4b",
            },
            "QDCOUNT": ("2B", "", "QUERIES"),
            "ANCOUNT": "2B",
            "NSCOUNT": "2B",
            "ARCOUNT": "2B",
            "QUERIES": {
                "QNAME": (serializeme.NULL_TERMINATE, serializeme.HOST),
                "QTYPE": "2B",
                "QCLASS": "2B"
            }
        }

        host_name = socket.gethostname()
        ip_address = socket.gethostbyname(host_name)
        print("Host name: ", host_name)
        print("IP Address:", ip_address)

    def run_server(self):
        sd = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sd.bind((self.addr, self.port))
        print("[+] DNS Server running at ", self.addr, ":", self.port, "...")
        while True:
            if sd.recv is not None:
                data, addr = sd.recvfrom(1024)
                self.__handle_query(data, addr)

    def __handle_query(self, data, addr):
        request = serializeme.Deserialize(data, self.dns_request)

    def __generate_dns_header(self, id, qr=0, opcode=0, aa=0, tc=0, rd=0, ra=0, z=0, rcode=0):
        dns_header = {
            "ID": ("2B", id),
            "QR": (1, qr),
            "OPCODE": (4, opcode),
            "AA": (1, aa),
            "TC": (1, tc),
            "RD": (1, rd),
            "RA": (1, ra),
            "Z": (3, z),
            "RCODE": (4, rcode)
        }
        return Serialize(dns_header)
