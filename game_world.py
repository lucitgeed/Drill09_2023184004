# wordl [0]:백그라운드 객체들
# world[1] : foreground 객체들
world = [[],[] , []]       # <- 월드리스트를 리스트 of 리스트로 변경


def add_object(o, depth):
    world[depth].append(o)


def update():
    for layer in world:
        for o in layer:
            o.update()


def render():
    for layer in world:
        for o in layer:
            o.draw()


def remove_object(o):       #다만 여기서 없는 o존재를 remove하면 프로그램이 죽으니까
    #조건문을 추가.
    for layer in world:
        if o in layer:
            layer.remove(o)
            return

    print(f'CRITICAL : 존재하지 않는 객체{o}를 지우려고 시도함')
