def check_test(score):
    if score >= 80:
        return 'допуск получен'
    else:
        return 'к сожалению, вы не прошли'

amount = int(input('введите каличество участников:'))
for i in range(amount):
    name = input('введите имя:')
    score = int(input('введите каличество баллов:'))
    print(name, check_test(score))