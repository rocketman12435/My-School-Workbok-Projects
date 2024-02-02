import sys

nameandclass = input("Enter your name, then your class (please don't separate with a comma) : ")

room =""

if "9T" in nameandclass:

    room = "16"

    fname = nameandclass.split()

    print("Hello",fname[0].capitalize(),",please go to Room",room)


elif "9V" in nameandclass:

    room = "18"

    fname = nameandclass.split()

    print("Hello",fname[0].capitalize(),",please go to Room",room)



elif "9W" in nameandclass:

    room = "20"

    fname = nameandclass.split()

    print("Hello",fname[0].capitalize(),",please go to Room",room)



elif "9X" in nameandclass:

    room = "22"

    fname = nameandclass.split()

    print("Hello",fname[0].capitalize(),",please go to Room",room)



elif "9Z" in nameandclass:

    room = "24 "

    fname = nameandclass.split()

    print("Hello",fname[0].capitalize(),",please go to Room",room)



else:
    print("Invalid input.")
