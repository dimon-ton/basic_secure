import hashlib

text = 'abc'

# create SHA256 object
sha_obj = hashlib.sha256()

# update sha_obj to input text into it
sha_obj.update(text.encode('utf-8'))

hashed_txt = sha_obj.hexdigest()

print(hashed_txt)