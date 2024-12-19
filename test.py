import re

# Log faylının yolu
log_file_path = 'server_logs.txt'

# Faylı oxumaq
with open(log_file_path, 'r') as log_file:
    log_content = log_file.readlines()

# Regex şablonu
pattern = r'(?P<ip>\d+\.\d+\.\d+\.\d+) .* \[(?P<date>.*?)\] "(?P<method>[A-Z]+)'

# Verilənləri çıxarmaq
extracted_data = []
for line in log_content:
    match = re.search(pattern, line)
    if match:
        ip = match.group('ip')
        date = match.group('date')
        method = match.group('method')
        extracted_data.append((ip, date, method))

# Çıxarılmış məlumatları göstərmək
for data in extracted_data:
    print(f"IP: {data[0]}, Tarix: {data[1]}, HTTP Metodu: {data[2]}")
