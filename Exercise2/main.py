def bigger_is_greater(word: str) -> str:
    w = list(word)
    largestK = len(w)-2
    largestI = len(w)-1

    while largestK >= 0 and w[largestK] >= w[largestK+1]:
        largestK -= 1

    if largestK < 0:
        return "no answer"

    while w[largestI] <= w[largestK]:
        largestI -= 1

    w[largestK], w[largestI] = w[largestI], w[largestK]
    w[largestK+1:] = w[len(w)-1:largestK:-1]

    return ''.join(w)

        
def main():
    f = open("input", "r")
    lines = f.readlines()

    for line in lines[1:]:
        line = line.replace("\n", "")
        print(bigger_is_greater(line))  

if __name__ == "__main__":
    main()
