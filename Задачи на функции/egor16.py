def cheng_course(wish):
    if wish.find('спорт') != -1:
        course = 'хоккей'
    elif wish.find('наука') != -1:
        course = 'астрономия'
    elif wish.find('исскуство') != -1:
        course = 'рисование'
    else:
        course = 'история'
    return course

amount = int(input('введите каличество студентов'))
for i in range(amount):
    wish = input('введите своё пожилание').lower()
    course = cheng_course(wish)
    print('рекомендуем вам курс:', course)
    if course == 'астраномия':
        print('внимание занятия проходят ночью')