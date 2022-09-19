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
    office_a["employee_id"] = ["A" + str(i) for i in id_a]
    office_a.set_index("employee_id", inplace=True)

    id_b = office_b["employee_office_id"].to_numpy()
    office_b["employee_id"] = ["B" + str(i) for i in id_b]
    office_b.set_index("employee_id", inplace=True)

    hr_data.set_index("employee_id", drop=False, inplace=True)

    # 4
    result = pd.concat([office_a, office_b], axis=0)

    result = result.merge(hr_data, left_index=True, right_index=True)

    # 6

    result.drop(columns=['employee_office_id', 'employee_id'], inplace=True)
    result.dropna(inplace=True)

    # 7
    result.sort_index(inplace=True)
    print(result.index.tolist())
    print(result.columns.tolist())


if __name__ == '__main__':
    main()
