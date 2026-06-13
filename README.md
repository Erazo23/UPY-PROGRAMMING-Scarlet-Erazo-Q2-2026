## Classwork 08 - Numerical Integration

In this project, I made a program to calculate the area under a curve using numerical integration. The program works for 6 different functions, like $x^2-4x+3$, $\sin(x)$, $e^x$, and others.

### What I did in this assignment:
1. **Wrote the Pseudocode (`PPP.txt`):** I created the logic of the program in plain English. I followed the class rules, using `<-` for variables and `#` for my comments. It includes all 4 methods: Left Riemann Sum, Right Riemann Sum, Midpoint, and Trapezoid.
2. **Made the Flowchart (`Flowchart.png`):** I built a diagram to show how the loops work for every method and how the program decides what to do based on the 3 modes (Default, Custom, and Auto-adjust).
3. **Coded the Python Script (`numerical_integration.py`):** I wrote the Python code to do the math. The program calculates the exact area using calculus and compares it with the approximation to find the absolute and relative errors. For Mode 3, I made a while loop that doubles the number of splits ($n$) automatically until the error is smaller than the limit.

### AI Use Declaration:
I declare that I used AI as an assistant to help me fix some syntax bugs in the pseudocode blocks and organize the flowchart logic.