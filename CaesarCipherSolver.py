# A solution for the ANDman problem from IEEExtreme 2022 by Brendan Woo.
# Special thanks to my teammates, Hoyoun and Jiwon!

# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield(number)   

input_parser = parser()

def get_word():
    global input_parser
    return next(input_parser)

def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)

      
#Frequencies of all letters, from A(0) to B(25)
freq = [0.08, 0.015, 0.03, 0.04, 0.13, 0.02, 0.015, 0.06, 0.065, 0.005, 0.005, 0.035, 0.03, 0.07, 0.08, 0.02, 0.002, 0.065, 0.06, 0.09, 0.03, 0.01, 0.015, 0.005, 0.02, 0.002]

charMap = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9, 'k':10, 'l':11, 'm':12, 'n':13, 'o':14, 'p':15, 'q':16, 'r':17, 's':18, 't':19, 'u':20, 'v':21, 'w':22, 'x':23, 'y':24, 'z':25}
numMap = {0:'a', 1:'b', 2:'c', 3:'d', 4:'e', 5:'f', 6:'g', 7:'h', 8:'i', 9:'j', 10:'k', 11:'l', 12:'m', 13:'n', 14:'o', 15:'p', 16:'q', 17:'r', 18:'s', 19:'t', 20:'u', 21:'v', 22:'w', 23:'x', 24:'y', 25:'z'}


cipherText = input()

cipherFreq = {}
for i in range(26):
  cipherFreq[i] = 0

nChars = 0

for char in cipherText:
  #For all letters, track frequency
  if char.isalpha():
    if charMap[char.lower()] in cipherFreq:
      cipherFreq[charMap[char.lower()]] +=1
      nChars +=1


#Adjust cipherFreq to store probability by dividing frequency/nChars
for char in cipherFreq:
  cipherFreq[char] = cipherFreq[char]/nChars

#Calculate most probable outcome with a statistical attack
bestProb = 0
bestShift = 0
for shift in range(26):
  prob = 0

  #Calculate the total probability for each char if it is shifted by shift
  for char in range(26):
    prob += cipherFreq[char]*freq[(char+shift) % 26]
    
  #Find the shift with the highest probability
  if prob > bestProb:
    bestProb = prob
    bestShift = shift

#print(bestShift)

#Decrypt using most probable shift
plaintext = ""
for char in cipherText:
  if char.isupper():
    #Replace each char with its shifted counterpart
    char = numMap[ (charMap[char.lower()]+bestShift) % 26].upper()
  elif char.islower():
    char = numMap[ (charMap[char.lower()]+bestShift) % 26].lower()
  plaintext += char
print(plaintext)

#Sample ciphertext
#U iuxx nq mf ftq eqzmfq fapmk fa tqmd m bqfufuaz rday Fuxxuge. Omeeuge mzp Ndgfge tmhq nqqz mofuzs efdmzsq. Etagxp nq nmow uz fuyq rad