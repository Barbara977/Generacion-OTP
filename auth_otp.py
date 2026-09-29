import pyotp
import time
import qrcode

# Generar secreto unico por usuario
secreto = pyotp.random_base32()
totp = pyotp.TOTP(secreto)

# Generar OTP 
codigo = totp.now()
print("OTP actual:", codigo)


# Crear URI de aprovisionamiento 
uri = pyotp.totp.TOTP(secreto).provisioning_uri(
    name="usuario@example.com",
    issuer_name="MiServicioSeguro"
)
# Generar QR a partir de la URI
qr = qrcode.make(uri)
qr.save("otp_qr.png")  # Se guarda como imagen
print("QR generado: escanea otp_qr.png en Google Authenticator")


# Validar OTP 
codigo_usuario = input("Introduce tu OTP: ")
if totp.verify(codigo_usuario):
    print("OTP valido, acceso permitido")
else:
    print("OTP invalido, acceso denegado")
