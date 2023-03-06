import math
# need to import math because calculating square root is required
import cmath
# need [cmath] for handling complex/imaginary numbers.
decimal_place = dp = 4
# Variable to dictate how many decimal places of answer do I want,
# in other words this variable controls the precision I want in my solutions


def round_complex(num):
    return round(num.real, dp) + round(num.imag, dp) * 1j
# self-created module to round up the complex values


print("\n                                     <Solving SUVAT equations> \n")

# Inputs from user: ideally in int/float, but if str/bool is used, user will be notified by "except" in the end.
a1 = input("Enter ACCELERATION value (in m/s^-2): ")
t1 = input("Enter TIME value (in s): ")
s1 = input("Enter TRAVELED DISTANCE value (in m): ")
v1 = input("Enter FINAL VELOCITY value (in m/s^-1): ")
u1 = input("Enter INITIAL VELOCITY value (in m/s^-1): ")

try:
    # First, all the combination of values that are insufficient for solving SUVAT equations due to lack of information
    if u1 == "" and v1 == "" and s1 == "" and t1 == "" and a1 == "":
        print("\n## Not enough information ##")

    elif v1 == "" and s1 == "" and t1 == "" and a1 == "":
        print("\n## Not enough information ##")
    elif s1 == "" and u1 == "" and v1 == "" and a1 == "":
        print("\n## Not enough information ##")
    elif s1 == "" and u1 == "" and v1 == "" and t1 == "":
        print("\n## Not enough information ##")
    elif s1 == "" and u1 == "" and a1 == "" and t1 == "":
        print("\n## Not enough information ##")
    elif u1 == "" and v1 == "" and a1 == "" and t1 == "":
        print("\n## Not enough  information ##")

    elif s1 == "" and u1 == "" and v1 == "":
        print("\n## Not enough  information ##")
    elif s1 == "" and u1 == "" and a1 == "":
        print("\n## Not enough  information ##")
    elif s1 == "" and u1 == "" and t1 == "":
        print("\n## Not enough  information ##")
    elif s1 == "" and v1 == "" and a1 == "":
        print("\n## Not enough  information ##")
    elif s1 == "" and v1 == "" and t1 == "":
        print("\n## Not enough  information ##")
    elif s1 == "" and a1 == "" and t1 == "":
        print("\n## Not enough  information ##")
    elif u1 == "" and v1 == "" and a1 == "":
        print("\n## Not enough  information ##")
    elif u1 == "" and v1 == "" and t1 == "":
        print("\n## Not enough  information ##")
    elif u1 == "" and a1 == "" and t1 == "":
        print("\n## Not enough  information ##")
    elif v1 == "" and a1 == "" and t1 == "":
        print("\n## Not enough  information ##")

    # Now with at least three values we can start solving equations.
    elif s1 == "" and u1 == "":
        # The original input was in str so need to convert the values in float here. EVERYTIME.
        a = float(a1)
        t = float(t1)
        v = float(v1)
        u = v - (a * t)
        s = ((v + u) / 2) * t
        # It is better to round up the values to certain decimal places
        u = round(u, dp)
        s = round(s, dp)
        print("\nINITIAL VELOCITY = " + str(u) + " m/s^-1")
        # If the value is negative, the NOTE will pop up
        if u != math.fabs(u):
            print("[Note: negative value means the velocity was in opposite direction "
                  "relative to the positive velocity]")
        print("\nTRAVELED DISTANCE = " + str(s) + " m")
        if s != math.fabs(s):
            print("[Note: negative value means the Distance is in the opposite direction relative to the direction "
                  "of positive vector(s)]")

    elif s1 == "" and v1 == "":
        a = float(a1)
        t = float(t1)
        u = float(u1)
        v = u + (a * t)
        s = ((v + u) / 2) * t
        v = round(v, dp)
        s = round(s, dp)
        print("\nFINAL VELOCITY = " + str(v) + " m/s^-1")
        if v != math.fabs(v):
            print("[Note: negative value means the velocity was in opposite direction "
                  "relative to the positive velocity]")
        print("\nTRAVELED DISTANCE = " + str(s) + " m")
        if s != math.fabs(s):
            print("[Note: negative value means the Distance is in the opposite direction relative to the direction "
                  "of positive vector(s)]")

    elif s1 == "" and a1 == "":
        t = float(t1)
        v = float(v1)
        u = float(u1)
        a = (v - u) / t
        # Here if the value of t was 0, it is a division by zero error. Issue addressed at the end with another "except"
        s = ((v + u) / 2) * t
        a = round(a, dp)
        s = round(s, dp)
        print("\nACCELERATION = " + str(a) + " m/s^-2")
        if a != math.fabs(a):
            print("[Note: negative value means the acceleration was in opposite direction "
                  "relative to the positive velocity]")
        print("\nTRAVELED DISTANCE = " + str(s) + " m")
        if t != math.fabs(t):
            print("[Note: this value for Time (t) is unrealistic. Time can not be negative]")

    elif s1 == "" and t1 == "":
        a = float(a1)
        v = float(v1)
        u = float(u1)
        t = (v - u) / a
        s = ((v + u) / 2) * t
        t = round(t, dp)
        s = (round(s, dp))
        print("\nTIME = " + str(t) + " s")
        if t != math.fabs(t):
            print("[Note: this value for Time (t) is unrealistic. Time can not be negative]")
        print("\nTRAVELED DISTANCE = " + str(s) + " m")
        if s != math.fabs(s):
            print("[Note: negative value means the Distance is in the opposite direction relative to the direction "
                  "of positive vector(s)]")

    elif u1 == "" and v1 == "":
        a = float(a1)
        t = float(t1)
        s = float(s1)
        u = ((2 * s) - (a * t * t)) / (2 * t)
        v = u + (a * t)
        u = round(u, dp)
        v = round(v, dp)
        print("\nINITIAL VELOCITY = " + str(u) + " m/s^-1")
        if u != math.fabs(u):
            print("[Note: negative value means the velocity was in opposite direction "
                  "relative to the positive velocity]")
        print("\nFINAL VELOCITY = " + str(v) + " m/s^-1")
        if v != math.fabs(v):
            print("[Note: negative value means the velocity was in opposite direction "
                  "relative to the positive velocity]")

    elif u1 == "" and a1 == "":
        t = float(t1)
        s = float(s1)
        v = float(v1)
        u = ((2 * s) - (v * t)) / t
        a = (v - u) / t
        u = round(u, dp)
        a = round(a, dp)
        print("\nINITIAL VELOCITY = " + str(u) + " m/s^-1")
        if u != math.fabs(u):
            print("[Note: negative value means the velocity was in opposite direction "
                  "relative to the positive velocity]")
        print("\nACCELERATION = " + str(a) + " m/s^-2")
        if a != math.fabs(a):
            print("[Note: negative value means the acceleration was in opposite direction "
                  "relative to the positive velocity]")

    elif u1 == "" and t1 == "":
        a = float(a1)
        s = float(s1)
        v = float(v1)
        # have to check if the value was going to be negative or positive.
        # Cause there will either be normal value for rooting positive or complex/imaginary for negative roots
        if (v*v) > (2*a*s):
            u = math.sqrt((v * v) - (2 * a * s))
            t = (v - u) / a
            u = round(u, dp)
            t = round(t, dp)
            print("\nINITIAL VELOCITY = " + str(u) + " m/s^-1")
            if u != math.fabs(u):
                print("[Note: negative value means the velocity was in opposite direction "
                      "relative to the positive velocity]")
            print("\nTIME = " + str(t) + " s")
            if t != math.fabs(t):
                print("[Note: this value for Time (t) is unrealistic. Time can not be negative]")

        elif (v * v) < (2 * a * s):
            u = cmath.sqrt((v * v) - (2 * a * s))
            u = round_complex(u)
            print("\nINITIAL VELOCITY = " + str(u) + " m/s^-1")
            print("[Note: this value for Initial Velocity (u) is partially or completely Imaginary.]")
            t = (v - u) / a
            t = round_complex(t)
            print("\nTIME = " + str(u) + " s")
            print("[Note: this value for Time (t) is partially or completely Imaginary.]")

    elif v1 == "" and a1 == "":
        t = float(t1)
        s = float(s1)
        u = float(u1)
        v = ((2 * s) - (u * t)) / t
        a = (v - u) / t
        v = round(v, dp)
        a = round(a, dp)
        print("\nFINAL VELOCITY = " + str(v) + " m/s^-1")
        if v != math.fabs(v):
            print("[Note: negative value means the velocity was in opposite direction "
                  "relative to the positive velocity]")
        print("\nACCELERATION = " + str(a) + " m/s^-2")
        if a != math.fabs(a):
            print("[Note: negative value means the acceleration was in opposite direction "
                  "relative to the positive velocity]")

    elif v1 == "" and t1 == "":
        a = float(a1)
        s = float(s1)
        u = float(u1)
        if (u * u) > (2 * a * s):
            v = math.sqrt((u * u) + (2 * a * s))
            t = (v - u) / a
            v = round(v, dp)
            t = round(t, dp)
            print("\nFINAL VELOCITY = " + str(v) + " m/s^-1")
            if v != math.fabs(v):
                print("[Note: negative value means the velocity was in opposite direction "
                      "relative to the positive velocity]")
            print("\nTIME = " + str(t) + " s")
            if t != math.fabs(t):
                print("[Note: this value for Time (t) is unrealistic. Time can not be negative]")
        elif (u * u) < (2 * a * s):
            v = cmath.sqrt((u * u) + (2 * a * s))
            v = round_complex(v)
            print("\nFINAL VELOCITY = " + str(v) + " m/s^-1")
            print("[Note: this value for Initial Velocity (u) is partially or completely Imaginary.]")
            t = (v - u) / a
            t = round_complex(t)
            print("\nTIME = " + str(t) + " s")
            print("[Note: this value for Time (t) is partially or completely Imaginary.]")

    elif a1 == "" and t1 == "":
        s = float(s1)
        v = float(v1)
        u = float(u1)
        t = (2 * s) / (v + u)
        a = (v - u) / t
        t = round(t, dp)
        a = round(a, dp)
        print("\nACCELERATION = " + str(a) + " m/s^-2")
        if a != math.fabs(a):
            print("[Note: negative value means the acceleration was in opposite direction "
                  "relative to the positive velocity]")
        print("\nTIME = " + str(t) + " s")
        if t != math.fabs(t):
            print("[Note: this value for Time (t) is unrealistic. Time can not be negative]")

    # With four or more values present, we need to check if they are consistent or not
    elif u1 == "":
        a = float(a1)
        t = float(t1)
        s = float(s1)
        v = float(v1)
        u_1 = v - (a * t)
        u_2 = ((2 * s) - (a * t * t)) / (2 * t)
        if u_1 == u_2:
            u_1 = round(u_1, dp)
            print("\nINITIAL VELOCITY = " + str(u_1) + " m/s^-1")
            if u_1 != math.fabs(u_1):
                print("[Note: negative value means the velocity was in opposite direction "
                      "relative to the positive velocity]")
        else:
            print("\n## variable information are inconsistent ##")

    elif v1 == "":
        a = float(a1)
        t = float(t1)
        s = float(s1)
        u = float(u1)
        v_1 = u + (a * t)
        v_2 = ((2 * s) / t) - u
        if v_1 == v_2:
            v_1 = round(v_1, dp)
            print("\nFINAL VELOCITY = " + str(v_1) + " m/s^-1")
            if v_1 != math.fabs(v_1):
                print("[Note: negative value means the velocity was in opposite direction "
                      "relative to the positive velocity]")
        else:
            print("\n## variable information are inconsistent ##")

    elif a1 == "":
        u = float(u1)
        t = float(t1)
        s = float(s1)
        v = float(v1)
        a_1 = (v - u) / t
        a_2 = ((v * v) - u) / (2 * s)
        if a_1 == a_2:
            a_1 = round(a_1, dp)
            print("\nACCELERATION = " + str(a_1) + " m/s^-2")
            if a_1 != math.fabs(a_1):
                print("[Note: negative value means the acceleration was in opposite direction "
                      "relative to the positive velocity]")
        else:
            print("\n## variable information are inconsistent ##")

    elif t1 == "":
        u = float(u1)
        a = float(a1)
        s = float(s1)
        v = float(v1)
        t_1 = (v - u) / a
        t_2 = (2 * s) / (v + u)
        if t_1 == t_2:
            t_1 = round(t_1, dp)
            print("\nTIME = " + str(t_1) + " s")
            if t_1 != math.fabs(t_1):
                print("[Note: this value for Time (t) is unrealistic. Time can not be negative]")
        else:
            print("\n## variable information are inconsistent ##")

    elif s1 == "":
        u = float(u1)
        t = float(t1)
        a = float(a1)
        v = float(v1)
        s_1 = ((v + u) / 2) * t
        s_2 = (u * t) + ((a * t * t) / 2)
        if s_1 == s_2:
            s_1 = round(s_1, dp)
            print("\nTRAVELED DISTANCE = " + str(s_1) + " m")
            if s_1 != math.fabs(s_1):
                print("[Note: negative value means the Distance is in the opposite direction relative to the direction "
                      "of positive vector(s)]")
        else:
            print("\n## variable information are inconsistent ##")

    else:
        u = float(u1)
        t = float(t1)
        a = float(a1)
        v = float(v1)
        s = float(s1)
        v_1 = u + (a * t)
        v_2 = math.sqrt((u * u) + (2 * a * s))
        if v_1 == v_2:
            print("\n## All the values are present and consistent ##")
        else:
            print("\n## variable information are inconsistent ##")

except ValueError:
    print("\n## Please enter values in numbers (integer & float), no symbol allowed ##")
except ZeroDivisionError:
    print("\n## The inputs lead to a division by zero, which means the values are incoherent ##")
