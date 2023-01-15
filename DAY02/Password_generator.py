import random
len_1=int(input("How many letters would you like in your Password?"))
len_2=int(input("How many numbers would you like in your password?"))
len_3=int(input("How many special characters would you like in your password?"))
letters_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
                'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols_list = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def randPassGen():
    Password_list = []
    for i in range(1,len_1+1):
        Password_list.append(random.choice(letters_list))

    for i in range(1,len_2+1):
        Password_list.append(random.choice(numbers_list))

    for i in range(1,len_3+1):
        Password_list.append(random.choice(symbols_list))

    random.shuffle(Password_list)
    password_final = ""
    for i in Password_list:
        password_final += i
    return password_final

print(f"Your Password is : {randPassGen()}")
