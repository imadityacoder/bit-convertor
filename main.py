# bit convetor - it convert a binary to decimal and a decimal to binary

#Bit convertor made by Aditya

#loop which repeat the program
while True:
    #this will handle the error
    try:

        inp =input("\n\nEnter '1' for convert binary to decimal or '0' for decimal to binary | 'e' for exit\n:")

        number = str(input(f"\nenter value here: \n"))

        def bin_to_dec(binary):
            decimal = 0
            exponent = 0

            for n in binary[::-1]: 

                if n == '1' or n == '0':
                    n = int(n)
                    num = (2**exponent)*n
                    decimal = decimal + num

                else:
                    print("enter a valid binary digits!!!")

                exponent = exponent + 1

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
                    print("Enter a valid decimal!!!")
                        
                decimal = int(decimal)//2

            print(f'\n{number} in binary is {binary[::-1]}\n')    
        
        if inp == "1": bin_to_dec(number)

        elif inp == "0": dec_to_bin(number)

        elif inp == "e" or number == "e": break

        else:print("Please choose '1' or '0' !!!")

    except Exception as e:
        print(e)    
