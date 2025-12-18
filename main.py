import qrcode

def codigoGenerator(url, nombre):
    img = qrcode.make(url)
    img.save(f"{nombre}.png")

if __name__ == "__main__":
    url = input("Ingresa la url: ")
    nombre  = input("Ingresa el nombre deseado del qr (sin extensión): ")
    codigoGenerator(url, nombre)


