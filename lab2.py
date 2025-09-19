import re
ips=[]  #declare the empty list which I will append to fill with IP addresses to print

#Printing the entire auth logs, commented out as i dont need this part in later parts, just need to remeber to print the outputs.
#with open('auth.log', 'r') as f:
#   for line in f:
#        print(line.strip())

#Extract and print the IP addresses only
with open('auth.log', 'r') as f:
    for line in f:
        ip_pattern = r"\d+\.\d+\.\d+\.\d+"
        found_ips = re.findall(ip_pattern,line)
        for ip in found_ips:
            ips.append(ip)
   # print(ips) If i didnt want unique addresses, i would keep this line and not have anything below

# However i do want unique ips, so i convert to a set to remove duplicates

unique_ips = set(ips)

# Print each unique IP
print("Unique IPs:")
for ip in unique_ips:
    print(ip)

#here I am saving the ips to a new file, and I am usuing a variable I called save.
with open('unique_ips.txt', 'w') as save:
    for ip in unique_ips:
        save.write(ip + "\n")