is_hot = input("Is the weather hot today (y/n)? ")
have_lecture = input("Do you have a lecture today (y/n)? ")

if is_hot=="y" and have_lecture=="y":
    print("Go to TAFE and be v sad")
if is_hot=="y" and have_lecture=="n":
    print("Go to beach")
if is_hot=="n" and have_lecture=="n":
    print("sleep")
if is_hot=="n" and have_lecture=="y":
    print("Go to TAFE and be content")
