'''
Create a class which represents hats with coloured balls, that takes a 
variable number of arguments specifying the number of balls of each colour 
that are in the hat. Define a method which can be used to take a random 
sample of balls from the hat, and record the occurences of each colour to
calculate the distribution of colours within the hat.
'''

from random import choice

class ProbabilityCalculator():
    def __init__(self, **cols):
        self.dict = cols
        self.colours = cols.keys()
        balls = []
        for colour in self.colours:
            balls.extend([colour for i in range(cols[colour])])
        self.balls = balls
    
    def sample(self, n):
        return {colour:([choice(self.balls) for i in range(n)].count(colour) / n) for colour in self.colours}

# Example usage
probcalc = ProbabilityCalculator(red=3, green=4, blue=5, yellow=2, black=10, white=7)
print(probcalc.sample(1000))
