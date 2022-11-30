f = open("Исходник.txt", encoding='utf-8')
import time


def file_to_massive(file):
    TSV_file = [['day', 'lesson']]
    day = file.readline()[:-1].strip()
    day = day.split(':')
    txt = file.read()
    ms1 = txt.split('\n')

    for i in range(len(ms1) - 1):
        ms1[i] = ms1[i].strip()

    for i in range(len(ms1) - 1):
        if ms1[i] == '':
            ms1.remove('')
        ms1[i] = ms1[i].replace(':', '/', 1)
        ms1[i] = ms1[i].split('/')
    dct_number = {
        'day': 0,
        'lesson': 1
    }
    lessonnumber = 0
    for i in ms1:
        if 'lesson' in i[0]:
            lessonnumber = int(i[0][-1])
            TSV_file.append([day[1]])
            TSV_file[lessonnumber].append(lessonnumber)
            dct_number['lesson'] = int(i[0][-1])
        else:
            if i[0] in TSV_file[0]:
                TSV_file[lessonnumber].append(i[1])
            else:
                dct_number[i[0]] = len(TSV_file[0])
                TSV_file[0].append(i[0])
                TSV_file[lessonnumber].append(i[1])
    return TSV_file


massive = file_to_massive(f)
for i in massive:
    for j in i:
        print(j, end='\t')
    print('\n')


