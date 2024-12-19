import re
from collections import Counter

# Log faylının yolu
log_file_path = 'server_logs.txt'

# Faylı oxumaq
with open(log_file_path, 'r') as log_file:
    log_content = log_file.readlines()

# Regex şablonu
pattern = r'(?P<ip>\d+\.\d+\.\d+\.\d+) .* \[(?P<date>.*?)\] "(?P<method>[A-Z]+)'

# Uğursuz giriş cəhdlərinin IP ünvanlarını tapmaq (HTTP statusu 401)
unsuccessful_attempts = [match.group('ip') for line in log_content 
                         if (match := re.search(pattern, line)) and '401' in line]

# Hər bir IP ünvanının cəhd sayını hesablamaq
ip_counts = Counter(unsuccessful_attempts)

# 5-dən çox uğursuz cəhd edən IP-ləri süzmək
frequent_offenders = {ip: count for ip, count in ip_counts.items() if count > 5}

# Nəticələri yeni mətn faylına yazmaq
output_path = 'frequent_offenders.txt'
with open(output_path, 'w') as text_file:
    for ip, count in frequent_offenders.items():
        text_file.write(f"IP: {ip}, Uğursuz giriş cəhdləri: {count}\n")

print(f"Nəticələr '{output_path}' faylında saxlanıldı.")
