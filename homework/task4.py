with open('Engl.txt', 'w') as f:
    f.write('one - 1\n')
    f.write('two - 2\n')
    f.write('three - 3\n')
    f.write('four - 4\n')
""""Попытался через словари решить, но не вышло"""
#num_dikt = {}
#rus_dikt = {'one': 'один', 'two': 'два', 'three': 'три',
#            'four': 'четыре'}
#with open('Engl.txt') as f:
#    for line in f:
#        key, value = line.split('-')
#        num_dikt[key] = value

#for i in num_dikt:
#    if i in rus_dikt:
#        num_dikt[rus_dikt[i]] = num_dikt.pop(i)


""""Сделал так не маштабируемо"""

with open('Engl.txt') as f:
    with open('rus.txt', 'w', encoding='UTF-8') as rus_f:
        for line in f:
            if line == 'one - 1\n':
                rus_line = line.replace('one', 'один')
                rus_f.write(rus_line)
            elif line == 'two - 2\n':
                rus_line = line.replace('two', 'два')
                rus_f.write(rus_line)
            elif line == 'three - 3\n':
                rus_line = line.replace('three', 'три')
                rus_f.write(rus_line)
            elif line == 'four - 4\n':
                rus_line = line.replace('four', 'четыре')
                rus_f.write(rus_line)
