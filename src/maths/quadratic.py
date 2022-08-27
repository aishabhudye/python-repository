class MathsProcessor:

    '''
    Function name: determineRoots
    Input arguments: Whole numbers a, b and c
    Output: String describing the type of roots
    '''
    def determine_roots(self, a, b, c):
        discriminant = (b ** 2) - (4 * a * c)
        if discriminant > 0:
            return "2 distinct real roots"
        elif discriminant == 0:
            return "single real root"
        elif discriminant < 0:
            return "no real roots"
    '''End of def determineRoots'''

