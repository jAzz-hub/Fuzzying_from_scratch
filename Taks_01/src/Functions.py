from numpy import asarray

def Triangular(x, a, b, c):
    

    nao_SAT_error = ValueError("Os valores de a, b e c geram Insatisfazibilidade da função triângular") 

    x = asarray(x)              #Garantindo que o valor de x passado será um array, mesmo que seja um único valor
    
    if a <= b <= c:             # a <= b <= c
        raise nao_SAT_error
    
    else:
        if x <= a or x >= c:        #  x <= a  OU  x >= c 
            return 0
        elif x <= b and x >= a:     # a <= x <= b
            return (x - a)/(b - a)
        elif  x >= b and x <= c:    # b <= x <= c
            return (c - x)/(c - b)
        else:
            raise nao_SAT_error

def Trapezoidal(x):


def Gaussiana(x):


def Sigmoidal(x):


def SinoGeneralizada(x):


def FuncS(x):


def FuncZ(x):


def Cauchy(x):


def GaussianaDupla(x):


def MyOption1(x):


def MyOption2(x):
