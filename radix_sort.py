option = int(input("Введите 1 для ввода из консоли / введите 2 для ввода из файла\n"))
if option == 1:
    n = int(input("Введите кол-во элементов: "))
    array = []
    for i in range(n):
        array.append(input(f"Введите элемент {i + 1}: "))
else:
    path = input("Укажите путь к файлу: ")
    with open(path, "r") as file:
        array = [line.strip() for line in file if line.strip()]
        n = int(array[0])
        array = array[1:]

print("Initial array:")
print(", ".join(array))
print("*" * 10)

l = len(array[0])
for i in range(l - 1, -1, -1):
    bucket_0 = []
    bucket_1 = []
    bucket_2 = []
    bucket_3 = []
    bucket_4 = []
    bucket_5 = []
    bucket_6 = []
    bucket_7 = []
    bucket_8 = []
    bucket_9 = []
    for j in range(n):
        if array[j][i] == "0":
            bucket_0.append(array[j])
        elif array[j][i] == "1":
            bucket_1.append(array[j])
        elif array[j][i] == "2":
            bucket_2.append(array[j])
        elif array[j][i] == "3":
            bucket_3.append(array[j])
        elif array[j][i] == "4":
            bucket_4.append(array[j])
        elif array[j][i] == "5":
            bucket_5.append(array[j])
        elif array[j][i] == "6":
            bucket_6.append(array[j])
        elif array[j][i] == "7":
            bucket_7.append(array[j])
        elif array[j][i] == "8":
            bucket_8.append(array[j])
        elif array[j][i] == "9":
            bucket_9.append(array[j])
    bucket_list = [bucket_0, bucket_1, bucket_2, bucket_3, bucket_4, bucket_5, bucket_6, bucket_7, bucket_8, bucket_9]
    print(f"Phase {l - i}")
    main_counter = 0
    for number, bucket in enumerate(bucket_list):
        if len(bucket) == 0:
            print(f"Bucket {number}: empty")
        else:
            print(f"Bucket {number}: {', '.join(bucket)}")
        while len(bucket) != 0:
            array[main_counter] = bucket.pop(0)
            main_counter += 1
    print("*" * 10)
    bucket_list.clear()

print("Sorted array:")
print(", ".join(array))
