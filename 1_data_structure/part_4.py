
num_list = [1, 2, 3 ,4 ,5]

print(num_list[0]) # первый элемент списка
print(num_list[2]) # третий элемент списка
print(num_list[:3]) # список из первых трех элементов


words_list = ["Ростов", "+", "на", "-", "Дону"]
words_list[1] = '-'

for element in words_list:
    print(element, end="")
  
# print(''.join(words_list))
    
num_word_list = ["a", "s", "1", "a", "32", "23"]

words_list = [word for word in num_word_list if word.isalpha()]
nums_list = [word for word in num_word_list if word.isdigit()]
print(words_list, nums_list)

words_list.pop()
words_list.reverse()
print(words_list)

num_word_set = set(num_word_list)
print(num_word_set)