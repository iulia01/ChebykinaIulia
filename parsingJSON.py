import json


def decryption_currencies(decr_f, json_f):
    jsonData = json.load(json_f)
    for i in jsonData['Valute']:
        decr_f.write(f"{i} — {jsonData['Valute'][i]['Name']}" + '\n')
    json_f.close()


def main():
    decr_f = open('decryption_of_currencies.txt', 'w', encoding='utf-8')
    decr_f.write('Расшифровка международного кода валют: \n \n')
    with open('currencies.json', encoding='utf-8') as json_f:
        decryption_currencies(decr_f, json_f)


if __name__ == '__main__':
    main()
