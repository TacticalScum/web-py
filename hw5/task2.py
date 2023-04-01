def salaries_calculating(name, salary, award):
    award_percent=[]
    for i in range(0, len(award)):
        award_percent.append(salary[i] + salary[i] * float(award[i].replace('%', ''))/100)
    
    salarys_dict = {key: value for key, value in zip(name, award_percent)}
    return salarys_dict

    
employers = ['Oleg', 'Vadim', 'Alex', 'Egor']
salary = [12000, 20000, 16000, 10000]
award = ['8%', '7.9%', '12%', '20%']

print(salaries_calculating(employers, salary, award))
