d = {
   'apple': ['malum', 'pomum', 'popula'],

   'fruit': ['baca', 'bacca', 'popum'],

   'punishment': ['malum', 'multa']
}
new_d = {}
for key, words in d.items():
   for new_words in words:
      if new_words not in new_d:
         new_d[new_words] = [key]
      else:
         new_d[new_words].append(key)
print(new_d)