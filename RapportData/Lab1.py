"""
__version__ = "1.0"
__author__ = "Bård Pedersen"
__email__ = "bard.tollef.pedersen@nmbu.no"
"""

# Imports to make calculation and plotting
import numpy as np
import matplotlib.pyplot as plt
import decimal


# Function to read data from csv file
# Input is a csv file of values
# Returns two list, one for total decay chain and one for background decay chain
def read_from_csv(file_name):
    list_of_tot = []
    list_of_back = []
    with open(file_name) as file:
        for line in file:
            line = line.split(";")
            line = [k.strip() for k in line]
            list_of_tot.append(int(line[-1]))
            list_of_back.append(int(line[1]))

    return list_of_tot, list_of_back


# Function to calculate middle value based on list of values
# Input is a list of numbers used to calculate middle value
# Returns the middle value as float
def find_middle_value(list_of_numbers):
    n = len(list_of_numbers)
    number_freq = {}
    answer = 0
    for k, number_func in enumerate(list_of_numbers):
        try:
            number_freq[number_func] += 1
        except KeyError:
            number_freq[number_func] = 1

    for key_func, value_func in number_freq.items():
        answer += key_func * value_func

    return answer / n


# Function to calculate sigma based on normal distribution
# Input is a list of observed values and the middle value
# Returns the standard deviation as float
def sigma_norm(list_of_nu, my):
    list_to_ans = []
    for k, nu in enumerate(list_of_nu):
        ans = (nu - my) ** 2
        list_to_ans.append(ans)
    sigma = np.sqrt(sum(list_to_ans) / (len(list_of_nu) - 1))

    return sigma


# Function to calculate sigma based on normal distribution and middle value
# Input is a list of observed values and the middle value
# Returns the standard deviation as float
def sigma_norm_mid(sd, list_of_nu):
    ans = sd / np.sqrt(len(list_of_nu))
    return ans


# Function to calculate poisson distribution
# Input is a list of observed values and the middle value
# Returns the poisson distribution as dictionary, with value as key and number of times
# that value will accrue as value in percentage
def poisson(my_1, list_of_nu1):
    decimal.getcontext().prec = 100  # Number of decimal
    ans_dict = {}
    list_of_nu = list(range(min(list_of_nu1), max(list_of_nu1) + 1))
    for k, nu in enumerate(list_of_nu):
        ans = decimal.Decimal(np.e) ** decimal.Decimal(-my_1) * \
              ((decimal.Decimal(my_1) ** nu) / decimal.Decimal(np.math.factorial(nu)))
        ans_dict[nu] = float(ans)
    return ans_dict


# Function to calculate sigma based on poisson distribution
# Input is the middle value
# Returns the standard deviation as float
def sigma_poisson(my):
    return np.sqrt(my)


# Function to calculate chi-square test
# Input is two list, the observed data and the expected data
# Returns the chi-square value as float
def chi_square(observed_data, expected_data):
    list_el = []
    for k in range(len(observed_data)):
        ans = observed_data[k] - expected_data[k]
        ans1 = ans ** 2 / expected_data[k]
        list_el.append(ans1)

    return sum(list_el)


# Function to calculate only the source decay
# Input is four values, the middle value and the standard deviation for total decay,
# the middle value the standard deviation for background decay
# Returns two float numbers, the middle value and the standard deviation
def calculate_source_gamma(my_tot, sd_tot, my_back, sd_back):
    my_ans = my_tot - my_back
    sd_ans = np.sqrt(sd_tot ** 2 + sd_back ** 2)
    return my_ans, sd_ans


# Function to turn list into dictionary
# Input is a list with keys
# Returns dictionary of number of times a key occurs
def list_to_dict(total_list):
    dict_func = {}
    for k, number_funct in enumerate(total_list):  # list_number_tot
        try:
            dict_func[number_funct] += 1
        except KeyError:
            dict_func[number_funct] = 1
    return dict_func


