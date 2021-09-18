import re
import csv


with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
title_contacts = contacts_list[:1]
contacts = contacts_list[1:]
pattern_phone = re.compile(r"(\+7|8)?\s*\(?(495)\)?[-\s]?(\d{3})-?(\d\d)"
                           r"-?(\d\d)(\s\(?(доб.)\)?\s(\d{4})\)?)?")
phonebook_dict = {}
for each in contacts:
    result = pattern_phone.sub(r"+7(\2)\3-\4-\5 \7\8", each[-2])
    each[-2] = result
    name_row = str(each[0]) + ' ' + str(each[1]) + ' ' + str(each[2])
    name_row = re.sub('\s+', ' ', name_row)
    name_row = name_row.split()
    new_key = name_row[0] + ' ' + name_row[1]
    if new_key not in phonebook_dict.keys():
        phonebook_dict[new_key] = name_row + each[3:]
    for number, item in enumerate(phonebook_dict[new_key]):
        if item == '':
            item = each[number]
improved_contacts = title_contacts + list(phonebook_dict.values())
with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=",")
    datawriter.writerows(improved_contacts)