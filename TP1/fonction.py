def Puissance_2(nombreA, nombreB):

	if type(nombreA) == int and type(nombreB) == int:
		x=nombreA**nombreB
		return(x)
	else:
		raise TypeError ("only integers are allowed")
