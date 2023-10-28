import math
import matplotlib.pyplot as plt

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

def fuck_around():
    simple_frac = 2.131224
    print("the complex fraction is {:.2f}".format(simple_frac))
    print()

def wtf_math():
    six = math.factorial(6) # factorios = 6 * 5 * 4 * 3 * 2 * 1 
    two = math.factorial(2) # factoreos are a number * by all smaller numbers till 1 so 2 would be 2 * 1
    four = math.factorial(4) # 4 * 3 * 2 * 1

    ans = math.factorial(6) / math.factorial(2) / math.factorial(4) # same function different way of writing it BETTER WAY

    quick = math.comb(6,2) # answer is 15 

    #plt.plot([0.1,0.9,2.0,3.0]) #unfinished 

    sin_of_5 = math.sin(0.5) # takes sin of 0.5 duhhhh

    omg_pie = math.pi # NOTE variable color is farker because they are not used in anywhere / repeated in anything

    # things to remember 
    square_root = math.sqrt(3.9)
    #cube_root = math.cbrt(28) # cube root
    exponent = math.exp(1e1 ** -1.25) # no idea what that is 
    logaritom = math.log10(999) # log base 10 
    degrees = math.degrees(6.283)
    tangent = math.tan(math.pi/2)
    
    rounding = math.round(math.pi,5)

    horiz = 80 * math.sin(2)

    next = math.nextafter(15,16)

def cubed(x):    
    cubing = x * x * x
    return cubing 
    
    #print(cubed(4)) # forgot about this do this 

def c2f(x):
    ans = (x * (9/5)) + 32
    return ans

def quadraitics(a,b,c,x):
    return(a * x ** 2) + (b * x) + c

def adds(a,b,c):
    return a + b + c 
    
def charge(voltage,resistance,capacitance,time):
    term = math.exp()

def bac_t():
    print("ab")
    print("a\tb") #\t = tab 

def lang_fam():
    print(len("whowhwoh long dick size huh how long is it len?")) # length of string = len

def loop_mag_math():
    pie = math.pi
    radians = 25 * pie/180 # 25 is degrees
    ans = 1 * 0.2 * (pie * (7.5/100)**2) * math.cos(radians)
    return ans # tab = 4 spaces 

def list_test():
    hour = [9.25, 11, 13.5, 15, 15.75]
    power = [2.54, 4.1, 1.21, 3.9, 4]
    plt.plot(hour, power)
    #plt.plot(power, hour)
    plt.xlabel('Decimal Hour in Day')
    plt.ylabel('Power (mW)')
    plt.title("Power versus Time")


list_test()