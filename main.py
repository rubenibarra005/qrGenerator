import qrcode

def codigoGenerator(url, nombre, color_fondo="white", color_code= "black"):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color=color_code, back_color=color_fondo)
    img.save(f"{nombre}.png")

if __name__ == "__main__":
    url = input("Ingresa la url: ")
    nombre  = input("Ingresa el nombre deseado del qr (sin extensión): ")
    colores = input("¿Deseas personalizar los colores? (s/n): ").lower()
    if colores == 's':
        color_fondo = input("Ingresa el color de fondo (nombre o código hex): ")
        color_code = input("Ingresa el color del código QR (nombre o código hex): ")
        codigoGenerator(url, nombre, color_fondo, color_code)
    else:
        codigoGenerator(url, nombre)

