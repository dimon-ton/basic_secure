# !pip install cryptography library

from cryptography.fernet import Fernet

# fernet algorithm two way
# create unique key
# you have to use the key below to decode
key = Fernet.generate_key()
print(key)


# create fernet object
f = Fernet(key)

text = 'สวัสดีจ้า วันนี้เรียนเรื่อง cryptography'
message = f.encrypt(text.encode('utf-8'))

print(f'{message}')

