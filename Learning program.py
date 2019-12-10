

def start():
    listt = {}
    first = input('Вы загадали человека?')
    while first == 'да':
        dif = input('Чем оно отличается от человека?')
        if dif not in listt:
            listt[dif] = []
        elif dif in listt:
            if len(listt[dif]) > 0:
            
