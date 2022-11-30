import dict2xml
import time
f = open("Исходник.txt", encoding='utf-8')

def file_to_dict(file):
    dct = {}
    timetablename = file.readline()[:-2]
    day = file.readline()[:-1].strip()
    day = day.split(':')
    txt = file.read()
    array = txt.split('\n')
    dct[timetablename] = {}
    dct[timetablename][day[0]] = day[1]
    for i in range(len(array) - 1):
        array[i] = array[i].strip()

    for i in range(len(array) - 1):
        if array[i] == '':
            array.remove('')
        array[i] = array[i].replace(':', '/', 1)
        array[i] = array[i].split('/')


    lesson_number = ''
    for i in range(len(array) - 1):
        if 'lesson' in array[i][0]:
            lesson_number = array[i][0]
            dct[timetablename][array[i][0]] = {}
        else:
            dct[timetablename][lesson_number][array[i][0]] = array[i][1]
    return dct

print(dict2xml.dict2xml(file_to_dict(f)))
start_time = time.time()
for n in range(1000):
    f = open("Исходник.txt", encoding='utf-8')
    file_to_dict(f)
print("--- %s seconds ---" %(time.time() - start_time))