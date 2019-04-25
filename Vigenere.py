
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    myMessage = open("tekst.txt", "r").read()
    myMode = 'encrypt'
    myKey = input("Enter your key")


    translated = encryptMessage(myKey, myMessage)

   # print('%sed message:' % (myMode.title()))
    print(translated)
    print()
    f=open("txt.txt","w")
    f.write(translated)
    f.close()


def encryptMessage(key, message):
    return translateMessage(key, message, 'encrypt')



def translateMessage(key, message, mode):
    translated = [] # array for encrypted string

    keyIndex = 0
    key = key.upper()

    for symbol in message:  # for every character in message
        num = LETTERS.find(symbol.upper()) #find returns the index
        if num != -1:  # -1 means symbol.upper() was not found in LETTERS
            if mode == 'encrypt':
                num += LETTERS.find(key[keyIndex])  # add next index value

            num %= len(LETTERS)  # modulo 26 because of alphabet

            # add the encrypted symbol to the end of translated.
            if symbol.isupper():
                translated.append(LETTERS[num])
            elif symbol.islower():
                translated.append(LETTERS[num].lower())

            keyIndex += 1  # move to the next letter in the key
            if keyIndex == len(key):
                keyIndex = 0


    return ''.join(translated) #returning encrypted string

main()


def index_coincidence(s):
    index_coincidence = 0
    N = len(s)
    n = []
    for x in range(0, 26): # 26 amount of letters in alphabet
        summ = 0
        for k in range(0, N):
            if (x == (ord(s[k]) - 97)): #ord makes chars into ints
                summ += 1
        n.append(summ) #fill array with ints

    for x in range(0, 26):
        index_coincidence += (n[x] * (n[x] - 1))
    index_coincidence = index_coincidence / (N * (N - 1)) #pattern for coincidence from pdf
    print("Index is equal to:")
    print(index_coincidence)
    print()

#we do the same thing as in index_coincidence but for 2 columns not single


def mutual_index_coincidence(s1, s2): #s1 -strings in 1 column
    index_coincidence = 0
    H1 = len(s1) #amount of strings
    H2 = len(s2)
    h1 = [] #arrays for index coincidence
    h2 = []
    for x in range(0, 26): # 26 - len of letters
        summ1 = 0
        summ2 = 0
        for k in range(0, H1):
            if (x == (ord(s1[k]) - 97)):
                summ1 += 1

        for k in range(0, H2):
            if (x == (ord(s2[k]) - 97)):
                summ2 += 1

        h1.append(summ1)
        h2.append(summ2)

    for x in range(0, 26):
        index_coincidence += (h1[x] * h2[x])
    index_coincidence = index_coincidence / (H1 * H2) #pattern for coincidence from pdf
    print(index_coincidence)

f1=open("txt.txt", "r").read()

def coincidencecolumns(f1):
    columns = int(input("Enter the amount of columns"))
    columns_strings = [] #array of chars in each column
    for x in range(0, columns):
        s = '' #single char we add to column
        for k in range(0, int(len(f1) / columns)):
            s += f1[k * columns + (x % columns)]
        print('for column', (x + 1), ':', s[::], "\n")
        index_coincidence(s)
        columns_strings.append(s)


    for x in range(0, columns - 1):
       for k in range(x + 1, columns):
           print('mutual index of coincidence between columns : ', (x + 1), 'and', (k + 1))
           mutual_index_coincidence(columns_strings[x], columns_strings[k])
print(coincidencecolumns(f1))
