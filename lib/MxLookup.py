import socket
import dns.resolver

def mx_lookup(site):
    try:
        # Fetch MX DNS records
        answers = dns.resolver.resolve(site, 'MX')
        mx_record = str(answers[0].exchange).rstrip('.')
        
        # Resolve IP address from MX target
        mx_ip = socket.gethostbyname(mx_record)
        
        # Perform reverse DNS lookup to get hostname
        try:
            mx_hostname = socket.gethostbyaddr(mx_ip)[0]
        except socket.herror:
            mx_hostname = mx_ip

        # Format output using ANSI escape sequences
        mx_result = f"\033[1m\033[36mIP      :\033[32m {mx_ip}\n\033[36mHOSTNAME:\033[32m {mx_hostname}\033[0m"
        return mx_result

    except Exception as e:
        return False

# Example usage:
# print(mx_lookup("google.com"))
