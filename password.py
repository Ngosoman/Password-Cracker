import time

password = input("Enter your password: ")
start = time.time()
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]{}|;:,.<>?/`~ '
guess = []
for val in range(5):
    a = [i for i in chars]
    for y in range(val):