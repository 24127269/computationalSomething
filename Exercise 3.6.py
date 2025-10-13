s = "Hôm nay trời đẹp."
encoded = s.encode('utf-8')

with open("3.6-output.bin", "wb") as f:
    f.write(encoded)  