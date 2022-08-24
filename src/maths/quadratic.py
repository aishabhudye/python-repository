class MathsProcessor:

    def solve(self, a, b, c):
        a
        b
        c

        discriminant = (b ** 2) - (4 * a * c)
        if discriminant > 0:
            return "2 distinct real roots"
        elif discriminant == 0:
            return "single real root"
        elif discriminant < 0:
            return "no real roots"


