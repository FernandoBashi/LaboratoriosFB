# Fernando Barrientos 1226323
print("Fernando Barrientos - 1226323")  

# Solicitar al usuario que ingrese una cantidad en metros
metros = float(input("Ingrese una cantidad en metros: "))

# Conversiones de unidades
# Constantes de conversión
MILLA_A_KM = 1.60934
KM_A_METROS = 1000
METRO_A_PIES = 3.28084
PIE_A_PULGADAS = 12

# Calculando conversiones
millas = metros / (KM_A_METROS * MILLA_A_KM)
kilometros = metros / KM_A_METROS
pies = metros * METRO_A_PIES
pulgadas = pies * PIE_A_PULGADAS

# Mostrando resultados
print("Resultado:")
print(f"Millas: {millas}")
print(f"Kilómetros: {kilometros}")
print(f"Pies: {pies}")
print(f"Pulgadas: {pulgadas}")

# Solicitar otra cantidad en metros para conversiones en el sistema inglés
metros_ingles = float(input("\nIngrese otra cantidad en metros para la conversión al sistema inglés: "))

# Conversiones al sistema inglés
# Constantes de conversión al sistema inglés
METRO_A_YARDAS = 1.09361
METRO_A_PULGADAS_INGLES = METRO_A_PIES * PIE_A_PULGADAS

# Calculando conversiones al sistema inglés
yardas = metros_ingles * METRO_A_YARDAS
pies_ingles = metros_ingles * METRO_A_PIES
pulgadas_ingles = metros_ingles * METRO_A_PULGADAS_INGLES

# Mostrando resultados del sistema inglés
print("Resultado:")
print(f"Yardas: {yardas}")
print(f"Pies: {pies_ingles}")
print(f"Pulgadas: {pulgadas_ingles}")