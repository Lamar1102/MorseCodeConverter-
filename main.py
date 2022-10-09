from morsecode import code

def morse_code_converter():

    user_input = input("Please enter text you would like to be translated to Morse Code! \n")
    user_input_upper = user_input.upper()
    morse_code = ""

    for letter in user_input_upper:
        if letter != " " and letter.isalnum()==False:
            print("Please enter letters or digits only!")
            morse_code_converter()
        else:
            morse_code += code[letter]

    print(f"{user_input} in Morse Code is {morse_code}")

morse_code_converter()


