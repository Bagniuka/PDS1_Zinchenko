dict_1 = {name: 'Rostyslav', surname: 'Zinchenko', age: 21}
dict_2 = {breakfast: 'milk', lunch: 'soup', dinner: 'buckwheat'}
dict_3 = {The_Green_book: 8.5, The_Lighthouse: 7.6, Se7en: 8.6}

def new_file(*dict, name):
    with open(name, 'w', encoding='utf8') as f:
        for i in dict:
            for k, v in i.items():
                kv = str(k) + ': ' + str(v) + '\n'
                f.write(kv)

new_file(dict_1, dict_2, dict_3, name="DZ_5_New_file")