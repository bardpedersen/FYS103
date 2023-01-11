import numpy as np

# a)
print('a) standard deviation for my=9 is sqrt(9) = 3')


# b)
my = 9
list_of_nu = [7, 8, 9, 10, 11]


def poisson(my_1, nu):
    ans = np.e**(-my_1)*((my_1**nu)/np.math.factorial(nu))
    return ans


list_to_ans = []
for number, i in enumerate(list_of_nu):
    list_to_ans.append((poisson(my, i)*100))

print('b) ', list_to_ans)

# c)
print('c) prob for 1 sd away is the same as less than 7 or larger than 12 which is: ',
      100-sum(list_to_ans))

# d)
print('d) since the percentage is 40% i dont doubt that the my=9')
