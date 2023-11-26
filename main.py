# bit convetor - it convert a binary to decimal and a decimal to binary

#Bit convertor made by Aditya

while True:

    inp =input("\n\nEnter '1' for convert binary to decimal or '0' for decimal to binary | 'e' for exit\n:")

    number = input(f"\nenter value here: \n")

    def bin_to_dec(binary):

        decimal = int()
            
        for n in binary[::-1]:
            n = int(n)

            if n == (0 or 1):
                exponent = 0
                num = n*2^exponent
                exponent += 1
                decimal += num

            else:
                print("enter a valid binary digits!!!")    

        print(decimal)    

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

    else:print("Please choose '1' or '0' !!!")
