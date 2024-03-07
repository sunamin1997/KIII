Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def find_most_repeated_element(input_list):
...     element_count = {}
...     
...     for element in input_list:
...         if element in element_count:
...             element_count[element] += 1
...         else:
...             element_count[element] = 1
... 
...     most_common_element = max(element_count, key=element_count.get)
...     count = element_count[most_common_element]
... 
...     return most_common_element, count
... 
... if __name__ == "__main__":
...     # Example usage
...     input_list = [1, 2, 3, 4, 2, 2, 3, 3, 3, 5, 5, 5, 5]
...     
...     most_repeated_element, count = find_most_repeated_element(input_list)
... 
