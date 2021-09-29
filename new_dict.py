with open('new_dict.txt') as dictionary:
	dict_list = sorted(dictionary.read().splitlines())



with open('new_new_dict.txt', 'a') as diccionario:
	for palabra in dict_list:
		
		diccionario.write(palabra.lower() + '\n')