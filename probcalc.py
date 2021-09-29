'''
Create a lottery ball, or Hat, that takes a variable number of arguments
that specify the number of balls of each color that are in the hat. Give
the object the ability to pick a random number of balls from the hat,
which will then be used to compute the probability of picking a certain
distribution of balls over a large number of experiments.
'''

from random import choice

class ProbabilityCalculator():
    def __init__(self, dict):
        self.dict = dict
        self.colours = dict.keys()
        balls = []
        for colour in self.colours:
            balls.extend([colour for i in range(dict[colour])])
        self.balls = balls
    
    def sample(self, n):
        sample = []
        for i in range(n):
            sample.append(choice(self.balls))
        sample_result = {colour:(sample.count(colour) / n) for colour in self.colours}
        return sample_result

probcalc = ProbabilityCalculator({"red":3, "green":4, "blue":5, "yellow":2, "black":10, "white":7})
print(probcalc.sample(100))
