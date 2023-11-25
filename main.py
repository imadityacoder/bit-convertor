

while True:

    inp =input("\n\nenter '1' for binary to decimalor '0' for decimal to binary and 'e' for exit\n\n:")

    number = input(f"\nenter value here: \n")


    def bin_to_dec(binary):

        binary = int(binary)
        dec_arry = {}
        pass


    def dec_to_bin(decimal):
        decimal = int(decimal)

        binary = str('')

        while decimal > 0:
            on = "1"
            off = "0"

            if (decimal%2) == 0:
                binary = binary + off

            elif (decimal%2) == 1:
                binary = binary + on   

            else:
                print("error")
                    
            decimal = int(decimal)//2

        print(f'\n{number} in binary is {binary[::-1]}\n')    
    

    if inp == "1": bin_to_dec(number)

    elif inp == "0": dec_to_bin(number)

    elif (inp and number) == "e": break

    else:print("choose '1' or '0' .")
