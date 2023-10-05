def should_have_used_my_head ():
    #what makes good variable names 

    # cant start with a number
    # no &^!%@ characters 
    # Case is important/ checked count as different variables 
    total = 3
    Total = 5
    #7otal = error
    #python uses Snake case I.E speed_of_light 
    print(total + Total)
    # round function will round to __
    speed = 30 * 123 / 0.88
    rounded_speed = round(speed,2)
    print(speed)
    print(round(speed,2))

    pi = 3.141592653589
    print(round(pi,2))
    print(round(pi,6))

    pies = 22/7
    print(pies)

def head_used():
    a = 3.1
    # m = pythag(a,-4.9) there was an error must need to import pythag

def energy_calculation():
    mass = 2.7
    g = 9.8
    energy = mass * g * 3.65
    print(round(energy,4)) # it doesnt include 0

def testing_e_notation():
    x = 1.05 * (10 ** -34)
    y = 2.99 * (10 ** 8)
    print(y)
def grav_between_earth_moon():
    G = 6.67 * 10 ** -11
    Me = 6e24 # got e to work finally 
    Mm = 7.2 * 10 ** 22
    R = 3.84 * 10 ** 8

    F = G * Me * Mm / R ** 2
    print(F)

def earth_to_moon():
    radius_km = 6371

    circumference_km = 2 * 3.14 * radius_km

    surface_area_sq_km = 4 * 3.14 * radius_km ** 2

    volume_cubic_km = (4/3) * 3.14 * radius_km ** 3

    print("The Earth's Circumference is approximately {:.2f} km.".format(circumference_km))
    print("The Earth's Surface Area is approximately {:.2f} square km.".format(surface_area_sq_km))
    print("The Earth's Volume is approximately {:.2f} cubic km.".format(volume_cubic_km))

earth_to_moon()


