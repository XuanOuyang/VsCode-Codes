import math
import matplotlib.pyplot as plt
import pyautogui
import pydirectinput
import numpy as np

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
    plt.show()

def waaa():
    import matplotlib.pyplot as plt

    # Data
    volume = [10.0, 9.0, 8.0, 7.0, 6.0, 5.0, 4.0, 3.0, 2.0, 1.0]
    pressure = [1.203, 1.333, 1.504, 1.720, 1.998, 2.407, 3.010, 3.999, 6.011, 12.021]

    plt.figure(figsize=(8, 6))
    plt.plot(volume, pressure, marker='o', linestyle='-')
    plt.xlabel('Volume (L)')
    plt.ylabel('Pressure (atm)')
    plt.title('Pressure vs. Volume for Nitrogen Gas at 293 K')
    plt.grid(True)

    plt.show()
def is_even(n):
    if n % 2 == 0:
        print('its even')
        return True
    else: 
        print("its odd")
        return False
    
def multiples_of(n):
    print(f"{n} is a")
    if n % 1 == 0:
        print("multiple of 1")
    if n % 2 == 0:
        print("multiple of 2")
    if n % 3 == 0:
        print("multiple of 3")
    if n % 4 == 0:
        print("multiple of 4")

def print_mult():
    for n in [1,2,3,4,5,6,7,8,9,10]:
        multiples_of(n)

def season_check(month):
    season = ""
    if month == "jan"or"dec"or"feb":
        season = "summer"

    elif month == "mar"or"apr"or"may":
        season = "autumn"

    elif month == "jun" or "jul" or "aug":
        season = "spring"

    else:
        season = "not a month"

    print(season)
    return season

def test_season():
    season_check("jun")

def D_rays():
    import numpy as np
    bios = np.array (['dep','ass','depass'])
    #numpy arrays are fixed in size (num - py)
    wtf = np.array ([1,3,"tuesday",(3,8),49])


def wieght_of_molocu():
    import numpy as np
    molocul = np.array(["boron","carbon","sodium","calcium","iorn"])
    wieght = np.array([2.46,2.26,0.968,1.55,7.74]) 
    # seems like np cycles throughs the arrays when called
    print(molocul)
    print(120 * wieght)

def tttst():
    import numpy as np

    # Create NumPy arrays for Volts and Ohms
    volts = np.array([6.3, 4.2, 5.0, 1.1, 1.1, 5.9])
    ohms = np.array([100, 150, 220, 330, 470, 680])

    # Calculate the current using a single, whole-array operation
    current = volts / ohms

    # Print the result
    print("Volts:", volts)
    print("Ohms :", ohms)
    print("Current (Amps):", current)

# arrays and lists arrays are faster 
def asd():
    import numpy as np

    def magforce(v, B):
        Fx = v[1] * B[2] - v[2] * B[1]
        Fy = v[2] * B[0] - v[0] * B[2]
        Fz = v[0] * B[1] - v[1] * B[0]

        force_vector = np.array([Fx, Fy, Fz])
        force_magnitude = np.linalg.norm(force_vector)
        
        return force_magnitude

    # Test case
    result = magforce([0.1, 0.2, 0.3], [0.4, 0.5, 0.6])

    # Print the result, rounded to 5 decimal places
    print(round(result, 5))

    # Check with NumPy functions
    v = np.array([0.1, 0.2, 0.3])
    B = np.array([0.4, 0.5, 0.6])
    numpy_result = np.linalg.norm(np.cross(v, B))

    # Print the NumPy result, rounded to 5 decimal places
    print(round(numpy_result, 5))

# Generate xs using a for loop
xs = np.array([i * 1.111 for i in range(8)])

# Generate ys without using a loop
ys = np.full(8, 7.654)

# Perform element-wise addition without using a loop
result = xs + ys

# Define the pretty function
def pretty(vector):
    print(" ".join([f"{x:6.2f}" for x in vector]))

# Print the results using pretty

def pyAUTO():
    pyautogui.press('y')
    pydirectinput.leftClick()
    pydirectinput.press('w')

pyAUTO()