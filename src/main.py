def calcular_medidas(base: int, altura: int) -> tuple[int, int]:
	"""
	Calcular el área y el perímetro del rectángulo
	
	:param base: Base solicitada
	:param altura: Altura solicitada
	
	:return: Devuelve una tupla con el área y el perímetro, en ese orden
	"""
	
	base = 0
	altura = 0
	
	area = base * altura
	perimetro = (base * 2) + (altura * 2)
	
	if base == 0 or altura == 0
		area == "ERROR!"
		perimetro == "ERROR!"
		
	return area, perimetro



def determinar_forma(base: int, altura: int) -> str
	"""
	Determinar la forma del cuadrado
	
	:param base: Base solicitada
	:param altura: Altura solicitada
	
	:return: Devuelve "cuadrado" si ambas medidas son iguales, "horizontal" si la base es mayor que la altura y "vertical" en el caso restante.
	"""

	forma = "Forma incorrecta!"
	if base == altura:
		forma = "cuadrado"
	elif base > altura:
		forma = "horizontal"
	else:
		forma = "vertical"
	
	if base == 0 or altura == 0
		forma == "ERROR!"
		
	return forma
	
	

main():
	""" Función principal del programa """
	print("CALCULADORA DE RECTÁNGULOS")
	print("-" * 15)
	
	base = int(input("Introduzca la base: ")
	altura = int(input("Introduzca la altura: ")
	
	medidas = calcular_medidas(base, altura)
	forma = determinar_forma(base, altura)
	
	print("")
	print(f"Forma: {forma}")
	print(f"Área: {medidas[0]} cm²")
	print(f"Perímetro: {medidas[1]} cm²")
	
	
	


if __name__ == "__main__":
	main()