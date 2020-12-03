from lxml import etree


def get_current_rates(current_rates_f, xml_f):
    xml = xml_f.read()
    root = etree.fromstring(xml)
    for appt in root.getchildren():
        for elem in appt.getchildren():
            if elem.tag == 'CharCode':
                code = elem.text
            elif elem.tag == 'Value':
                value = elem.text
        current_rates_f.write(f"{code}: {value} руб.\n")
    current_rates_f.close()
    xml_f.close()


def main():
    current_rates_f = open('current_rates.txt', 'w', encoding='utf-8')
    current_rates_f.write('Курс валют на сегодня:\n\n')
    with open('currencies.xml', encoding='utf-8') as xml_f:
        get_current_rates(current_rates_f, xml_f)


if __name__ == '__main__':
    main()
