import hashlib
import re
import getpass

def check_password_strength(password):
    score = 0
    feedback = []

    # Comprimento
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("⚠️ Senha muito curta (mínimo recomendado: 12 caracteres).")

    # Maiúsculas
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("⚠️ Adicione letras maiúsculas.")

    # Minúsculas
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("⚠️ Adicione letras minúsculas.")

    # Números
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("⚠️ Adicione números.")

    # Caracteres especiais
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("⚠️ Adicione caracteres especiais (!@#$...).")

    return score, feedback

def generate_hashes(password):
    encoded = password.encode('utf-8')
    return {
        "MD5 (Inseguro)": hashlib.md5(encoded).hexdigest(),
        "SHA-256": hashlib.sha256(encoded).hexdigest(),
        "SHA-512": hashlib.sha512(encoded).hexdigest()
    }

def main():
    print("\n" + "="*50)
    print(" 🔐 VALIDADOR DE SENHAS E GERADOR DE HASHES")
    print("="*50 + "\n")

    # getpass oculta a senha enquanto o usuário digita no terminal
    password = getpass.getpass("Digite a senha para analisar: ")

    if not password:
        print(" Nenhuma senha fornecida.")
        return

    score, feedback = check_password_strength(password)

    print("\n[+] Análise de Força:")
    if score >= 5:
        print("  🟢 Nível de Força: FORTE / EXCELENTE")
    elif score >= 3:
        print("  🟡 Nível de Força: MÉDIO")
    else:
        print("  🔴 Nível de Força: FRACO")

    if feedback:
        print("\n[+] Recomendações de Melhoria:")
        for item in feedback:
            print(f"  {item}")

    print("\n[+] Hashes Gerados:")
    hashes = generate_hashes(password)
    for algo, hash_val in hashes.items():
        print(f"  • {algo:15}: {hash_val}")

    print("\n" + "="*50 + "\n")

if __name__ == "__main__":
    main()
