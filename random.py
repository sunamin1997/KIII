Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
... 
... def generate_random_list(length, start_range, end_range):
...     random_list = [random.randint(start_range, end_range) for _ in range(length)]
...     return random_list
... 
... def main():
...     length = 5
...     start_range = 1
...     end_range = 10
... 
...     random_numbers = generate_random_list(length, start_range, end_range)
... 
...     print("Random List of Numbers:", random_numbers)
... 
... if __name__ == "__main__":
