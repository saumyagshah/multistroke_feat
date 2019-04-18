class Stroke:
    x = []
    y = []
    t = []

    def __init__(self, x, y, t = None,):
        self.x = x
        self.y = y
        self.t = t
        pass


    def getPoint(self, i):
        return [self.x[i],self.y[i],self.t[i]]

    def getStrokeLength()
