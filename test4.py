import re
import csv
from collections import Counter

# Log faylının yolu
log_file_path = 'server_logs.txt'

# Faylı oxumaq
with open(log_file_path, 'r') as log_file:
    log_content = log_file.readlines()

# Regex şablonu
pattern = r'(?P<ip>\d+\.\d+\.\d+\.\d+) .* \[(?P<date>.*?)\] "(?P<method>[A-Z]+)'

# Məlumatların çıxarılması
data = []
for line in log_content:
    match = re.search(pattern, line)
    if match:
        ip = match.group('ip')
        date = match.group('date')
        method = match.group('method')
        status = '401' in line  # Uğursuz giriş olub-olmaması
        data.append((ip, date, method, status))

# Uğursuz giriş cəhdlərini hesablamaq
ip_counts = Counter(ip for ip, _, _, status in data if status)

# Unikal IP-lərin məlumatlarını toplamaq
results = []
for ip, count in ip_counts.items():
    # İlk tarixi və HTTP metodunu tapmaq
    for ip_data in data:
        if ip_data[0] == ip:
            results.append({'IP ünvanı': ip, 'Tarix': ip_data[1], 'HTTP metodu': ip_data[2], 'Uğursuz cəhdlər': count})
            break

# CSV faylına yazmaq
output_path = 'frequent_offenders.csv'
with open(output_path, 'w', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=['IP ünvanı', 'Tarix', 'HTTP metodu', 'Uğursuz cəhdlər'])
    writer.writeheader()
    writer.writerows(results)

print(f"Nəticələr '{output_path}' faylında saxlanıldı.")
