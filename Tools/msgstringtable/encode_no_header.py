import csv
import base64

with open('msgstringtable_no_header.csv', 'w', newline='') as outfile, open('msgstringtable_no_header.txt', newline='') as decoded:
    rdr = csv.reader(decoded, delimiter=',')
    for row in rdr:
        msg = base64.b64encode(row[0].encode('utf-8')).decode('utf-8')
        print(f"{msg}")
        outfile.write(f"{msg}\n")