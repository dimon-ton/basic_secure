
from cryptography.fernet import Fernet



# text and key from my friend
text = b'gAAAAABkx6tyYufGqYmua6XcmOHARA9FIySMQ4meBdR24bcb_mRkQctMR2HdLaoN4aZiplKNzLufTOvDBs9_yYf3gzGG6zXxlTLADL6M2UDDsJUhJXax4eh-LluKz_VK7NYzoGrrVgCehibDMnZeQJqM-e5jbA1zaEc9L3sGfgBs5fhXsAGIFnuR2-c8I1gKrVKmm1ya4rH4'
key = b'XwJAAn_iGzsBSWehVwmgoYOjI_46fR26UMxDVN4zNLk='

f = Fernet(key)
message = f.decrypt(text).decode('utf-8')

print(message)