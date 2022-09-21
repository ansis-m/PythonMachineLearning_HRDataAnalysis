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


def count_bigger_5(df):
    count = 0
    for i in df:
        if i > 5:
            count += 1
    return count


def share(series):
    true = 0
    for i in series:
        if i:
            true += 1
    return true/len(series)

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

    # print(result.salary)
    # print(result.index.tolist())
    # print(result.columns.tolist())

    #8a

    # top10hours = result.sort_values(by=['average_monthly_hours'], ascending=False).head(10).Department.values.tolist()
    # print(top10hours)

    #8b

    # number_of_projects = result[(result.salary == 'low') & (result.Department == 'IT')].number_project.sum()
    # print(number_of_projects)

    #8c

    # print(result.loc[['A4', 'B7064', 'A3033'], ['last_evaluation', 'satisfaction_level']].values.tolist())

    # *************************************************************************************************

    # the median number of projects the employees in a group worked upon, and how many employees worked on more than five projects;
    # the mean and median time spent in the company;
    # the share of employees who've had work accidents;
    # the mean and standard deviation of the last evaluation score



    # print(result.columns)
    # print("\n****************************************************\n")
    # print(result.groupby(['left']).agg({'number_project': 'median'}))
    # print("\n****************************************************\n")
    # print(result.groupby(['left']).agg({'number_project': count_bigger_5}))
    # print("\n****************************************************\n")
    # print(result.groupby(['left']).agg({'time_spend_company': 'mean'}).round(2))
    # print("\n****************************************************\n")
    # print(result.groupby(['left']).agg({'time_spend_company': 'median'}).round(2))
    # print("\n****************************************************\n")
    # print(result.groupby(['left']).agg({'Work_accident': share}).round(2))
    # print("\n****************************************************\n")
    # print(result.groupby(['left']).agg({'last_evaluation': 'mean'}).round(2))
    # print("\n****************************************************\n")
    # print(result.groupby(['left']).agg({'last_evaluation': 'std'}).round(2).to_dict())

    a = {('number_project', 'median'): result.groupby(['left']).agg({'number_project': 'median'}).to_dict().pop(
        'number_project')}

    b = {('number_project', 'count_bigger_5'): result.groupby(['left']).agg({'number_project': count_bigger_5}).to_dict().pop('number_project')}

    c = {('time_spend_company', 'mean'): result.groupby(['left']).agg({'time_spend_company': 'mean'}).round(2).to_dict().pop('time_spend_company')}

    d = {('time_spend_company', 'median'): result.groupby(['left']).agg({'time_spend_company': 'median'}).round(2).to_dict().pop('time_spend_company')}

    e = {('Work_accident', 'mean'): result.groupby(['left']).agg({'Work_accident': share}).round(2).to_dict().pop('Work_accident')}

    f = {('last_evaluation', 'mean'): result.groupby(['left']).agg({'last_evaluation': 'mean'}).round(2).to_dict().pop('last_evaluation')}

    g = {('last_evaluation', 'std'): result.groupby(['left']).agg({'last_evaluation': 'std'}).round(2).to_dict().pop('last_evaluation')}

    print(a | b | c | d | e | f | g)




if __name__ == '__main__':
    main()
