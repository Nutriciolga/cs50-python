# inputting the file name, deleting whitespaces
i = input("File name: ").strip()
# finding the index of the last point symbol
p = i.rfind(".")
# if the point symbol exists, do the next:
if p != -1:
    new_character = " "
    # making the list from the string
    temp = list(i)
    # replacing the cheracter with the index p into the space
    temp[p] = new_character
    # making the string again with the space
    i = "".join(temp)
    # splitting the line
    c, a = i.split()
    # comparing the part after point with cases and printing answers
    if not a:
        exit("wrong file name")
    match a:
        case "gif":
            print("image/gif")
        case "jpg" | "jpeg":
            print("image/jpeg")
        case "png":
            print("image/png")
        case "pdf" | "PDF":
            print("application/pdf")
        case "txt":
            print("text/plain")
        case "zip":
            print("application/zip")
        case _:
            print("application/octet-stream")
else:
    print("application/octet-stream")