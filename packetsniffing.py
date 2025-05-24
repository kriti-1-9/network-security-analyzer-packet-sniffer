from scapy.all import sniff, IP
import csv

packets = sniff(count = 50)

with open("packets.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Source IP", "Destination IP", "Protocol", "Length"])
    
    for pkt in packets:
        if IP in pkt:
            writer.writerow([
                pkt[IP].src,
                pkt[IP].dst,
                pkt.proto,
                len(pkt)
            ])

# Print a summary of 10 captured packets
# sniff(prn=lambda x: x.show(), count=10) # x.summary()