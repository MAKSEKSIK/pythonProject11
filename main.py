import random
length = 10
health = 100
respect = 20
weight = 30
print("Ваша цель: Добиться уважения больше 100 и не дать основным параметрам упасть до нуля")
while length > 0 and health > 0 and respect > 0 and weight > 0 and respect < 100:
    print("Ваши характеристики:")
    print("Длина норы:", length)
    print("Здоровье:", health)
    print("Уважение:", respect)
    print("Вес:", weight)
    print()
    print("Что хотите сделать?")
    print("1. Копать нору")
    print("2. Поесть травы")
    print("3. Подраться")
    print("4. Проспать весь день")

    a = int(input())
    if a == 1:
        print("1. Интенсивно")
        print("2. Лениво")
        b = int(input())
        if b == 1:
            length += 5
            health -= 30
        if b == 2:
            length += 2
            health -= 10
    if a == 2:
        print("1. Жулхой")
        print("2. Зелёной")
        b = int(input())
        if b == 1:
            health += 10
            weight += 15
        if b == 2:
            if respect < 30:
                health -= 30
            if respect >= 30:
                health += 30
                weight += 30
    if a == 3:
        print("1. Со слабым существом")
        print("2. Со средним существом")
        print("3. С сильным существом")
        b = int(input())
        if b == 1:
            enemy_weight = 30
            summ = abs(weight - enemy_weight)
            rand = random.randint(1, weight + enemy_weight)
            if rand <= weight:
                print("Ты выиграл")
                respect += 10
                health -= summ
            else:
                print("Ты проиграл")
                health -= summ
        if b == 2:
            enemy_weight = 50
            summ = abs(weight - enemy_weight)
            rand = random.randint(1, weight + enemy_weight)
            if rand <= weight:
                print("Ты выиграл")
                respect += 20
                health -= summ
            else:
                print("Ты проиграл")
                health -= summ
        if b == 3:
            enemy_weight = 70
            summ = abs(weight - enemy_weight)
            rand = random.randint(1, weight + enemy_weight)
            if rand <= weight:
                print("Ты выиграл")
                respect += 40
                health -= summ
            else:
                print("Ты проиграл")
                health -= summ
    if a == 4:
        length -= 2
        health += 20
        respect -= 2
        weight -= 5
    else:
        print("Вы думали над выбором весь день, пока не наступила ночь")
    print("Наступила ночь")
    length -= 2
    health += 20
    respect -= 2
    weight -= 5
if (respect >= 100):
    print("Вы прошли игру")
if (health <= 0 or weight <= 0 or respect <= 0 or length <= 0):
    print("Вы умерли")