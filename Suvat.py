class SUVAT :
    '''
v = u + at              DONE
v**2 = u**2 + 2as       DONE
s = ut + (1/2)at**2     DONE KINDA
s = vt - (1/2)at**2     DONE KINDA
s = (1/2)(u + v)t       DONE KINDA

Find logic              GETTING THERE

    '''

    def __init__(self, S=None, U=None, V=None, A=None, T=None) :
        self.S = S
        self.U = U
        self.V = V
        self.A = A
        self.T = T


    def v_equals_u_plus_at(self) :
        if (self.V is None) and (type(self.U) is int or type(self.U) is float) and (type(self.A) is int or type(self.A) is float) and (type(self.T) is int or type(self.T) is float) :
            self.V = self.U + (self.A * self.T)
            return self.V

        elif (self.U is None) and (type(self.V) is int or type(self.V) is float) and (type(self.A) is int or type(self.A) is float) and (type(self.T) is int or type(self.T) is float) :
            self.U = self.V - (self.A * self.T)
            return self.U

        elif (self.A is None) and (type(self.V) is int or type(self.V) is float) and (type(self.U) is int or type(self.U) is float) and (type(self.T) is int or type(self.T) is float) :
            self.A = (self.V - self.U) / self.T
            return self.A

        elif (self.T is None) and (type(self.V) is int or type(self.V) is float) and (type(self.A) is int or type(self.A) is float) and (type(self.U) is int or type(self.U) is float) :
            self.T = (self.V - self.U) / self.A
            return self.T

        else :
            return "ERROR: all values already fulfilled"

    def v_squared_equals_u_squared_plus_2as(self) :
        if (self.V is None) and (type(self.U) is int or type(self.U) is float) and (type(self.A) is int or type(self.A) is float) and (type(self.S) is int or type(self.S) is float) :
            V_squared = (self.U ** 2) + (2 * self.A + self.S)
            self.V = V_squared ** (1/2)
            return self.V

        elif (self.U is None) and (type(self.V) is int or type(self.V) is float) and (type(self.A) is int or type(self.A) is float) and (type(self.S) is int or type(self.S) is float) :
            U_squared = (self.V ** 2) - (2 * self.A * self.S)
            self.U = U_squared ** (1/2)
            return self.U

        elif (self.S is None) and (type(self.U) is int or type(self.U) is float) and (type(self.A) is int or type(self.A) is float) and (type(self.V) is int or type(self.V) is float) :
            self.S = ((self.V ** 2) - (self.U ** 2)) / (2 * self.A)
            return self.S

        elif (self.A is None) and (type(self.U) is int or type(self.U) is float) and (type(self.V) is int or type(self.V) is float) and (type(self.S) is int or type(self.S) is float) :
            self.A = ((self.V ** 2) - (self.U ** 2)) / (2 * self.S)
            return self.A

        else:
            return "ERROR: all values already fulfilled"

    def s_equals_ut_plus_half_at_squared(self) :
        if (self.S is None) and (type(self.U) is int or type(self.U) is float) and (type(self.T) is int or type(self.T) is float) and (type(self.A) is int or type(self.A) is float) :
            self.S = (self.U * self.T) + (0.5 * self.A * (self.T ** 2))
            return self.S

    def s_equals_vt_minus_half_at_squared(self) :
        if (self.S is None) and (type(self.V) is int or type(self.V) is float) and (type(self.T) is int or type(self.T) is float) and (type(self.A) is int or type(self.A) is float) :
            self.S = (self.V * self.T) - (0.5 * self.A * (self.T ** 2))
            return self.S

    def s_equals_half_u_plus_v_t(self) :
        if (self.S is None) and (type(self.U) is int or type(self.U) is float) and (type(self.V) is int or type(self.V) is float) and (type(self.T) is int or type(self.T) is float) :
            self.S = 0.5 * (self.U + self.V) * self.T
            return self.T

    def Find(self,find) :
        if (find.lower() == 'v')  and (self.V is None) :
            if (type(self.U) is int or type(self.U) is float) and (type(self.S) is int or type(self.S) is float) and (type(self.A) is int or type(self.A) is float) :
                return round(self.v_squared_equals_u_squared_plus_2as(),1)
            elif (type(self.U) is int or type(self.U) is float) and (type(self.A) is int or type(self.A) is float) and (type(self.T) is int or type(self.T) is float) :
                return round(self.v_equals_u_plus_at(),1)


Q1 = SUVAT(U = 10, T = 20, A = 9.8)
print(Q1.Find("v"))
print(Q1.V)

Lol = None

if type(Lol) is float or type(Lol) is int:
    print("cool")
