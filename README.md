# Partial Derivatives – Mathematical Animation

An educational mathematical animation created using **Python and Manim Community** to explain the concept of partial derivatives through visualisation and step-by-step mathematical derivations.

## 🎯 Project Overview

This project demonstrates how partial derivatives measure the rate of change of a multivariable function with respect to one variable while keeping the other variable constant.

The animation uses the function:

\[
f(x,y)=x^2+2y^2
\]

It visualises the function as a 3D surface and explains how the surface changes along the x-direction and y-direction.

## 📚 Concepts Covered

- Introduction to functions of two variables
- 3D visualisation of a multivariable function
- Understanding partial derivatives geometrically
- Partial differentiation with respect to x
- Partial differentiation with respect to y
- Step-by-step mathematical derivation
- Evaluating partial derivatives at a given point

## 🧮 Mathematical Explanation

Given:

\[
f(x,y)=x^2+2y^2
\]

**Partial derivative with respect to x:**

While treating y as a constant:

\[
\frac{\partial f}{\partial x}=2x
\]

**Partial derivative with respect to y:**

While treating x as a constant:

\[
\frac{\partial f}{\partial y}=4y
\]

At the point \((1,1)\):

\[
f(1,1)=3
\]

\[
\frac{\partial f}{\partial x}=2
\]

\[
\frac{\partial f}{\partial y}=4
\]

## 🛠️ Technologies Used

- **Python** – Programming language
- **Manim Community** – Mathematical animation framework
- **LaTeX** – Mathematical equations and notation
- **Visual Studio Code** – Development environment

## 📁 Project Structure

```text
maths_video/
│
├── code/
│   └── partial_derivatives.py
│
├── media/
│   └── Generated animation assets
│
├── .gitignore
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/sarthakjaiswal2006/maths_animated_video.git
```

### 2. Navigate to the project directory

```bash
cd maths_animated_video
```

### 3. Create a virtual environment

```bash
python3 -m venv venv
```

### 4. Activate the environment

**macOS / Linux:**

```bash
source venv/bin/activate
```

### 5. Install Manim

```bash
pip install manim
```

Make sure the required LaTeX dependencies are installed for mathematical equation rendering.

### 6. Run the animation

```bash
manim -pql code/partial_derivatives.py PartialDerivatives
```

For high-quality rendering:

```bash
manim -pqh code/partial_derivatives.py PartialDerivatives
```

## 🎬 Output

The project generates an animated explanation of partial derivatives, combining mathematical equations and visual demonstrations to make the concept easier to understand.

The rendered video is available in the Manim-generated media directory.

## 🎓 Academic Context

**Subject:** M3 – Mathematics III  
**Topic:** Partial Derivatives  
**Project Type:** Mathematical Animation  
**Purpose:** Visual and conceptual understanding of partial differentiation.

## 👨‍💻 Author

**Sarthak Jaiswal**

GitHub: [@sarthakjaiswal2006](https://github.com/sarthakjaiswal2006)

---

*Created as part of the M3 Mathematical Animation Project.*
