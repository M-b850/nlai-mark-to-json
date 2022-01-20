import re
import json
from json import encoder

books = []


def write_json(new_data, filename='main.json'):
    with open(filename, 'r+') as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data["books"].append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent=4)


with open("sample.mrk", "r") as lines:
    new_book = {"ISBN": [], "zaban": [], "onvan-padid_avarandeh": [], "vaziyat-virast": [],
                "vaziyat-nashr": [], "tarikh-pishbini-enteshar": [], "moshakhasat-zaheri": [], "yaddasht-koli": [],
                "tarjome": [], "tarjome-az": [], "mozo": []}

    for line in lines:
        if '=LDR  ' in line:
            books.append(new_book)
            new_book = {"ISBN": [], "zaban": [], "onvan-padid_avarandeh": [], "vaziyat-virast": [],
                        "vaziyat-nashr": [], "tarikh-pishbini-enteshar": [], "moshakhasat-zaheri": [],
                        "yaddasht-koli": [],
                        "tarjome": [], "tarjome-az": [], "mozo": []}

        if '=010  ' in line:
            ISBN = "".join(re.findall(r'\d+', str(line).replace("\n", "").replace("=010", "")))
            specialChars = "!#$%^&*()۰۱۲۳۴۵۶۷۸۹"
            for specialChar in specialChars:
                ISBN = ISBN.replace(specialChar, '')
            new_book["ISBN"].append(ISBN)

        if '=101  ' in line:
            dir_zaban = str(line).replace("\n", "")
            zaban = ''
            if 'ara' in dir_zaban: zaban = 'Arabic '
            if 'per' in dir_zaban: zaban += 'Persian '
            if 'eng' in dir_zaban: zaban += 'English '
            new_book["zaban"].append(zaban)

        if '=200  ' in line:
            onvan_padid_avarandeh = (str(line).replace("\n", ""))
            specialChars = ['1\$a', '\\$a', '$a', '$b', '$f/ ', '$f', '$g', '=200 ', '\\', '$d', '$c', '.']
            for specialChar in specialChars:
                onvan_padid_avarandeh = onvan_padid_avarandeh.replace(specialChar, '')
            new_book["onvan-padid_avarandeh"].append(onvan_padid_avarandeh)

        if '=205  ' in line:
            vaziyat_virast = str(line).replace("\n", "")
            specialChars = ['1\$a', '\\$a', '$a', '$b', '$f/ ', '$f', '$g', '=205 ', '.', '\\']
            for specialChar in specialChars:
                vaziyat_virast = vaziyat_virast.replace(specialChar, '')
            new_book["vaziyat-virast"].append(vaziyat_virast)

        if '=210  ' in line:
            vaziyat_nashr = (str(line).replace("\n", ""))
            specialChars = ['$e', '1\$a', '\\$a', '$a', '$b', '$f/ ', '$f', '$g', '=210 ', '\\', '$d', '$c']
            for specialChar in specialChars:
                vaziyat_nashr = vaziyat_nashr.replace(specialChar, '')
            new_book["vaziyat-nashr"].append(vaziyat_nashr)

        if '=211  ' in line:
            tarikh_pishbini_enteshar = (str(line).replace("\n", ""))
            specialChars = ['1\$a', '\\$a', '$a', '$b', '$f/ ', '$f', '$g', '=211 ', '\\', '$d', '$c']
            for specialChar in specialChars:
                tarikh_pishbini_enteshar = tarikh_pishbini_enteshar.replace(specialChar, '')
            new_book["tarikh-pishbini-enteshar"].append(tarikh_pishbini_enteshar)

        if '=215  ' in line:
            moshakhasat_zaheri = (str(line).replace("\n", ""))
            specialChars = ['1\$a', '\\$a', '$a', '$b', '$f/ ', '$f', '$g', '=215 ', '\\', '$d', '$c', '\\\\$a', '.']
            for specialChar in specialChars:
                moshakhasat_zaheri = moshakhasat_zaheri.replace(specialChar, '')
            new_book["moshakhasat-zaheri"].append(moshakhasat_zaheri)

        if '=300  ' in line:
            yaddasht_koli = (str(line).replace("\n", ""))
            specialChars = ['1\$a', '\\$a', '$a', '$b', '$f/ ', '$f', '$g', '=300 ', '\\', '$d', '$c', '\\\\$a', '.',
                            '"']
            for specialChar in specialChars:
                yaddasht_koli = yaddasht_koli.replace(specialChar, '')
            new_book["yaddasht-koli"].append(yaddasht_koli)

        if '=453  ' in line:
            tarjome = (str(line).replace("\n", ""))
            specialChars = ['1\$a', '\\$a', '$a', '$b', '$f/ ', '$f', '$g', '=453 ', '\\', '$d', '$c', '\\\\$a', '.']
            for specialChar in specialChars:
                tarjome = tarjome.replace(specialChar, '')
            new_book["tarjome"].append(tarjome)

        if '=454  ' in line:
            tarjome_az = (str(line).replace("\n", ""))
            specialChars = ['1\$a', '\\$a', '$a', '$b', '$f/ ', '$f', '$g', '=454 ', '\\', '$d', '$c', '\\\\$a', '.']
            for specialChar in specialChars:
                tarjome_az = tarjome_az.replace(specialChar, '')
            new_book["tarjome-az"].append(tarjome_az)

        if '=606  ' in line:
            mozo = (str(line).replace("\n", ""))
            specialChars = ['1\\', '2\\', '$9', '$2nli', '$bc', '1\$a', '\\$a', '$a', '$b', '$x', '$z', '$f/ ', '$f',
                            '$g', '=606 ', '\\', '$d', '$c', '\\\\$a', '.']
            for specialChar in specialChars:
                mozo = mozo.replace(specialChar, '')
            new_book["mozo"].append(mozo)

for book in books:
    json_object = json.dumps(book, indent=4, ensure_ascii=False).encode('utf8')
    print(json_object.decode())
    print("\n" * 4)

# for book in books:
#     write_json(book)