'''
C00306572 Callum Matthews Class Group A
To make the starter code usuable, because it doesnt run, I need to define what ip_parse is

'''
from collections import defaultdict
def ip_parse(line):
    """
    looks for the substring ' from ' and returns the following ip address.
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

counts = defaultdict(int)           # Create a dictionary to keep track of IPs

with open("sample_auth_small.log") as f:
    for line in f:
        if "Failed password" in line or "Invalid user" in line:
            # extract ip
            ip = ip_parse(line)
            if ip:
              counts[ip] += 1

print(counts)
