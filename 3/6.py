ports = {
    20: "FTP Data",
    21: "FTP Control",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    443: "HTTPS",
    3306: "MySQL"
}
def search_by_port(port_num):
    if port_num in ports:
        return f"Port {port_num}: {ports[port_num]}"
    else:
        return f"Port {port_num} not found"

port = int(input("Enter Port Number : "))
print (search_by_port(port))