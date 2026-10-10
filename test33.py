import socket
def find_local_ip():
    # gets the local IP address
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address
print(find_local_ip())
# displays the local IP address