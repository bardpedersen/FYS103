import numpy as np


def poisson(my_1, nu):
    ans = np.e**(-my_1)*((my_1**nu)/np.math.factorial(nu))
    return ans


def chi_square(list1, list2):
    list_el = []
    for j in range(len(list1)):
        ans = list1[j]-list2[j]
        ans1 = ans**2/list2[j]

        list_el.append(ans1)
    return sum(list_el)


list_of_nu = [0, 1, 2, 3, 4, 5]
my = 3
list_to_ans = []
for number, i in enumerate(list_of_nu):
    list_to_ans.append((poisson(my, i)*100))

list_to_ans.append(100-sum(list_to_ans))
list_ans = [5, 19, 23, 21, 14, 12, 6]
result = chi_square(list_ans, list_to_ans)
print('x^2: ', result)
print('Df = 6')
print('x^2, tilde = ', result/6)
print('Ser i tabell og får at sansyligheten er mer enn 73%, det er derfor er '
      'dette tilnærmet forventet med poisson ')
