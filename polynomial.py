from cmath import sqrt
import matplotlib.pyplot as plt  # type:ignore


class Poly2:
    """ Classe permettant de representer un polynôme de degré 2."""
    poly = {a*x**2+b*x+c==0}

    def __init__(self, *coeffs):
        """ Méthode constructeur qui prend en paramètre, les coefficients du polynôme"""
        self.coeffs = liste_coeffs
        pass

    def __add__(self, other):
        """Addition 2 polynômes et qui renvoi du nouveau polynôme"""
        z = Poly([0, 2, 3, 1])
        e = Poly([0, 0, 0, 0, 0, 0, 1])
        r = z + e
        print(r)
        assert r.coeffs == [0, 2, 3, 1, 0, 0, 1]
        pass

    def __sub__(self, other):
        """Soustraction de 2 polynômes et renvoi du nouveau polynôme"""
        z = Poly([0, 2, 3, 1])
        e = Poly([0, 0, 0, 0, 0, 0, 1])
        r = z - e
        print(r)
        assert r.coeffs == [0, 2, 3, 1, 0, 0, 1]
        pass

    def __repr__(self):
        msg = 'Poly2(' + ', '.join([str(c) for c in sorted(self.coeffs.values())]) + ')'
        return msg

    def __str__(self):
        """Méthode qui personalise la chaîne de caractère affichée par la fonction print
        Si: p1 = Poly(3, -4, 2)
        Alors print(p1) affiche: '2X^2 - 4X + 3'
        """
        pass

    def solve(self):
        """ Méthode qui renvoie les solutions si elles existent."""
        p=Rationnel(2,3)
        q=Rationnel(3,4)
        print ("z=",z)
        print ("e=",e)
        print("z+e=",z+e)
        print("z-e=",z-e)
        print("z*z=",z*z)
        print("z/e=",z/e)
        assert (z/e).z==8
        assert (z*e).e==12
        pass

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
        pass


if __name__ == "__main__":
    bar = [1, 1, 1]
    p1 = Poly2(*bar)

    baz = [1, 1, 1]
    p2 = Poly2(*baz)

    p3 = p1 + p2
    print(p3)  # affiche 2x^2 + 2x + 2

    print(p1.solve())  # affiche ((-0.5+0.8660254037844386j), (-0.5-0.8660254037844386j))
    p1.draw()  # trace la courbe de p1, voir fichier png
