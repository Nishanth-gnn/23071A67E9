def most_common_word(text):
    words = text.split()
    counts = {}
    
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    max_count = 0
    most_common = ""
    
    for word, count in counts.items():
        if count > max_count:
            max_count = count
            most_common = word
            
    return most_common

text = input("Enter text: ")
print(most_common_word(text))

