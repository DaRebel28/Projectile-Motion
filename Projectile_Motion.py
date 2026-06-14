# John Burghardt
from math import pi, sqrt, sin, cos, asin, acos
a_y = 9.81
m = None
t = None
x = None
h = None
V = None
θ = None
unknowns = 0
while True :
    print("\033[H\033[2J",end="")
    print("Projectile Motion Calculator")
    print("↑   -----")
    print("|V↗   |h  ↘")
    print("|/θ   ↓a_y \\")
    print("·----------→·")
    print("m     ∆x    t")
    print("a_y = g = " + str(a_y) + " m/s^2")
    if isinstance(x, float) and isinstance(V, float) and x > V**2 / abs(a_y) :
        t = None
        x = None
        h = None
        V = None
        θ = None
        unknowns = 0
        continue
    if isinstance(x, float) and isinstance(V, float) and isinstance(θ, float) and not isinstance(t, float) :
        t = x / (V * cos(θ * pi / 180))
        continue
    elif isinstance(t, float) and isinstance(V, float) and isinstance(θ, float) and not isinstance(x, float) :
        x = t * V * cos(θ  * pi / 180)
        continue
    elif isinstance(x, float) and isinstance(t, float) and isinstance(θ, float) and not isinstance(V, float) :
        V = x / (t * cos(θ * pi / 180))
        continue
    elif isinstance(x, float) and isinstance(V, float) and isinstance(t, float) and not isinstance(θ, float) :
        θ = acos(x / (V * t))
        continue
    if isinstance(V, float) and isinstance(θ, float) and not isinstance(h, float) :
        h = V**2 * sin(θ  * pi / 180)**2 / a_y
        continue
    elif isinstance(h, float) and isinstance(θ, float) and not isinstance(V, float) :
        V = sqrt(h * a_y / sin(θ  * pi / 180))
        continue
    elif isinstance(h, float) and isinstance(V, float) and not isinstance(θ, float) :
        θ = asin(sqrt(h * a_y) / V)
        continue
    if isinstance(V, float) and isinstance(θ, float) and not isinstance(x, float) :
        x = V**2 * sin(2 * θ * pi / 180) / a_y
        continue
    elif isinstance(x, float) and isinstance(θ, float) and not isinstance(V, float) :
        V = sqrt(a_y * x / sin(2 * θ * pi / 180))
        continue
    elif isinstance(x, float) and isinstance(V, float) and not isinstance(θ, float) :
        θ = asin(a_y * x / V**2) / 2
        continue
    if m == None :
        m = input("Enter m: ")
        if m != "" :
            try :
                m = float(m)
                if m <= 0 :
                    m = None
            except :
                m = None
        continue
    elif m != "" :
        print("m = " + str(m) + " kg")
    if unknowns > 3 :
        t = None
        x = None
        h = None
        V = None
        θ = None
        unknowns = 0
        continue
    if t == None :
        t = input("Enter t: ")
        if t != "" :
            try :
                t = float(t)
                if t <= 0 :
                    t = None
            except :
                t = None
        else :
            unknowns += 1
        continue
    elif t != "" :
        print("t = " + str(t) + " s")
    if x == None :
        x = input("Enter ∆x: ")
        if x != "" :
            try :
                x = float(x)
                if x <= 0 :
                    x = None
            except :
                x = None
        else :
            unknowns += 1
        continue
    elif x != "" :
        print("∆x = " + str(x) + " m")
    if h == None :
        h = input("Enter h: ")
        if h != "" :
            try :
                h = float(h)
                if h <= 0 :
                    h = None
            except :
                h = None
        else :
            unknowns += 1
        continue
    elif h != "" :
        print("h = " + str(h) + " m")
    if V == None :
        V = input("Enter V: ")
        if V != "" :
            try :
                V = float(V)
                if V <= 0 :
                    V = None
            except :
                V = None
        else :
            unknowns += 1
        continue
    elif V != "" :
        print("V = " + str(V) + " m/s")
    if θ == None :
        θ = input("Enter θ: ")
        if θ != "" :
            try :
                θ = float(θ)
                if θ <= 0 :
                    θ = None
            except :
                θ = None
        else :
            unknowns += 1
        continue
    elif θ != "" :
        print("θ = " + str(θ) + "°")
    if not isinstance(h, float) and not isinstance(V, float) and not isinstance(θ, float) :
        t = None
        x = None
        h = None
        V = None
        θ = None
        unknowns = 0
        continue
    break