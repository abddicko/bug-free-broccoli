from cmath import sqrt
import matplotlib.pyplot as plt  # type:ignore


class Poly2:
    """ Classe permettant de representer un polynôme de degré 2."""

    def __init__(self, *coeffs):
        """ Méthode constructeur qui prend en paramètre, les coefficients du polynôme"""
        self.coeffs = liste_coeffs
        pass

    def __add__(self, other):
        """Addition 2 polynômes et qui renvoi du nouveau polynôme"""
        assert type(other) is Poly2
        if self.coeffs[0] != 0:
            a = self.coeffs[0] + other.coeffs[0]
            b = self.coeffs[1] + other.coeffs[1]
            c = self.coeffs[2] + other.coeffs[2]
            print(f"{a}x² + {b}x + {c}")
            #return (self.coeffs + other.coeffs)
        else:
            print(f"{self.coeffs[0]} ne peut pas être égal à 0")


    def __sub__(self, other):
        """Soustraction de 2 polynômes et renvoi du nouveau polynôme"""
        assert type(other) is Poly2
        if self.coeffs[0] != 0:
            a = self.coeffs[0] - other.coeffs[0]
            b = self.coeffs[1] - other.coeffs[1]
            c = self.coeffs[2] - other.coeffs[2]
            if a == 0:
                print(0)
            else:
                print(f"{a}x² + {b}x + {c}")
        else:
            print(f"{self.coeffs[0]} ne peut pas être égal à 0")

    def __str__(self):
        """Méthode qui personalise la chaîne de caractère affichée par la fonction print
        Si: p1 = Poly(3, -4, 2)
        Alors print(p1) affiche: '2X^2 - 4X + 3'
        """
        if self.coeffs[1] >= 0 & self.coeffs[2] >= 0:
            polytype = f"{self.coeffs[0]}x² + {self.coeffs[1]}x + {self.coeffs[2]}"
        elif self.coeffs[1] < 0 & self.coeffs[2] >= 0:
            polytype = f"{self.coeffs[0]}x² - {abs(self.coeffs[1])}x + {self.coeffs[2]}"
        elif self.coeffs[1] < 0 & self.coeffs[2] < 0:
            polytype = f"{self.coeffs[0]}x² - {abs(self.coeffs[1])}x - {abs(self.coeffs[2])}"
        elif self.coeffs[1] <= 0 & self.coeffs[2] < 0:
            polytype = f"{self.coeffs[0]}x² + {self.coeffs[1]}x - {abs(self.coeffs[2])}"
            
        return polytype

    def solve(self):
        """ Méthode qui renvoie les solutions si elles existent."""
        if self.coeffs[0] != 0:
            a = self.coeffs[0]
            b = self.coeffs[1]
            c = self.coeffs[2]
            
            # calculate the discriminant
            d = (b**2) - (4*a*c)
            # find two solutions
            sol2 = (-b - sqrt(d))/(2*a)
            sol1 = (-b + sqrt(d))/(2*a)
            
            resultat = ((resultat1), (resultat2))
            print(f"{resultat}")
            return resultat

    def __val(self, x):
        """ Méthode qui calcule et renvoie la valeur de y en fonction de x.
        Si: y = x^2 + 1
        Si: x prend pour valeur 5
        Alors: y = 5^2 + 1 = 26
        """
        pass

    def draw(self, x_points=None):
        """ Méthode qui trace la courbe, voir fichier png."""
    x = np.linspace(-2,2,100)
    y = np.exp(x)
    plt.title('Courbe de P1')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.plot(x, y, alpha = 0.4,
    color ='green', linestyle ='dashed',
    linewidth = 2)
    plt.grid(alpha =.6, linestyle ='-')
    plt.plot(x,y, 'y', label='f(x)=e^x')
    plt.legend(loc='upper left')
    plt.show()


if __name__ == "__main__":
    bar = [1, 1, 1]
    p1 = Poly2(*bar)

    baz = [1, 1, 1]
    p2 = Poly2(*baz)

    p3 = p1 + p2
    print(p3)  # affiche 2x^2 + 2x + 2

    print(p1.solve())  # affiche ((-0.5+0.8660254037844386j), (-0.5-0.8660254037844386j))
    p1.draw()  # trace la courbe de p1, voir fichier png
