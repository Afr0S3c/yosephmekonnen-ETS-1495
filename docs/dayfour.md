# String Methods

This script demonstrates basic Python string methods in a simple way.

## Usage
Clone the repository and run the script:

```sh
python example.py
```


### 1. `swapcase()`
Converts uppercase letters to lowercase and vice versa.
```python
text = "hello friend"
print(text.swapcase())  
```

### 2. `find()`
Finds the first occurrence of a substring. Returns `-1` if not found.
```python
print(text.find("hello"))  
print(text.find("friend")) 
```

### 3. Indexing (Incorrect in Original Script)
The script mistakenly uses `text[1]` instead of `text.index("character")`.
```python
print(text[1])  
```
✅ **Correction if you meant to use `index()`:**
```python
print(text.index("e"))  # Finds the position of "e"
```

### 4. `startswith()`
Checks if a string starts with a specific substring.
```python
print(text.startswith("hello"))   # Output: True
print(text.startswith("friend"))  # Output: False
```

## Running the Script
Save the code as `example.py` and run:
```sh
python example.py
```


