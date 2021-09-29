s = 'Thought I found a way Thought I found a way, yeah found But you never go away never (go away)'
s = s.replace(',', '').replace('(', '').replace(')', '').replace('!', '')
s = s.split(' ')
d = {}
count = 1
for new_s in s:
    if new_s not in d:
        d[new_s] = [count]
    else:
        d[new_s].append(count)
k = {}
for key, q in d.items():
    s = 0
    for kol in q:
        s += 1
    k[key] = [s]
print(k)