# fix_encoding.py

# Open and re-save the file with UTF-8 encoding
with open("data.json", "rb") as f:
    content = f.read()

# Try decoding with utf-16 (you can change this to latin1 or utf-8-sig if needed)
decoded = content.decode("utf-16")

# Write content to a new UTF-8 encoded file
with open("data_fixed.json", "w", encoding="utf-8") as f:
    f.write(decoded)