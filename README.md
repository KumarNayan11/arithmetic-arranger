> Format and display simple math problems vertically using Python.

# Arithmetic Arranger

This is a beginner Python project that formats arithmetic problems vertically and side-by-side, like students do in primary school. The project is part of the [freeCodeCamp Scientific Computing with Python](https://www.freecodecamp.org/learn/scientific-computing-with-python/) certification.

---

## 📌 Features

- Accepts a list of up to five arithmetic problems.
- Validates input (operator must be + or -, numbers must be digits, and max 4 digits).
- Returns the problems vertically aligned.
- Optional second argument to show answers.

---

## 🧪 Example Usage

```python
from Arithm_format import arithmetic_arranger

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))
```
---

### Output:
```
   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
  730     3799      88      172
```

---

## 🔒 Input Rules

Only + and - operators are allowed.

Operands must be numbers only.

Operands must be no more than four digits.

No more than five problems can be arranged at once.


---

### 🧠 What I Learned

- String manipulation and formatting  
- Input validation  
- Conditional logic  
- List construction and joining


---

## 📁 File Structure
```
arithmetic-arranger/
│
├── Arithm_format.py       # Main Python file (working code)
├── README.md              # Project description
```

---

## 🙋‍♂️ Author

Made with ❤️ by **Nayan**  

---

## 📝 License

This project is open-source and part of the freeCodeCamp curriculum.


