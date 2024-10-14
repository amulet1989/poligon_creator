# Conversor de coordenadas custom


def convertir_coord(x, y, xmax=1024, ymax=1024, escala=89.1):
    xout = x / escala
    yout = (ymax - y) / escala

    return (xout, yout), (x, ymax - y)
