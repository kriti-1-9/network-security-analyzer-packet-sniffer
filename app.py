from flask import Flask, render_template
import csv
from collections import Counter

app = Flask(__name__)

@app.route('/')
def index():
    protocols = []
    src_ips = []

    # Read packets.csv
    with open('packets.csv', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            protocols.append(row['Protocol'])
            src_ips.append(row['Source IP'])

    # Count protocols and IPs
    protocol_counts = Counter(protocols)
    ip_counts = Counter(src_ips).most_common(5)  # Top 5 IPs

    labels = list(protocol_counts.keys())
    values = list(protocol_counts.values())

    return render_template('index.html', labels=labels, values=values, top_ips=ip_counts)

if __name__ == '__main__':
    app.run(debug=True)