# 99乘法表
# range(10)=range(1,10)
# list(range(1,10)) = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# for i in range(1,10):
#     for j in range(1,i + 1):
#         print("%sx%s=%s" % (j,i,i*j),end='\t')
#     print()

def mtable(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print("%sX%s=%s" %(j,i,i*j),end='\t')
        print()

mtable(9)