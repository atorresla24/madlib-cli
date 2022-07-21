def read_template(path):
    file = open(path, "r")
    read = file.read()
    file.close()
    return read.strip()


def parse_template(words):
    string = ""
    lis = []
    capture = False
    captured_word = ""
    for x in words:
        if capture:
            if x == "}":
                capture = False
                lis.append(captured_word)
                captured_word = ""
                string += x
            else:
                captured_word += x
        else:
            string += x
            if x == "{":
                capture = True
    return string, tuple(lis)


def merge(str, tup):
    return str.format(*tup)


print("""
Welcome to my Madlib game! 
Enter information and you will receive a surprise!
""")

if __name__ == '__main__':
    filepath = "assets/dark_and_stormy_night_template.txt"

    final, desc = parse_template(read_template(filepath))

    responses = []
    for x in desc:
        if x.lower() == "adjective":
            print(f"Enter an {x}")
            response = input("> ")
            responses.append(response)
        else:
            print(f"Enter a {x}")
            response = input("> ")
            responses.append(response)

    print(merge(final, tuple(responses)))
