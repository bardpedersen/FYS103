import numpy as np
import matplotlib.pyplot as plt


def read_from_csv(file_name):
    list_of_all_numbers = []
    with open(file_name) as file:
        for line in file:
            line = line.split(";")

            line = [i.strip() for i in line]
            for number in line:
                list_of_all_numbers.append(int(number))
    return list_of_all_numbers


def calculate_mean(list_with_numbers):
    sum_numbers = sum(list_with_numbers)
    return sum_numbers/len(list_with_numbers)


def calculate_sd(list_with_numbers, mean_in_function):
    temp_list = []
    for number in list_with_numbers:
        sd1 = mean_in_function - number
        temp_list.append(sd1**2)

    sd1 = np.sqrt(sum(temp_list)/(len(list_with_numbers)-1))
    return sd1


def split_list_to_ten(list_with_numbers):
    list_with_four = [[], [], [], [], [], [], [], [], [], []]
    i = 0
    for number in list_with_numbers:
        list_with_four[i].append(number)
        i += 1
        if i == 10:
            i = 0
    return list_with_four


def mean_multiple_list(ten_list1):
    list_of_mean1 = []
    for i in range(len(ten_list1)):
        mean1 = calculate_mean(ten_list1[i])
        list_of_mean1.append(mean1)

    return list_of_mean1


print('\n')

# a)
list_number = read_from_csv('5_31.csv')
mean = calculate_mean(list_number)
sd = calculate_sd(list_number, mean)
print('Standard deviation is: ', sd, '\n')

# b)
ten_list = split_list_to_ten(list_number)
list_of_mean = mean_multiple_list(ten_list)
mean = calculate_mean(list_of_mean)
sd = calculate_sd(list_of_mean, mean)
print('Expected standard deviation is the same as sigma = 7.04/sqrt(4) = 3.52.\n',
      'The true value of standard deviation is:', sd)


# c)
bins = np.linspace(55.1, 90.7, 11)
plt.hist(list_number, bins=bins, histtype='step', edgecolor='green', linewidth=1)
plt.hist(list_of_mean*4, bins=bins, histtype='step', edgecolor='red', linewidth=1)
plt.legend(['List of all numbers', 'List of mean'])
plt.axvline(72.9, color='k', linestyle='dashed', linewidth=1.2)
plt.show()
