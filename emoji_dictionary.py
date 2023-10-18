emoji = {':)': '😄',
         ":(":'😒',
         ":))":"🤣"       
         }


emoji_list = []
for i in range(0,3):
    message = input("Enter your input: ")
    words = message.split(' ')
    print(words)
    for word in words:
        a = emoji.get(word,word)
        print(word, end=" ")
    print()





