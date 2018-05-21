word_list = ['cat','dog','rabbit']
letter_list = [ ]
for a_word in word_list:
    for a_letter in a_word:
        if a_letter in letter_list:
            continue
        else:
            letter_list.append(a_letter)
print(letter_list)