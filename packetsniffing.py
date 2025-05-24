from scapy.all import sniff

# Print a summary of 10 captured packets
sniff(prn=lambda x: x.show(), count=10) # x.summary()