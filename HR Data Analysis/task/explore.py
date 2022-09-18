import pandas as pd
import requests
import os


def initialize():

    if not os.path.exists('../Data'):
        os.mkdir('../Data')

    # Download data if it is unavailable.
    if ('A_office_data.xml' not in os.listdir('../Data') and
        'B_office_data.xml' not in os.listdir('../Data') and
        'hr_data.xml' not in os.listdir('../Data')):
        print('A_office_data loading.')
        url = "https://www.dropbox.com/s/jpeknyzx57c4jb2/A_office_data.xml?dl=1"
        r = requests.get(url, allow_redirects=True)
        open('../Data/A_office_data.xml', 'wb').write(r.content)
        print('Loaded.')

        print('B_office_data loading.')
        url = "https://www.dropbox.com/s/hea0tbhir64u9t5/B_office_data.xml?dl=1"
        r = requests.get(url, allow_redirects=True)
        open('../Data/B_office_data.xml', 'wb').write(r.content)
        print('Loaded.')

        print('hr_data loading.')
        url = "https://www.dropbox.com/s/u6jzqqg1byajy0s/hr_data.xml?dl=1"
        r = requests.get(url, allow_redirects=True)
        open('../Data/hr_data.xml', 'wb').write(r.content)
        print('Loaded.')


def main():
    initialize()

    office_a = pd.read_xml('../Data/A_office_data.xml')
    office_b = pd.read_xml('../Data/B_office_data.xml')
    hr_data = pd.read_xml('../Data/hr_data.xml')

    id_a = office_a["employee_office_id"].to_numpy()
    office_a.index = ["A" + str(i) for i in id_a]

    id_b = office_b["employee_office_id"].to_numpy()
    office_b.index = ["B" + str(i) for i in id_b]

    hr_data = hr_data.set_index("employee_id")

    print(list(office_a.index.values))
    print(office_b.index.values.tolist())
    print(hr_data.index.values.tolist())


if __name__ == '__main__':
    main()

