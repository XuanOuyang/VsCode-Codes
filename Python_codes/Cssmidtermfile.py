import random
def formatting():

    # formatting
    print("hello",208,"i love you")
    # it can take variables also 
    name = "jhonny"
    age = 123
    print(name,age) # this way leaves space between each item
    # or you can do it this way

    print(f"hello {name}") # no built in space
    #len = length 

    print(f"hello {name} your name is {len(name)} letters long")
    f_test = 3.2131

    print(f"{f_test:10f}") # the format goes from f tells that it is function then "" to be a string {} for function inside f_test is the variable :10f means float 
    # so it is 10 spaces(infront) and put f_test as a float

    print(f'{f_test:.0f}') # . ____ means how many decimal places

    tiny = 1.23e-21
    huge = 1.23e+21

    print(f"{tiny:25.2f}") #small numbers don't have nice outputs
    print(f"{huge:25.2f}") #large numbers don't have large outputs

    print(f"{tiny:25.2e}")  #e notations work better (are scientific notations)
    print(f"{huge:25.2e}") 

    # you can add two variables together
    number1 = 3
    number2 = 4
    print(f"three plus four is {number1 + number2}")
    print(f"{number2=}") # if you put the variable infront of a = then it shows its result 

    #you can store funtions in vaiables

    text = f"{number2:,}"

    print("welcome to seattle")
    print(f"welcome to seattle")#same things as normal
    print(text)

    print(3 * "\n")

def tuples(): # tuples are immutable lists meaning you can not change them, but they function the same as lists
              # so you can directly make them lists then make changes
    my_list = [3, 5, 2, 9]# lists are in [] brackets square brackets
    print(my_list)

    my_tuple = (3, 5, 2, 9)# tuples are in () curved brackets
    print(my_tuple)

    my_list = my_list + [99, 100]
    print(my_list)
    my_tuple = my_tuple + (99, 100)
    print(my_tuple)
    print(my_list[1:3])
    print(my_tuple[1:3])
    [3, 5, 2, 9]
    (3, 5, 2, 9)
    [3, 5, 2, 9, 99, 100]
    (3, 5, 2, 9, 99, 100)
    [5, 2]
    (5, 2)

    tupular = ("blue","red","yellow","purple")
    print(tupular)

    p_ratios = (0.334, 0.331, 0.355, 0.32, 0.331,)
    print("normal")
    print(p_ratios)

    print("only these 3")
    print(p_ratios[1:4])

    # to change tuple values you change it to a list then change it back so 
    lis = list(p_ratios)
    lis[3] = .42
    p_ratios = tuple(lis)
    print("changed value")
    print(p_ratios)

    print("reversed")
    print(p_ratios[::-1]) # print it reversed

    ist = list(p_ratios)
    ist = ist + [0.303]
    p_ratios = tuple(ist)
    print("added item")
    print(p_ratios) # why am i not seeing an added item?


def build_a_plot():
    import matplotlib.pyplot as plt
    hoes = [1,2,3,4,5,6,7]
    ate =  [5,9,12,0,0,1,3]
    plt.plot(hoes,ate,linewidth=3,marker='*',markersize=15,color="red")
    plt.xlabel("amount of hoes")
    plt.ylabel("how much dick eaten")
    plt.title("hoes per dick")
    plt.show()
    #note has alot of shortcuts and variables I.E pain in the ass

def f_around():
    import FirstStart
    four_x_ten = FirstStart.quickCalc(4,"*",10)

def listings():
    lst = [2,3,5,6,8,1] # index starts at 0
    print(lst)
    print(lst[2:6:1]) # [start:stop:step]
    # start = index started at, stop = index stopped at, step = how many at a time
    # you can make it read every other index
    print(lst[::2])
    #reverse it 
    print(lst[::-1])
    #empty no rules 
    print(lst[::]) # also same with lst[:6]

def foing():
    matting = 129385710928375921734912739842
    print(matting)

    print(f'the number is {matting:12.0f}') #.0 means no decimals
    print(f'e notation/ scientific notation {matting:12e}')

def __what__():
    print("how is this allowed")



print(3 * "\n") # what?
#>>>>>>>>>>>>>>

#foing()
#listings()
#f_around()
#build_a_plot()
#tuples()
#formatting()

#>>>>>>>>>>>>>>
print("\n\n\n\n\n")
