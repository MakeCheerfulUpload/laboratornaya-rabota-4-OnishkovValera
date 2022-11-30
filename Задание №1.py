import time

f = open("Исходник.txt", encoding='utf-8')
d = f


def file_to_xml(file):
    xml_file_start = ""
    xml_file_end = ""
    xml_file = ''
    timetablename = file.readline()[:-2]
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

    for i in range(len(ms1) - 1):
        if 'lesson' in ms1[i][0]:
            xml_file += xml_file_start + xml_file_end
            xml_file_start = ' '
            xml_file_end = ' '
            xml_file_start += f"<{ms1[i][0].strip()}>\n"
            xml_file_end = f" </{ms1[i][0].strip()}>\n" + xml_file_end
        else:
            xml_file_start += f"   <{ms1[i][0]}>{ms1[i][1].strip()}</{ms1[i][0]}>\n"
    xml_file = f"<{timetablename}>\n" + f" <{day[0]}>{day[1].strip()}</{day[0]}>\n" + xml_file + xml_file_start + xml_file_end + f"</{timetablename}>\n"

    return xml_file

print(file_to_xml(f))
start_time = time.time()
for n in range(100):
    f = open("Исходник.txt", encoding='utf-8')
    file_to_xml(f)
print("--- %s seconds ---" % (time.time() - start_time))
