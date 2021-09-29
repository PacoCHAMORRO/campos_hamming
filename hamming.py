# with open('dict.txt') as dictionary:
# 	dict_list = dictionary.read().splitlines() 

# print(dict_list)

# myStr = input('Ingresa la cadena: ')

# myStr.split()

# separada = myStr.split()
# print(separada)

# for palabra in separada:
# 	if (palabra in dict_list):
# 		print('si está')
# 	else:
# 		print('no está')
		

def hammingDistance(x, y):
    if type(x) and type(y)==str:
        if len(x)==len(y):
            hamming=0
            i = 0
            s1, s2 = [], []
            [[s1.append(ord(val))] for val in x] # the ord function returns the ASCII
	

            # equivalent of a letter
            [[s2.append(ord(val))] for val in y]
            for x in s1:
                if x!=s2[i]: # assumption, strings are of equal length
                    hamming+=1
                i+=1
            return hamming
        else:
            return "Strings not of equal length"

    elif type(x) and type(y)==int:
        return bin(x ^ y).count('1')
    else:
        return "Unknown format of inputs"
    # bin converts int to binary string
    # x^y is a logical operator which produces 0 when digits in corresponding positions match
    # and 1 if otherwise

protein_sequence1="hola"
protein_sequence2="gota"
protein_sequence2="[g]o[t]a"
protein_sequence2="[gota]"
print(hammingDistance(protein_sequence1,protein_sequence2))
print("There is a",
      int((len(protein_sequence1)-hammingDistance(protein_sequence1,protein_sequence2))/len(protein_sequence1)*100),
"% match between the 2 protein sequences")
