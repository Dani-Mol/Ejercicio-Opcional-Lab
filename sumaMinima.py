
def caminoSumaMin(matriz):
    # Verificamos si la cuadrícula está vacía
    if not matriz:
        return 0

    filas = len(matriz)
    columnas = len(matriz[0])

    # Creamos una matriz de dp (dinámica) para almacenar las sumas mínimas
    dp = [[0] * columnas for _ in range(filas)]

    # El punto de partida es la celda (0,0)
    dp[0][0] = matriz[0][0]

    # Llenamos la primera fila (solo puede ir hacia la derecha por regla)
    for i in range(1, columnas):
        dp[0][i] = dp[0][i - 1] + matriz[0][i]

    # Llenamos la primera columna (solo puede ir hacia abajo por regla)
    for i in range(1, filas):
        dp[i][0] = dp[i - 1][0] + matriz[i][0]

    # Llenar el resto de la tabla dp para checar la suma mínima
    for i in range(1, filas):
        for j in range(1, columnas):
            dp[i][j] = matriz[i][j] + min(dp[i - 1][j], dp[i][j - 1])

    # La celda final contiene la suma mínima del camino
    return dp[filas - 1][columnas - 1]

