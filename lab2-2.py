# lab2-2_starter.py

LOGFILE = "sample_auth_small.log"  # change filename if needed
import re
ips=[]  #declare the empty list which I will append to fill with IP addresses to print
counter = 0

def simple_parser(line):
    """
    looks for the substring ' port ' and returns the following port number.
    Returns None if no matching substring found.
    """
    if " from " in line:
        parts = line.split() # splits the line into tokens, seperates by spaces by default
        try:
            anchor = parts.index("from")    # Find the position of the token "from", our anchor
            ip = parts[anchor+1]          # the from value will be next token, anchor+1
            return ip.strip()             # strip any trailing punctuation
        
        except (ValueError, IndexError):
            return None

    return None

#find uniqe IP'S
with open('sample_auth_small.log', 'r') as f:
    for line in f:
        ip_pattern = r"\d+\.\d+\.\d+\.\d+"
        found_ips = re.findall(ip_pattern,line)
        for ip in found_ips:
            ips.append(ip)
            #counter +=1

unique_ips = set(ips)

# Print each unique IP
print("Unique IPs:")
for ip in unique_ips:
    counter +=1
    print(ip)

print("The amount of unique IP's is: ",counter)


## This is the main block that will run first. 
## It will call any functions from above that we might need.
'''if __name__ == "__main__":

    with open(LOGFILE, "r") as f:
        for line in f:
            print (simple_parser(line.strip()))'''

    