import os
from collections import Counter

os.chdir(r"C:\Users\musto\OneDrive\Documents")

file = open("log.txt", "r")

errors = []
warnings = 0

for line in file:
    if "ERROR" in line:
        errors.append(line.strip())
    elif "WARNING" in line:
        warnings += 1

file.close()

print("Toplam ERROR:", len(errors))
print("Toplam WARNING:", warnings)

error_counts = Counter(errors)

if error_counts:
    most_common = error_counts.most_common(1)[0]
    print("En sık hata:", most_common[0])
    print("Tekrar sayısı:", most_common[1])

if len(errors) > 3:
    print("Şüpheli aktivite tespit edildi!")