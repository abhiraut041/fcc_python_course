import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, cnt in kwargs.items():
            self.contents.extend([color for _ in range(cnt)])
    
    def draw(self, cnt):
        if cnt >= len(self.contents):
            res =[]
            res, self.contents = self.contents, res
            return res
        
        return [ self.contents.pop(random.randrange(len(self.contents)))  for _ in range(cnt) ]


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    M = 0
    for _ in range(num_experiments):
        curr_balls = hat.draw(num_balls_drawn)    
        if all(curr_balls.count(color) >= cnt  for color, cnt in expected_balls.items()):
            M += 1
        hat.contents.extend(curr_balls)
    return round(M/num_experiments, 2)


hat1 = Hat(yellow=3, blue=2, green=3)
print(experiment(hat1, {'yellow':2, 'green':0}, 4, 10))
