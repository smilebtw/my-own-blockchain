from hashlib import sha256

# Hash de x * y deve terminar com 0. Logo hash(x*y) = "abc123...0"
x = 5
y = 0 # Nao sabemos este valor

while sha256(f'{x*y}'.encode()).hexdigest()[-1] != "0":
  y += 1

print(f"Solution y = {y}")