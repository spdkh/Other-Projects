s = 'BANANA'# input()
Stuart = 0
Kevin = 0
vowels = 'AEIOU'
for i in range(len(s)):
    if s[i] in vowels:
        Kevin +=  len(s[i:])
    else:
        Stuart += len(s[i:])
print(Kevin, Stuart)
##if __name__ == '__main__':
##    s = input()
##    minion_game(s)
