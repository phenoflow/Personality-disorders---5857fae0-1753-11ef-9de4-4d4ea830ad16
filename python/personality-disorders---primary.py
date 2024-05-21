# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"E212100","system":"readv2"},{"code":"E216.13","system":"readv2"},{"code":"Eu60713","system":"readv2"},{"code":"Eu60800","system":"readv2"},{"code":"Eu60y12","system":"readv2"},{"code":"Eu60z12","system":"readv2"},{"code":"E21y600","system":"readv2"},{"code":"E21z.00","system":"readv2"},{"code":"Eu60714","system":"readv2"},{"code":"Eu60213","system":"readv2"},{"code":"Eu60013","system":"readv2"},{"code":"E214.11","system":"readv2"},{"code":"E21yz11","system":"readv2"},{"code":"E212200","system":"readv2"},{"code":"Eu60200","system":"readv2"},{"code":"Eu60z11","system":"readv2"},{"code":"E213.12","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('personality-disorders-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["personality-disorders---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["personality-disorders---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["personality-disorders---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
