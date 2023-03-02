import re
import csv
import sys

def extract_mail_data(log_file, csv_file):
  with open(log_file, 'r') as file:
    log_lines = file.readlines()
  
  with open(csv_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Date', 'Taille', 'Nombre de destinataires'])
    for line in log_lines:
      match = re.search(r'(\w{3} \d{1,2} \d{2}:\d{2}:\d{2}).*size=(\d+),.*nrcpts=(\d+),', line)
      if match:
        date, size, nrcpts = match.groups()
        writer.writerow([date, size, nrcpts])

if __name__ == "__main__":
  if len(sys.argv) != 3:
    print("Usage: python script.py log_file csv_file")
    sys.exit(1)
  extract_mail_data(sys.argv[1], sys.argv[2])
