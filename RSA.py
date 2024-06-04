import random
import time
import os

try:
    import cowsay
except:
    os.system("pip3 install cowsay")
    
import cowsay

cowsay.cow('Hello, this is a simulation of the public-key \n cryptosystem RSA. ')
# Function to calculate the Greatest Common Divisor (GCD) of two numbers
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Function to calculate the modular inverse of 'a' modulo 'm'
def mod_inverse(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise Exception("Modular inverse does not exist")
    return x % m

# Function to calculate the extended GCD of two numbers
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x

# Function to check if a number is prime using the Miller-Rabin primality test
def is_prime(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for _ in range(k):
        a = random.randint(2, n - 2)
        if pow(a, n - 1, n) != 1:
            return False
    return True 

# Function to generate a prime number with a given number of bits
def generate_prime(bits):
    while True:
        num = random.getrandbits(bits)
        if is_prime(num):
            return num

# Function to generate a key pair (public key and private key) for encryption
def generate_keypair(bits):
    p = generate_prime(bits)
    q = generate_prime(bits)
    n = p * q
    phi = (p - 1) * (q - 1)

    while True:
        e = random.randint(2, phi - 1)
        if gcd(e, phi) == 1:
            break

    d = mod_inverse(e, phi)
    return (e, n), (d, n)

# Function to encrypt a message using the public key
def encrypt(public_key, plaintext):
    e, n = public_key
    cipher_text = [pow(ord(char), e, n) for char in plaintext]
    return cipher_text

# Function to decrypt a cipher text using the private key
def decrypt(private_key, cipher_text):
    d, n = private_key
    decrypted_text = ''.join([chr(pow(char, d, n)) for char in cipher_text])
    return decrypted_text

# Main function to execute the encryption and decryption process
def main():
    bits = int(input("Enter the number of bits for key generation: "))

    public_key, private_key = generate_keypair(bits)
    
    print("Generated public key (e, n):", public_key)
    print("Generated private key (d, n):", private_key)
    
    message = input("Enter a message to encrypt: ")
    
    start_encryption = time.time()  # Record the start time for encryption
    encrypted = encrypt(public_key, message)
    end_encryption = time.time()  # Record the end time for encryption
    
    print("Encrypted message:", encrypted)
    
    start_decryption = time.time()  # Record the start time for decryption
    decrypted = decrypt(private_key, encrypted)
    end_decryption = time.time()  # Record the end time for decryption
    
    print("Decrypted message:", decrypted)

    encryption_time = end_encryption - start_encryption
    decryption_time = end_decryption - start_decryption
    
    print("Encryption Time:", encryption_time, "seconds")
    print("Decryption Time:", decryption_time, "seconds")

if __name__ == "__main__":
    main()