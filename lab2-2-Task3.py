'''
C00306572 Callum Matthews Class Group A
To make the starter code usuable, because it doesnt run, I need to define what ip_parse is

'''
from collections import defaultdict
import time

def top_n(counts, n=5):
    return sorted(counts.items(), key=lambda kv: kv[1], reverse=True)[:n]


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

start = time.time() # start counting

counts = defaultdict(int)           # Create a dictionary to keep track of IPs

with open("sample_auth_small.log") as f:
    for line in f:
        if "Failed password" in line or "Invalid user" in line:
            # extract ip
            ip = ip_parse(line)
            if ip:
              counts[ip] += 1

final_list = top_n(counts)
num = 0

print("Top 5 attackers:")
for i in final_list:
    num += 1
    print(num, ".",  i[0], "-", i[1])


end = time.time() #stop counting

with open('failed_counts.txt', 'w') as f:
    f.write("Failed Password Attemps: \n")
    for i in final_list:
        f.write(str(i[0]) + str(i[1]) + "\n")


print("Elapsed:", end-start, "seconds")
