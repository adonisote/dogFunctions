# to_learn = ['sit', 'lay down', 'attack']
# perfectioning = []
# ready_to_use = []

def tricks_learning(name, to_learn, perfectioning):
    while to_learn:
        current_trick = to_learn.pop()
        perfectioning.append(current_trick)
        print(f"{name.title()} will have to learn how to {current_trick}.")


#tricks_learning('pilatus', to_learn, perfectioning)


def tricks_perfectioning(name, perfectioning, ready_to_use):
    while perfectioning:
        current_trick = perfectioning.pop()
        ready_to_use.append(current_trick)
        print(f'{name.title()} is currently perfectioning how to {current_trick}')

#tricks_perfectioning('pilatus', perfectioning, ready_to_use)

def name_and_owner(dog_name, owner_name):
    return f"{dog_name.title()} belongs to {owner_name.title()}"

def dog_needs(dog_name, need_1 ='pop', need_2='sleep', need_3='eat'):
    return f"{dog_name} needs always to {need_1}, {need_2}, or {need_3}"

