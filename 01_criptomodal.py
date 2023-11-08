from cryptography.fernet import Fernet
import base64

chave_secreta = "#modalGR#GPTW#top#maiorEmpresaTecnologia#baixadaSantista"
chave_secreta_bytes = chave_secreta.encode()
hash_chave_secreta = Fernet.generate_key()
chave_fernet = Fernet(hash_chave_secreta)

# Método 1: AES
def cripto_aes(texto):
    texto_cripto = chave_fernet.encrypt(texto.encode())
    return texto_cripto

def descripto_aes(texto_cripto):
    texto = chave_fernet.decrypt(texto_cripto).decode()
    return texto

# Método 2: Outra técnica de criptografia (por exemplo, XOR)
def cripto_xore(texto):
    texto_cripto = ''.join([chr(ord(x) ^ ord(y)) for x, y in zip(texto, chave_secreta)])
    return texto_cripto.encode()

def descripto_xore(texto_cripto):
    texto_descripto = ''.join([chr(ord(x) ^ ord(y)) for x, y in zip(texto_cripto.decode(), chave_secreta)])
    return texto_descripto

# Método 3: Base64
def cripto_base64(texto):
    texto_cripto = base64.b64encode(texto.encode())
    return texto_cripto

def descripto_base64(texto_cripto):
    texto_descripto = base64.b64decode(texto_cripto).decode()
    return texto_descripto

# Exemplo de uso
senha_teste = input("Digite a senha: ")

# AES
senha_cripto_aes = cripto_aes(senha_teste)
print("Senha cripto (AES):", senha_cripto_aes)

senha_descripto_aes = descripto_aes(senha_cripto_aes)
print("Senha descripta (AES):", senha_descripto_aes)

# XOR
senha_cripto_xor = cripto_xore(senha_teste)
print("Senha cripto (XOR):", senha_cripto_xor)

senha_descripto_xor = descripto_xore(senha_cripto_xor)
print("Senha descripta (XOR):", senha_descripto_xor)

# Base64
senha_cripto_base64 = cripto_base64(senha_teste)
print("Senha cripto (Base64):", senha_cripto_base64)

senha_descripto_base64 = descripto_base64(senha_cripto_base64)
print("Senha descripta (Base64):", senha_descripto_base64)
