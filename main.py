print("\n\nThis python script is to change an existing string in tht whole document\n")

print("Put the file into main.py folder, is it done? y/n")
choice = str(input())

if choice == "y":
    print("please enter the file name with txt extension (\".txt\"): ")
    filename = input()
    while 1:
        with open(filename, 'r') as file:
            filedata = file.read()

        print(filedata)
        print('\nWhich string do you want to change ?')
        string = input()
        print('Change by?')
        change = input()
        filedata = filedata.replace(string, change)

        with open(filename, 'w') as file:
            file.write(filedata)

        print('Here is your new file:\n')
        print(filedata)
        print("\nDo you need another change? y/n")
        choice2 = str(input())

        if choice2 == "n":
            print("Thanks for using my program :)")
            break

else:
    print("Do it and restart the script")