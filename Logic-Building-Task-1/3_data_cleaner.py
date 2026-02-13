# Simple Data Cleaner
# Real-World Application: Data preprocessing before analysis

names = [" Alice ", "bob", " CHARLIE "]

cleaned_names = []

for name in names:
    cleaned_name = name.strip().lower()
    cleaned_names.append(cleaned_name)

print("Cleaned Names:", cleaned_names)
