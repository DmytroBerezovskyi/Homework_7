str = 'Thought I found a way Thought I found a  way, yeah found But you never go away never (go away)'
str = str.replace(',', '').replace('(', '').replace(')', '').replace('!', '')
str = str.split(' ')
d = {}
for new_str in str:
    if new_str in d:
        d[new_str] = d[new_str] + 1
    else:
        d[new_str] = 1
r = {}
lst = []
for key, word in d.items():
    r[word] = [key]
    lst.append(word)
i = max(lst)
print('Количество раз встречающегося слова: ', i)
print('Слово, которое в этом тексте встречается чаще всего: ', r[i])
