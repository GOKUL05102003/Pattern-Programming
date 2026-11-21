<div align="center">

# Python Daily Pattern Programming

**A curated daily collection of pattern printing challenges to master loops, logic, and problem-solving in Python.**

<p align="center">
  <img src="https://img.shields.io/badge/Language-Python%203.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Badge" />
  <img src="https://img.shields.io/badge/Skill-Problem%20Solving-FFA116?style=for-the-badge&logo=leetcode&logoColor=white" alt="Problem Solving Badge" />
  <img src="https://img.shields.io/badge/Challenge-Daily%20Uploads-2ea44f?style=for-the-badge&logo=github&logoColor=white" alt="Daily Badge" />
  <img src="https://img.shields.io/badge/Status-Active-blue?style=for-the-badge" alt="Status Badge" />
</p>

[Browse Patterns](#-daily-patterns-tracker) • [Folder Structure](#-repository-structure) • [How to Run](#-how-to-run) • [Logic Cheat Sheet](#-logic-building-cheat-sheet)

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
├── Star-Pattern/          # Pyramids, triangles, diamonds, crosses
```

---

## 📅 Daily Patterns Tracker

| Day | Pattern Name | Category | Code Link | Visual Preview |
|:---:|:---|:---:|:---:|:---|
| **01** | Left-Sided Triangle | Star | [`LeftSideTriangle.py`](./Star-Pattern/LeftSideTriangle.py) | `*`<br>`**`<br>`***` |

---

## 🚀 How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/Python-Patterns.git
   cd Python-Patterns
   ```

2. **Run any pattern file:**
   ```bash
   python Star-Pattern/LeftSideTriangle.py
   ```

3. **Enter the requested row count** when prompted.

---

## 💡 Logic Building Cheat Sheet

When solving any pattern problem, follow this 4-step framework:

1. **Rows (Outer Loop):** Count the total rows ($n$). Loop from `1` to `n` (or `0` to `n-1`).
2. **Spaces (Inner Loop 1):** Determine if spaces depend on the row index (e.g., $n - i$).
3. **Symbols / Values (Inner Loop 2):** Identify how characters change per line (e.g., $2i - 1$, $i$, etc.).
4. **New Line:** Print a line break after each row finishes printing.

---

## ⭐ Feedback & Support

- If you have any feedback, ideas, or suggestions, feel free to open an **Issue**!
- If you find this project helpful for your learning journey, please leave a **Star ⭐** to support the repository.

