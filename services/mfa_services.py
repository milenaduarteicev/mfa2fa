
import pyotp

def generate_otp_secret():
    """Gera um segredo TOTP (usado pelo Google Authenticator)"""
    return pyotp.random_base32()

def generate_otp_url(user):
    """Gera a URL do QR code para o Google Authenticator"""
    totp = pyotp.TOTP(user.otp_secret)
    return totp.provisioning_uri(name=user.username, issuer_name="MyApp")

def verify_otp(user, otp):
    """Verifica se o código fornecido é válido"""
    totp = pyotp.TOTP(user.otp_secret)
    return totp.verify(otp)
