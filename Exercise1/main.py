def main():
    f = open("input", "r")
    lines = f.readlines()
    dictionary = {}

    for line in lines[1:]:
        line = line.replace("\n", "")
        
        if line in dictionary:
            dictionary[line] += 1
        else:
            dictionary[line] = 1

    output: str = ""
    for word in dictionary:
        output += f"{dictionary[word]} "

    print(f"{len(dictionary)}\n{output}")

if __name__ == "__main__":
    main()
