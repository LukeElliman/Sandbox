try:
    in_file = open("on_off.txt", 'r')
    line = in_file.readline()
    in_file.close()

    out_file = open("on_off.txt", 'w')
    if line == "on":
        line = "off"
    else:
        line = "on"
    print(line, file=out_file)
    out_file.close()
except FileNotFoundError:
    print("Error with file. Aborting!")



