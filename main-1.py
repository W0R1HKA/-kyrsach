import sys, traceback



t = True
while t == 1:
    try:
        print(' Науки и их номера: \n 1) Физика\n 2) Биология \n 3) Информатика      ')
        a = input('Введите номер необходимой вам категории:')
        if a == 'закончить':
            break
        print('Формат книги и её номер: \n1) Справочник \n2) Учебник \n3) Энциклопедии          ')
        b = input('Введите номер необходимого вам формата:')
        if b == 'закончить':
            break
        a = int(a)
        b = int(b)
        t = False
    except ValueError:
        if a or b == str:
            t = True
    if a == 1:
        if b == 1:
            print( 'Название:Физика невозможного\nАвтор: Митио Каку             ')
            break
        elif b == 2:
            print( ' Название: Физика. 11 класс. Учебник. Базовый уровень \n Авторы: Мякишев Г. Я., Петрова М. А.                   ')
            break
        elif b == 3:
            print(' Название: Детская энциклопедия \n Автор: О’Каллаган Д., Фарндон Д., Филд Д., Брайт М., Митчелл А., О’Брайен С.;')
            break


    if a == 2:
        if b == 1:
            print( ' Название:  Биология. Готовимся к ОГЭ и ВПР \n Автор: Лаптева О. В.                        ')
            break
        elif b == 2:
            print(' Название: Биология. 5 класс. Бактерии, грибы, растения. Учебное пособие. ВЕРТИКАЛЬ \n Автор: Пасечник В. В.                                                               ')
            break
        elif b == 3:
            print( +' Название: Насекомые. Полная энциклопедия \n Авторы: Издательство «Эксмо»              ')
            break



    if a == 3:
        if b == 1:
            print(' Название:  ЕГЭ. Информатика. Новый полный справочник для подготовки к ЕГЭ \n Автор: Богомолова О.В.                                                    '+ s.zero)
            break

        elif b == 2:
            print( +' Название: Информатика. 9 класс. Учебник. ФГОС \n Авторы: Семакин И. Г., Залогова Л. А., Русаков С. В., Шестакова Л. В. '+ s.zero)
            break
        elif b == 3:
            print( +' Название: Энциклопедия школьной информатики \n Авторы: Издательство «Просвещение/БИНОМ»     ')
            break
        else:
            print( '---------------------------------------------------------------------------')
            print('Вы ввели значение, которе находится в стадии разработки) Попробуйте ещё раз' )
            print( '---------------------------------------------------------------------------' )
        t = True
    else:
        print('---------------------------------------------------------------------------' )
        print( 'Вы ввели значение, которе находится в стадии разработки) Попробуйте ещё раз')
        print('---------------------------------------------------------------------------')
    t = True

input()
