letter_frequency = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
random_coincidence = 0.0385
english_coincidence = 0.0667

def frequency(text):
        DECIMAL_ADJUST = 97 #adjust letter's decimal character to python's zero based list
        for char in text:
                if char.isalpha():
                pos = ord(char) - DECIMAL_ADJUST
                letter_frequency[pos] = letter_frequency[pos] + 1   

def phi_observed(text):
        observed_coincidence = 0
        for i in letter_frequency:
                coincidence = letter_frequency[i]
                if coincidence > 1:
                        observed_coincidence += (coincidence * (coincidence - 1))
    return observed_coincidence

def phi_random(comparisons, random_coincidence):
        return random_coincidence * comparisons

def phi_english(comparisons, english_coincidence):
        return english_coincidence * comparisons

def delta_index_of_coincidence(phi_observed, phi_random):
        return phi_observed / phi_random

print('Enter text to analyze: ')
text = input()
text_length = len(text)

comparisons = text_length * (text_length - 1)
frequency(text)

phi_r = phi_random(comparisons, random_coincidence)
phi_e = phi_english(comparisons, english_coincidence)
phi_o = phi_observed(text)
delta_ic = delta_index_of_coincidence(phi_o, phi_r)

for n,g in zip(letters, letter_frequency):
        print('{}: {}'.format(n, g))
print('Random coincidence factor (phi R): {}'.format(phi_r))
print('English coincidence factor (phi E): {}'.format(phi_e))
print('Observed coincidences (phi O): {}'.format(phi_o))
print('Delta Index of Coincidence (Delta IC): {}'.format(delta_ic))
print('The monographic phi test is a tool used to analyse ciphertexts by comparing letter repitions with that of the english language and a random distribution.')

if text_length < 50:
        print('Given the small sample size, results may have unreliable variance.')
if 50 <= text_length < 200:
        if 1.50 <= delta_ic <= 2.00:
                print('Given the sample size, the index of coincidence indicates the ciphertext uses a monoalphabetic encryption scheme. Shift cipher brute force and further frequency analysis is recommended.')
        elif 0.75 <= delta_ic <= 1.25:
                print('Given the sample size, the index of coincidence indicates the ciphertext uses a polyalphabetc encryption scheme. Deeper cryptanalysis may be necessary.')
        else:
                print('The text provided yielded unexpected results, a larger sample size may be necessary.')
if text_length >= 200:
        if 1.63 <= text_length <= 1.83:
                print('The index of coincidence indicates the ciphertext uses a monoalphabetic encryption scheme. Shift cipher brute force and further frequency analysis is recommended.')
        elif 0.90 <= text_length <= 1.10:
                print('The index of coincidence indicates the ciphertext uses a polyalphabetc encryption scheme. Deeper cryptanalysis may be necessary.')
        else:
                print('The text provided yielded unexpected results, a larger sample size may be necessary.')
        