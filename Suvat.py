from math import sqrt
class SUVAT :
    '''
Basic SUVAT class created using lots of ugly selection

made by Tom Moldon
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
            pass

    def v_squared_equals_u_squared_plus_2as(self) :
        if (self.V is None) and (type(self.U) is int or type(self.U) is float) and (type(self.A) is int or type(self.A) is float) and (type(self.S) is int or type(self.S) is float) :
            V_squared = (self.U ** 2) + (2 * self.A + self.S)
            self.V = sqrt(V_squared)
            return self.V

        elif (self.U is None) and (type(self.V) is int or type(self.V) is float) and (type(self.A) is int or type(self.A) is float) and (type(self.S) is int or type(self.S) is float) :
            U_squared = (self.V ** 2) - (2 * self.A * self.S)
            self.U = sqrt(U_squared)
            return self.U

        elif (self.S is None) and (type(self.U) is int or type(self.U) is float) and (type(self.A) is int or type(self.A) is float) and (type(self.V) is int or type(self.V) is float) :
            self.S = ((self.V ** 2) - (self.U ** 2)) / (2 * self.A)
            return self.S

        elif (self.A is None) and (type(self.U) is int or type(self.U) is float) and (type(self.V) is int or type(self.V) is float) and (type(self.S) is int or type(self.S) is float) :
            self.A = ((self.V ** 2) - (self.U ** 2)) / (2 * self.S)
            return self.A

        else:
            pass

    def s_equals_ut_plus_half_at_squared(self) :
        if (self.S is None) and (type(self.U) is int or type(self.U) is float) and (type(self.T) is int or type(self.T) is float) and (type(self.A) is int or type(self.A) is float) :
            self.S = (self.U * self.T) + (0.5 * self.A * (self.T ** 2))
            return self.S
        elif (self.U is None) and (type(self.S) is int or type(self.S) is float) and (type(self.T) is int or type(self.T) is float) and (type(self.A) is int or type(self.A) is float) :
            self.U = (self.S -(self.A * (self.T ** 2))) / (2 * self.T)
            return self.U
        elif (self.A is None) and (type(self.S) is int or type(self.S) is float) and (type(self.T) is int or type(self.T) is float) and (type(self.U) is int or type(self.U) is float) :
            self.A = (2 * (self.S - (self.U * self.T))) / (self.T ** 2)
            return self.A
        elif (self.T is None) and (type(self.S) is int or type(self.S) is float) and (type(self.U) is int or type(self.U) is float) and (type(self.A) is int or type(self.A) is float) :
            self.T = sqrt((2 * self.A * self.S) + (self.U ** 2) - self.U) / self.A
            return self.T
        else:
            pass

    def s_equals_vt_minus_half_at_squared(self) :
        if (self.S is None) and (type(self.V) is int or type(self.V) is float) and (type(self.T) is int or type(self.T) is float) and (type(self.A) is int or type(self.A) is float) :
            self.S = (self.V * self.T) - (0.5 * self.A * (self.T ** 2))
            return self.S
        elif (self.V is None) and (type(self.S) is int or type(self.S) is float) and (type(self.T) is int or type(self.T) is float) and (type(self.A) is int or type(self.A) is float) :
            self.V = (self.S + (self.A * (self.T ** 2))) / (2 * self.T)
            return self.V
        elif (self.A is None) and (type(self.V) is int or type(self.V) is float) and (type(self.T) is int or type(self.T) is float) and (type(self.S) is int or type(self.S) is float) :
            self.A = (2 * ((self.V * self.T) - self.S)) / (self.T ** 2)
            return self.A
        elif (self.T is None) and (type(self.V) is int or type(self.V) is float) and (type(self.S) is int or type(self.S) is float) and (type(self.A) is int or type(self.A) is float) :
            self.T = (self.V - sqrt((self.V ** 2) - (2 * self.A * self.S)))
            return self.T
        else:
            pass

    def s_equals_half_u_plus_v_t(self) :
        if (self.S is None) and (type(self.U) is int or type(self.U) is float) and (type(self.V) is int or type(self.V) is float) and (type(self.T) is int or type(self.T) is float) :
            self.S = (self.T / 2) * (self.U + self.V)
            return self.S
        elif (self.U is None) and (type(self.S) is int or type(self.S) is float) and (type(self.V) is int or type(self.V) is float) and (type(self.T) is int or type(self.T) is float) :
            self.U = ((2 * self.S) / self.T) + self.V
            return self.U
        elif (self.V is None) and (type(self.U) is int or type(self.U) is float) and (type(self.S) is int or type(self.S) is float) and (type(self.T) is int or type(self.T) is float) :
            self.V = ((2 * self.S) / self.T) - self.U
            return self.V
        elif (self.T is None) and (type(self.U) is int or type(self.U) is float) and (type(self.V) is int or type(self.V) is float) and (type(self.S) is int or type(self.S) is float) :
            self.T = (2 * self.S) / (self.U + self.V)
            return self.T
        else:
            pass


    def Find(self) :
        while type(self.S) is not float:
            print("check 1")
            self.v_squared_equals_u_squared_plus_2as()
            self.s_equals_ut_plus_half_at_squared()
            self.s_equals_half_u_plus_v_t()
            self.s_equals_vt_minus_half_at_squared()
            print("check 2")

        while type(self.U) is not float:
            self.s_equals_ut_plus_half_at_squared()
            self.v_equals_u_plus_at()
            self.v_squared_equals_u_squared_plus_2as()
            self.s_equals_half_u_plus_v_t()

        while type(self.V) is not float:
            self.v_equals_u_plus_at()
            self.s_equals_half_u_plus_v_t()
            self.s_equals_vt_minus_half_at_squared()
            self.v_squared_equals_u_squared_plus_2as()

        while type(self.A) is not float:
            self.v_equals_u_plus_at()
            self.v_squared_equals_u_squared_plus_2as()
            self.s_equals_ut_plus_half_at_squared()
            self.s_equals_vt_minus_half_at_squared()

        while type(self.T) is not float:
            self.v_equals_u_plus_at()
            self.s_equals_ut_plus_half_at_squared()
            self.s_equals_vt_minus_half_at_squared()
            self.s_equals_half_u_plus_v_t()

        return None



        # if (find.lower() == 'v')  and (self.V is None) :
        #     if (type(self.U) is int or type(self.U) is float) and (type(self.S) is int or type(self.S) is float) and (type(self.A) is int or type(self.A) is float) :
        #         return round(self.v_squared_equals_u_squared_plus_2as(),1)
        #     elif (type(self.U) is int or type(self.U) is float) and (type(self.A) is int or type(self.A) is float) and (type(self.T) is int or type(self.T) is float) :
        #         return round(self.v_equals_u_plus_at(),2)
        #     else :
        #         return "ERROR: EITHER SUPPORT IS YET TO BE ADDED OR WRONG VARIABLES ADDED"
        #
        # elif (find.lower() == 's') and (self.S is None) :
        #     if (type(self.U) is int or type(self.U) is float) and (type(self.V) is int or type(self.V) is float) and (type(self.T) is int or type(self.T) is float) :
        #         return round(self.s_equals_half_u_plus_v_t(),1)
        #     elif (type(self.U) is int or type(self.U) is float) and (type(self.A) is int or type(self.A) is float) and (type(self.T) is int or type(self.T) is float) :
        #         return round(self.s_equals_ut_plus_half_at_squared(),2)
        #     elif (type(self.V) is int or type(self.V) is float) and (type(self.A) is int or type(self.A) is float) and (type(self.T) is int or type(self.T) is float) :
        #         return round(self.s_equals_vt_minus_half_at_squared(),2)
        #     else :
        #         return "ERROR: EITHER SUPPORT IS YET TO BE ADDED OR WRONG VARIABLES ADDED"
        #
        # elif (find.lower() == 't') and (self.T is None) :
        #     if (type(self.V) is int or type(self.V) is float) and (type(self.U) is int or type(self.U) is float) and (type(self.A) is int or type(self.A) is float) :
        #         return round(self.v_equals_u_plus_at(),2)
        #     else :
        #         return "ERROR: EITHER SUPPORT IS YET TO BE ADDED OR WRONG VARIABLES ADDED"
        #
        # elif (find.lower() == 'u') and (self.U is None) :
        #     if (type(self.V) is int or type(self.V) is float) and (type(self.A) is int or type(self.A) is float) and (type(self.T) is int or type(self.T) is float) :
        #         return round(self.v_equals_u_plus_at(),2)
        #     elif (type(self.V) is int or type(self.V) is float) and (type(self.A) is int or type(self.A) is float) and (type(self.S) is int or type(self.S) is float) :
        #         if type(self.v_squared_equals_u_squared_plus_2as()) is complex:
        #             raise TypeError("Result is a complex number")
        #         else:
        #             return round(self.v_squared_equals_u_squared_plus_2as(),2)
        #     else:
        #         return "ERROR: EITHER SUPPORT IS YET TO BE ADDED OR WRONG VARIABLES ADDED"
        #
        # elif (find.lower() == 'a') and (self.A is None) :
        #     if (type(self.V) is int or type(self.V) is float) and (type(self.U) is int or type(self.U) is float) and (type(self.T) is int or type(self.T) is float) :
        #         return round(self.v_equals_u_plus_at(),2)
        #     elif (type(self.V) is int or type(self.V) is float) and (type(self.U) is int or type(self.U) is float) and (type(self.S) is int or type(self.S) is float) :
        #         return round(self.v_squared_equals_u_squared_plus_2as(),2)
        #     else:
        #         return "ERROR: EITHER SUPPORT IS YET TO BE ADDED OR WRONG VARIABLES ADDED"
        #
        # else:
        #     return "ERROR: YOU DID NOT SELECT A VALID VARIABLE TO FIND"






    def print_values(self) :
        values = f'''
S is {self.S}
U is {self.U}
V is {self.V}
A is {self.A}
T is {self.T}
        '''
        print(values)
