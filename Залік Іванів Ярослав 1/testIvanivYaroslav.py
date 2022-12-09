def readline():
    with open ("text.txt", "r") as f:
        a=f.readlines()
    return a
text=readline()
symbols=0
words=0
print("Ми будемо працювати з наступним текстом: ")
for i in text:
    print(i)

w=int(input("Введіть номер рядка який бажаєте зчитати"))
    
for j in text[w-1]:
    symbols=symbols+1
g=i.split(' ')
for b in range(len(g)):
    words=b
print('Кількість слів у рядку',w ,'-', words, '. Кількість символів у тексті - ', symbols)
        
