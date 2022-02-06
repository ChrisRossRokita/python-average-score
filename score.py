from stringprep import in_table_c6


firstScore = input('What is the first score?')

secondScore = input('What is the second score?')

thirdScore = input('What is the third score?')

fourthScore = input('What is the fourth score?')

fifthScore = input('What is the fifth score?')

averageScore = int(int(firstScore) + int(secondScore) + int(thirdScore) + int(fourthScore) + int(fifthScore)) / 5

print('The average score of the five tests is ' + str(averageScore) + '!' )