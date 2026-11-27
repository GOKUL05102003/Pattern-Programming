
<div align="center">

---

## 📌 About The Project

Pattern printing is one of the best ways to build a rock-solid foundation in:

- Nested loop mechanics (outer loops for rows, inner loops for columns/spaces)
- Mathematical and index manipulation
- Spatial reasoning and algorithmic thinking

This repository tracks my journey of uploading **at least one new pattern problem every day**, complete with multiple approaches (nested loops vs. string multiplication) and visual output examples.

---

## 📂 Repository Structure

```plaintext
Patterns/
│
├── Star-Pattern/                    # Star & symbol patterns
│   ├── LeftSideTriangle.py          # Day 01: Left-sided upright triangle
│   ├── LeftReverseTriangle.py       # Day 02: Inverted left-sided triangle
│   ├── LeftTriangleOutline.py       # Day 03: Hollow left-sided triangle outline
│   ├── LeftTriangleInvertedOutline.py # Day 04: Hollow inverted left-sided triangle outline
│   ├── RigthSideTriangle.py         # Day 05: Right-sided upright triangle
│   ├── RightInvertedTriangle.py     # Day 06: Inverted right-sided triangle
│   ├── RightTriangleOutline.py      # Day 07: Hollow right-sided triangle outline
│   └── RightTriangleInvertedOutline.py # Day 08: Hollow inverted right-sided triangle outline
│
├── Number-Pattern/                  # (Upcoming) Number triangles, Pascal, Floyd's
├── Alphabet-Pattern/                # (Upcoming) Character pyramids, letter matrices
└── Advanced-Pattern/                # (Upcoming) Hollow shapes, butterfly, spirals
```

---

## 📅 Daily Patterns Tracker

| Day | Pattern Name | Category | Code Link | Visual Preview |
|:---:|:---|:---:|:---:|:---|
| **01** | Left-Sided Triangle | Star | [`LeftSideTriangle.py`](./Star-Pattern/LeftSideTriangle.py) | `*`<br>`**`<br>`***` |
| **02** | Left Reverse Triangle | Star | [`LeftReverseTriangle.py`](./Star-Pattern/LeftReverseTriangle.py) | `***`<br>`**`<br>`*` |
| **03** | Left Triangle Outline | Star | [`LeftTriangleOutline.py`](./Star-Pattern/LeftTriangleOutline.py) | `*`<br>`**`<br>`* *`<br>`*  *`<br>`*****` |
| **04** | Inverted Left Triangle Outline | Star | [`LeftTriangleInvertedOutline.py`](./Star-Pattern/LeftTriangleInvertedOutline.py) | `*****`<br>`*  *`<br>`* *`<br>`**`<br>`*` |
| **05** | Right-Sided Triangle | Star | [`RigthSideTriangle.py`](./Star-Pattern/RigthSideTriangle.py) | `  *`<br>` **`<br>`***` |
| **06** | Right Inverted Triangle | Star | [`RightInvertedTriangle.py`](./Star-Pattern/RightInvertedTriangle.py) | `***`<br>` **`<br>`  *` |
| **07** | Right Triangle Outline | Star | [`RightTriangleOutline.py`](./Star-Pattern/RightTriangleOutline.py) | `    *`<br>`   **`<br>`  * *`<br>` *  *`<br>`*****` |
| **08** | Inverted Right Triangle Outline | Star | [`RightTriangleInvertedOutline.py`](./Star-Pattern/RightTriangleInvertedOutline.py) | `*****`<br>` *  *`<br>`  * *`<br>`   **`<br>`    *` |

---

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/GOKUL05102003/Pattern-Programming.git
cd Pattern-Programming
```

### 2. Common Run Commands

Run any pattern script directly using Python:

```bash
# General Syntax:
python <folder-name>/<file-name>.py

# Examples:
python Star-Pattern/LeftSideTriangle.py
python Star-Pattern/LeftReverseTriangle.py
python Star-Pattern/LeftTriangleOutline.py
python Star-Pattern/LeftTriangleInvertedOutline.py
python Star-Pattern/RigthSideTriangle.py
python Star-Pattern/RightInvertedTriangle.py
python Star-Pattern/RightTriangleOutline.py
python Star-Pattern/RightTriangleInvertedOutline.py
```

### 3. Provide Input

When prompted, enter the number of rows (e.g., `5`):

```text
Enter the no. of Rows: 5
```

---

## 💡 Logic Building Cheat Sheet

When solving any pattern problem, follow this 4-step framework:

1. **Rows (Outer Loop):** Count the total rows ($n$). Loop from `1` to `n` (or `n` down to `1` for reverse patterns).
2. **Spaces (Inner Loop 1):** Determine if spaces depend on the row index (e.g., $n - i$).
3. **Symbols / Values (Inner Loop 2):** Identify how characters change per line (e.g., boundary conditions `j == 1 or j == i or i == n` for outlines).
4. **New Line:** Print a line break after each row finishes printing.

---

## ⭐ Feedback & Support

- If you have any feedback, ideas, or suggestions, feel free to open an **Issue**!
- If you find this project helpful for your learning journey, please leave a **Star ⭐** to support the repository.

---

<div align="center">
  <sub>Made with ❤️ and Python. Happy Coding!</sub>
</div>
