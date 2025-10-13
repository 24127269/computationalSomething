#Exercise 3.1:
with open("output.txt","w") as file:
    file.write("I'm a student.\n")

#Exercise 3.2:
number = 1 / 7
ket_qua = f"Giá trị của 1/7 là: {number:.5f}"

with open("output.txt", "a", encoding="utf-8") as file:
    file.write(f"{ket_qua}\n")

#Exercise 3.3:
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

sum = a + b

with open("output.txt", "a") as file:
    file.write(f"The sum is: {sum}\n")

#Exercise 3.4:
file_name = input("Nhập tên file: ")
try:
    with open (file_name, 'r', encoding = 'utf-8') as f:
        content = f.read()
        with open("output.txt", "a", encoding = 'utf-8') as file:
            file.write("------ Nội dung file ------\n")
            file.write(content)
            file.write("\n----------------------------\n")
except FileNotFoundError:
    with open("output.txt", "a", encoding = 'utf-8') as file:
        file.write(f"Lỗi: Không tìm thấy file '{file_name}'")
