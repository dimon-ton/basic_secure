import hashlib

# SHA256 --> one way

h = hashlib.new('SHA256')

password = 'loong999'

h.update(password.encode())

password_hash = h.hexdigest()

print(password_hash)



# other way --> base64