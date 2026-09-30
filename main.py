from datetime import datetime
print("            DESI CHHORA     ")
print()
print()
print("       Ram Ram, Bhai!    ")
print()
print()
print("    Main Desi Chhora su.")
print()
print("  Python mein bana tera desi")
print("        AI assistant.")
print()
print()
print("       Chaal, shuru karein!")

while True:

    print()
    print("1. Baat-Cheet  ")
    print("2. Calculator ")
    print("3. Prime Number Check ")
    print("4. Maximum / Minimum ")
    print("5. Quiz ")
    print("6. Date & Time ")
    print("7. Help ")
    print("8. Bahar Niklo")

    choice = input("      Bata Bhai, ke karna se? ")

    if choice == "1":
        print()
        print("Baat-Cheet shuru karte hain! ")
        print()
        print("Desi Chhora ki Ram Ram bhai! Ke haal se? ")

        while True:
            user_message = input("You: ")

            if "bye" in user_message.lower():
                print("Desi Chhora: Theek se bhai! ")
                break

            elif "hi" in user_message.lower() or "hello" in user_message.lower():
                print("Desi Chhora: Ram Ram bhai! ")

            elif "how are you?" in user_message.lower():
                print("Desi Chhora: Main badhiya su bhai! ")

            elif "your name" in user_message.lower():
                print("Desi Chhora: Mera naam Desi Chhora hai! ")

            elif "thank you" in user_message.lower() or "thanks" in user_message.lower():
                print("Desi Chhora: Koi baat nahi bhai! ")

            else:
                print("Desi Chhora: Bhai, ye baat samajh na aayi. ")



    elif choice == "2":
        print()
        print("Calculator kholte hain ")
        try:
            num1 = float(input("Pehla number daal bhai: "))
            num2 = float(input("Doosra number daal bhai: "))
        except ValueError:
            print("Bhai, sirf number daal! ")
            continue

        operation = input("Konsa operation karna se (+,-,*,/): ")

        if operation == "+":
            result = num1 + num2
            print("Result:", result)

        elif operation == "-":
            result = num1 - num2
            print("Result:", result)

        elif operation == "*":
            result = num1 * num2
            print("Result:", result)

        elif operation == "/":
            if num2 == 0:
                print("Bhai, 0 te divide koni kar sakde! ")
            else:
                result = num1 / num2
                print("Result:", result)

        else:
            print("Bhai, ye operation valid koni se. Sirf +, -, *, / use kar! ")


    elif choice == "3":
        print()
        print("Prime Number check karein! ")

        num = int(input("Bhai, number daal: "))

        if num < 2:
            print("ye Prime Number nhi h.")
        else:
            is_prime = True

            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break

            if is_prime:
                print("ye Prime Number hai ")
            else:
                print("Ye prime number nahi hai. ")

    elif choice == "4":
        print()
        print("Maximum aur Minimum check karein! ")

        numbers = list(map(int ,input("Bhai, numbers daal (space se):").split()))

        maximum = numbers[0]
        minimum = numbers[0]

        for num in numbers:
            if num > maximum:
                maximum = num

            if num < minimum:
                minimum = num

            print("Maximum Number :",maximum)
            print("Minimum Number :",minimum)


    elif choice == "5":
        print()
        print("Quiz shuru karein! ")
 
        score = 0
 
        answer = input("Q1. India ka capital kya hai? ")
 
        if answer.lower() == "delhi":
            print("Sahi jawab! ")
            score = score + 1
        else:
            print("Galat jawab! ")
 
        answer = input("Q2. Python kis type ki language hai? ")
 
        if "programming" in answer.lower():
            print("Sahi jawab! ")
            score = score + 1
        else:
            print("Galat jawab! ")
 
        answer = input("Q3. 5 + 5 kitna hota hai? ")
 
        if answer == "10":
            print("Sahi jawab! ")
            score = score + 1
        else:
            print("Galat jawab! ")
 
        print()
        print("Tumhara score:", score, "/ 3")


    elif choice == "6":
        print()
        print("Date aur Time dekhein! ")

        current_time = datetime.now()

        print("Aaj ki date:", current_time.strftime("%d-%m-%Y"))
        print("Abhi ka time:", current_time.strftime("%I:%M:%S %p"))

    elif choice == "7":
        print()
        print("Madad chahiye? Yahan dekhein! ")

        print()
        print("Desi Chhora ye kaam kar sakta hai:")
        print()
        print("1. Baat-Cheet ")
        print("2. Calculator ")
        print("3. Prime Number Check ")
        print("4. Maximum / Minimum ")
        print("5. Quiz ")
        print("6. Date & Time ")
        print()
        print("Koi bhi option choose karke use kar bhai! ")

    elif choice == "8":
        print()
        print("Desi Chhora se milte hain phir! ")
        break

    else:
        print("Bhai, ye option menu mein nahi se. Dobara try kar! ")
   