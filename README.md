# Monographic_Phi_Test
Frequency Analysis and Index of Coincidence Test

The monographic phi test is designed to analyse a cipher text by comparing observed coincidenes of letter repitions with the expected coincidence for english plain text and random coincidence.

Given the english alphabet has 26 letters, there is a 1 / 26 or 3.85% chance to randomly choose the same letter twice from a sample of all english letters. However, in a sufficiently large sample size of english plaintext, there is approximately a 6.67% chance of randomly choosing the same letter twice. Comparing expected repitions with the actual observed repitions of the given text should indicate whether a cipher uses a monoalphabetic or polyalphabetic encryption scheme.

Randomly distributed letter frequencies should yield an index of coincidence of about 1.00, while English plaintext letter frequencies should yield an index of coincidence of about 1.73. Random distributions indicate a polyalphabetic scheme has been used, while distributions similar to enlgish plain text indicate a monoalphabetic scheme has been used.

This tool will take any sample size, however, texts of 50 characters or less will have unpredictable variance and should not be used. Texts of 50 to 200 characters will still have variance, but will yield more reliable results. Texts of greater than 200 characters should consistently yield reliable results. The greater a sample size is, the closer to an accurate distribution it should yield.
