#lab2-2 C00306572 Callum Matthews
import re
LOGFILE = "sample_auth_small.log"  # change filename if needed

#Declaration and initialisation
ips=[]  #declare the empty list which I will append to fill with IP addresses to print
ipCounter = 0   #count unique IP address
lineCounter = 0 #count amount of lines read

def simple_parser(line):
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

#find uniqe IP'S
with open('sample_auth_small.log', 'r') as f:
    for line in f:
        lineCounter +=1 #increase counter for each line read
        ip_pattern = r"\d+\.\d+\.\d+\.\d+"
        found_ips = re.findall(ip_pattern,line)
        for ip in found_ips:    #for ever IP found in the log
            ips.append(ip)  #append them to ips list


unique_ips = set(ips)   #convert ips list to a set, which automatically removes duplicates
#unique_ips only contain distinct IP addresses

sorted_ipAddresses = sorted(unique_ips) #using sort function to sort my set of unique ips

#print("Unique IPs:")   # Print each unique IP and count how many there are
for ip in unique_ips:
    ipCounter +=1

ipCounter = len(unique_ips) #len is the function to return number of items in an object


##All print line outputs
print("The amount of unique IP's is: ",ipCounter)
print("Lines read:", lineCounter)
print("First 10 Unique IP's: ", sorted_ipAddresses[:10])    #print first 10 unique ip addresses by slicing to print the first 10 ips from list [:10]

##------Commented out as not used, old starter file----##
## This is the main block that will run first. 
## It will call any functions from above that we might need.
'''if __name__ == "__main__":

    with open(LOGFILE, "r") as f:
        for line in f:
            print (simple_parser(line.strip()))'''

    