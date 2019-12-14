from urllib.request import urlopen, hashlib

sha1_hash = input("Please enter a hash to crack: ")

list = ["polony", "test", "poop", "lice"]
for l in list:
    setpass = bytes(l, 'utf-8')

    hash_objectsha1 = hashlib.sha1(setpass)
    guess_pw_sha1 = hash_objectsha1.hexdigest()

    hash_object_md5 = hashlib.md5(setpass)
    guess_pw_md5 = hash_object_md5.hexdigest()

    if guess_pw_sha1 == sha1_hash:
        print(guess_pw_sha1)
        print("\n The password is:")
        print(setpass)

    if guess_pw_md5 == sha1_hash:
        print(guess_pw_md5)
        print("\n The password is:")
        print(setpass)
