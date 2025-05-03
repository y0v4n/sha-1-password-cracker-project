import hashlib

with (
    open("top-10000-passwords.txt", "r", encoding="utf-8") as pw_txt,
    open("known-salts.txt", "r", encoding="utf-8") as sl_txt
):   
    passwords = [line.strip() for line in pw_txt if line.strip()]
    salts = [line.strip() for line in sl_txt if line.strip()]

def crack_sha1_hash(hash, use_salts = False):
    for password in passwords:
        if use_salts:
            for salt in salts:
                for variant in (salt + password, password + salt, salt + password + salt):
                    if hashlib.sha1(variant.encode()).hexdigest() == hash:
                        return password
        else:
            if hashlib.sha1(password.encode()).hexdigest() == hash:
                return password
    return "PASSWORD NOT IN DATABASE"
