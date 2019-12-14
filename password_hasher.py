import hashlib
import bcrypt

password = input("Enter a password to hash:  ")
print("\n SHA1 \n")
for i in range(1):
    setpass = bytes(password, 'utf-8')
    hash_object = hashlib.sha1(setpass)
    guess_pw = hash_object.hexdigest()
    print(guess_pw)
print("\n MD5 \n")
for i in range(1):
    setpass = bytes(password, "utf-8")
    hash_object = hashlib.md5(setpass)
    guess_pw = hash_object.hexdigest()
    print(guess_pw)
print("\n BCRYPT \n")
for i in range(1):
    hashed = bcrypt.hashpw(setpass, bcrypt.gensalt(10))
    print(hashed)
