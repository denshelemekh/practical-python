# bounce.py
#
# Exercise 1.5

bounce = height = 100  # Meters
bounce_back_rate = 3 / 5

for i in range(10):
    bounce *= bounce_back_rate
    print(i + 1, round(bounce, 4))
