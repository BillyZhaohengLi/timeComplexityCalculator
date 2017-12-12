import math;
def function(a):
    aaa = 0;
    for i in range(0,a):
        for j in range(0,a):
            for k in range(0,int(math.log(a,2))):
                aaa = aaa + 1;
    return aaa;
