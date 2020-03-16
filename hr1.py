string1 = 'ghiop'
string1_ascii = [103, 104, 105,111,112]
string1_r = len(string1)
string1_reversed = string1[string1_r::-1]
string2 = 'poihg'
string2_ascii = [112,111,105,104,103]

string1_abs = [1,1,6,1]
string2_abs = [1,6,1,1]

if string1_abs == string2_abs:
    print('funny')
else:
    print('not funny')

