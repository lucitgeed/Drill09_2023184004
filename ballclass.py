from pico2d import load_image

import game_world

class Ball:
    image = None

    def __init__(self, x = 400, y = 300, velocity = 1):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y, self.velocity = x, y, velocity

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.x += self.velocity
        if self.x < 100 or self.x > 700:
            game_world.remove_object(self)      #게임 월드에서부터 객체를, 자기자신을 remove.
