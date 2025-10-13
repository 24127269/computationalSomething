file_name = input("Nhập tên file: ")
try:
    with open (file_name, 'r', encoding = 'utf-8') as f:
        content = f.read()
        print("\n------ Nội dung file ------")
        print(content)
        print("----------------------------")
except FileNotFoundError:
    print(f"\nLỗi: Không tìm thấy file '{file_name}'")