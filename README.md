<div align="center">

<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="Python Logo" width="75" height="75" />

# Python Daily Pattern Programming

**A curated daily collection of pattern printing challenges to master loops, logic, and problem-solving in Python.**

<p align="center">
  <img src="https://img.shields.io/badge/Language-Python%203.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Badge" />
  <img src="https://img.shields.io/badge/Skill-Problem%20Solving-FFA116?style=for-the-badge&logo=leetcode&logoColor=white" alt="Problem Solving Badge" />
  <img src="https://img.shields.io/badge/Challenge-Daily%20Uploads-2ea44f?style=for-the-badge&logo=github&logoColor=white" alt="Daily Badge" />
  <img src="https://img.shields.io/badge/Status-Active-blue?style=for-the-badge" alt="Status Badge" />
</p>

[Browse Patterns](#-daily-patterns-tracker) • [Repository Structure](#-repository-structure) • [How to Run](#-how-to-run) • [Logic Cheat Sheet](#-logic-building-cheat-sheet)

</div>

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
├── Star-Pattern/                  # Star & symbol patterns
│   ├── LeftSideTriangle.py        # Day 01: Left-sided upright triangle
│   └── LeftReverseTriangle.py     # Day 02: Inverted left-sided triangle
│
├── Number-Pattern/                # (Upcoming) Number triangles, Pascal, Floyd's
├── Alphabet-Pattern/              # (Upcoming) Character pyramids, letter matrices
└── Advanced-Pattern/              # (Upcoming) Hollow shapes, butterfly, spirals
```

---

## 📅 Daily Patterns Tracker

| Day | Pattern Name | Category | Code Link | Visual Preview |
|:---:|:---|:---:|:---:|:---|
| **01** | Left-Sided Triangle | Star | [`LeftSideTriangle.py`](./Star-Pattern/LeftSideTriangle.py) | `*`<br>`**`<br>`***` |
| **02** | Left Reverse Triangle | Star | [`LeftReverseTriangle.py`](./Star-Pattern/LeftReverseTriangle.py) | `***`<br>`**`<br>`*` |

---

## 🚀 How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/Python-Patterns.git
cd Python-Patterns
```

### 2. Common Run Commands
Run any pattern script directly using Python:

```bash
# General Syntax:
python <folder-name>/<file-name>.py

# Examples:
python Star-Pattern/LeftSideTriangle.py
python Star-Pattern/LeftReverseTriangle.py
```

### 3. Provide Input
When prompted, enter the number of rows (e.g., `5`):
```text
enter no. of Rows: 5
```

---

## 💡 Logic Building Cheat Sheet

When solving any pattern problem, follow this 4-step framework:

1. **Rows (Outer Loop):** Count the total rows ($n$). Loop from `1` to `n` (or `n` down to `1` for reverse patterns).
2. **Spaces (Inner Loop 1):** Determine if spaces depend on the row index (e.g., $n - i$).
3. **Symbols / Values (Inner Loop 2):** Identify how characters change per line (e.g., $2i - 1$, $i$, etc.).
4. **New Line:** Print a line break after each row finishes printing.

---

## ⭐ Feedback & Support

- If you have any feedback, ideas, or suggestions, feel free to open an **Issue**!
- If you find this project helpful for your learning journey, please leave a **Star ⭐** to support the repository.

---

<div align="center">
  <sub>Made with ❤️ and Python. Happy Coding!</sub>
</div>