if __name__ == '__main__':

    # Read csv data into to lists, one for total decay and one for background
    list_number_tot, list_number_back = read_from_csv('data.csv')

    # Middle value for total and background decay
    my1 = find_middle_value(list_number_tot)
    my2 = find_middle_value(list_number_back)

    # Standard deviation for total and background decay based on normal distribution
    sd_norm1 = sigma_norm(list_number_tot, my1)
    sd_norm2 = sigma_norm(list_number_back, my2)

    # Standard error for total and background decay based on normal distribution
    sd_mid1 = sigma_norm_mid(sd_norm1, list_number_tot)
    sd_mid2 = sigma_norm_mid(sd_norm2, list_number_back)

    # Standard deviation for total and background decay based on poisson distribution
    sd_pos1 = sigma_poisson(my1)
    sd_pos2 = sigma_poisson(my2)

    print('-------------------')
    print('Målinger bakgrunnstårling\n')
    print('Middelverdi =', my2, ' Standaravvik normal =', sd_norm2, 'Standarfeil = ', sd_mid2,
          'Standaravvik poisson =', sd_pos2)

    # Turn number of observation to dictionary with frequency of occurrence
    number_freq_observed = list_to_dict(list_number_back)

    # Calculate poisson distribution
    list_of_pos = poisson(my2, number_freq_observed.keys())
    for key in list_of_pos:
        list_of_pos[key] *= 200  # Turn percentage into number of times it will occur with
                                 # 200 readings
    number_freq_expected = list_of_pos

    # Sort dictonary
    myKeys = list(number_freq_observed.keys())
    myKeys.sort()
    number_freq_observed = {i: number_freq_observed[i] for i in myKeys}

    # Sum the last bins to get bin value over 5
    number_freq_observed[8] = number_freq_observed[8] + number_freq_observed[9] + \
        number_freq_observed[11] + number_freq_observed[12]
    del number_freq_observed[9]
    del number_freq_observed[11]
    del number_freq_observed[12]
    number_freq_expected[8] = number_freq_expected[8] + number_freq_expected[9] + \
        number_freq_expected[10] + number_freq_expected[11] + \
        number_freq_expected[12]
    del number_freq_expected[9]
    del number_freq_expected[10]
    del number_freq_expected[11]
    del number_freq_expected[12]

    # Calculate chi-squared
    x_squared = chi_square(list(number_freq_observed.values()), list(number_freq_expected.values()))
    print('x_squared =', x_squared)

    # Define number of degrees of freedom
    df = 7

    # Calculate chi-squared tilde
    x_tilde = x_squared / df
    print('x_tilde', x_tilde)

    # Plot observed background decay with poisson distribution
    width = 1
    plt.bar(number_freq_observed.keys(), number_freq_observed.values(),
            edgecolor='purple', color='None', label='Observerte desintegrasjoner')
    plt.bar(number_freq_expected.keys(), number_freq_expected.values(),
            edgecolor='orange', color='None', label='Forventet desintegrasjoner')
    plt.axvline(my2, color='k', ls='dashed', linewidth=1.2, label='Observert middelverdi')
    plt.xlabel('Antall desintegrasjoner')
    plt.ylabel('Antall ganger observert')
    plt.title('Antall målte desintegrasjoner bakgrunnstråling')
    plt.legend(loc='lower center')
    plt.show()

    print('-------------------')
    print('Målinger med strålekilden\n')
    print('Middelverdi =', my1, 'Standaravvik =', sd_norm1, 'Standaravik poisson =', sd_pos1)

    # Turn number of observation to dictionary with frequency of occurrence
    number_freq_observed1 = list_to_dict(list_number_tot)

    # Divide into bins to get each bin value over 5
    a = sorted(number_freq_observed1)
    bins = np.linspace(min(a), max(a), 20)
    list_with_bins_obs1 = []
    for i, number in enumerate(list(bins)):
        temp_value1 = 0
        for j, value in enumerate(number_freq_observed1.keys()):
            if bins[i] <= value <= bins[i + 1]:
                temp_value1 += number_freq_observed1[value]
            if i + 1 >= len(list(bins)):
                break
        list_with_bins_obs1.append(temp_value1)

    # Sum last and first bins to get bin value over 5
    list_with_bins_obs1[-5] = list_with_bins_obs1[-5] + list_with_bins_obs1[-4] + \
        list_with_bins_obs1[-3] + list_with_bins_obs1[-2] + \
        list_with_bins_obs1[-1]
    list_with_bins_obs1[1] = list_with_bins_obs1[1] + list_with_bins_obs1[0]
    list_with_bins_obs1 = list_with_bins_obs1[1:-4]
    bins = bins[1:-4]

    # Plot the total decay
    plt.bar(bins, list_with_bins_obs1, width=10, linewidth=2, label='Observerte desintegrasjoner')
    plt.title('Antall målte desintegrasjoner totalt')
    plt.axvline(my1, color='k', linestyle='dashed', linewidth=1.2, label='Middelverdi')
    plt.xlabel('Antall desintegrasjoner')
    plt.ylabel('Antall ganger observert')
    plt.legend(loc='lower center')
    plt.show()

    print('-------------------')
    print('Måling kun stråling\n')

    # Calculate the decay of only source
    source_my, source_sd = calculate_source_gamma(my1, sd_mid1, my2, sd_mid2)
    print('Middelverdi =', source_my, 'Standarfeil', source_sd)
    print('-------------------')
