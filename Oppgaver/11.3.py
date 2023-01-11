import numpy as np

sample = 5*10**19
prob_samp = 3*10**(-20)

# a)
my = sample * prob_samp
print('a) ', my)

# b)
list_of_nu = [0, 1, 2, 3]


def poisson(my_1, nu):
    ans = np.e**(-my_1)*((my_1**nu)/np.math.factorial(nu))
    return ans


list_to_ans = []
for number, i in enumerate(list_of_nu):
    list_to_ans.append((poisson(my, i)*100))

print('b) ', list_to_ans)


# c)
prob_3_or_lower = sum(list_to_ans)
prob4_higher = 100-prob_3_or_lower
print('c) ', prob4_higher)
