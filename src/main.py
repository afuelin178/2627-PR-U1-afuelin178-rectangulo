def calcular_medidas(base: int, altura: int) -> tuple[int, int]:
	"""
	Calcular el área y el perímetro del rectángulo
	
	:param base: Base solicitada
	:param altura: Altura solicitada
	
	:return: Devuelve una tupla con el área y el perímetro, en ese orden
	"""

	area: int = base * altura
	perimetro: int = (base * 2) + (altura * 2)
	
		
	return area, perimetro



def determinar_forma(base: int, altura: int) -> str:
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
		
	return forma
	
	

def main():
	""" Función principal del programa """
	print("CALCULADORA DE RECTÁNGULOS")
	print("-" * len("CALCULADORA DE RECTÁNGULOS"))
	
	base: int = int(input("Introduzca la base: "))
	altura: int = int(input("Introduzca la altura: "))

	if base <= 0 or altura <= 0:
		print("ERROR!")
	else:
		medidas = calcular_medidas(base, altura)
		forma = determinar_forma(base, altura)
		print("")
		print(f"Forma: {forma}")
		print(f"Área: {medidas[0]} cm²")
		print(f"Perímetro: {medidas[1]} cm²")
	
	

if __name__ == "__main__":
	main()