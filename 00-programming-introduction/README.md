# 🧠 Programming Introduction

![Programming](https://img.shields.io/badge/Programming-Fundamentals-blue?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Beginner-green?style=for-the-badge)
![Testing](https://img.shields.io/badge/Focus-Software%20Testing-orange?style=for-the-badge)
![AI](https://img.shields.io/badge/Path-AI%20Quality%20Engineering-purple?style=for-the-badge)

> **One topic → one folder → one README → complete learning chapter**

---

## 🗺️ Where This Topic Fits

```text
Programming
    │
    ├── Python Fundamentals
    │
    ├── Software Testing
    │
    ├── Automation
    │      ├── pytest
    │      ├── API Testing
    │      └── Playwright
    │
    └── AI Quality Engineering
           ├── AI Application Testing
           ├── LLM Testing
           ├── AI Evaluation
           └── CI/CD Quality Gates
```

This chapter gives you the **programming foundation** needed before learning Python and automation.

---

# 🎯 Learning Objectives

By the end of this chapter, you should be able to explain:

- What a **program** is
- What **programming** means
- What a **programming language** is
- How a computer executes instructions
- What source code and syntax mean
- What variables and data are
- What logic and algorithms are
- What conditions and loops do
- What functions are
- What bugs and debugging mean
- How programming connects to software testing
- How programming enables test automation
- Why programming knowledge matters for AI testing

---

# 1️⃣ What Is a Program?

A **program** is a set of instructions written for a computer to perform a task.

### Simple example

Imagine you want a computer to calculate the total price of two products.

```text
Product 1 = ₹100
Product 2 = ₹200

Total = ₹100 + ₹200

Output = ₹300
```

The instructions that tell the computer how to perform this calculation form a **program**.

### Real-world examples

| Application | Example of a Program |
|---|---|
| Calculator | Performs mathematical calculations |
| Browser | Opens and interacts with websites |
| Banking app | Performs banking operations |
| WhatsApp | Sends messages |
| Amazon | Handles shopping workflows |
| Netflix | Streams video |
| Test automation | Executes automated test cases |
| AI application | Processes prompts and generates responses |

---

# 2️⃣ What Is Programming?

**Programming is the process of creating instructions that tell a computer what to do.**

Think of it like giving instructions to a person.

```text
Human instruction:

1. Open the browser
2. Open the shopping website
3. Search for a laptop
4. Select a laptop
5. Add it to cart
6. Verify the cart
```

A programmer converts these instructions into a form that a computer can execute.

```text
Human Problem
      ↓
Logic
      ↓
Algorithm
      ↓
Program
      ↓
Computer
      ↓
Result
```

---

# 3️⃣ Program vs Programming vs Programming Language

| Term | Meaning | Example |
|---|---|---|
| Program | Instructions that perform a task | Login program |
| Programming | Process of creating programs | Writing login logic |
| Programming Language | Language used to write programs | Python, Java, JavaScript |
| Source Code | Human-readable program instructions | `print("Hello")` |
| Execution | Running the program | `python app.py` |

### Easy way to remember

> **Programming language = language**  
> **Programming = process**  
> **Program = finished set of instructions**

---

# 4️⃣ Why Do We Need Programming?

Programming allows us to automate tasks and solve problems.

Without programming:

```text
Human
  ↓
Manually performs task
  ↓
Repeats task
  ↓
Consumes time
```

With programming:

```text
Human
  ↓
Writes instructions once
  ↓
Computer executes them
  ↓
Task can be repeated
```

This is especially important in **software testing**.

### Manual testing

```text
Tester
  ↓
Open browser
  ↓
Login
  ↓
Search product
  ↓
Add product
  ↓
Verify result
```

### Automation

```text
Test Code
   ↓
Browser Automation
   ↓
Login
   ↓
Search
   ↓
Add Product
   ↓
Verify
```

---

# 5️⃣ How Does a Computer Execute a Program?

At a high level:

```text
Source Code
    ↓
Compiler / Interpreter
    ↓
Machine-understandable instructions
    ↓
CPU + Memory
    ↓
Execution
    ↓
Output
```

Computers ultimately execute machine-level instructions.

Humans prefer languages such as:

```python
print("Hello")
```

Computers operate using much lower-level representations.

---

# 6️⃣ What Is Source Code?

**Source code** is the human-readable code written by a programmer.

Example:

```python
name = "Vishwa"
print("Hello", name)
```

The programmer can read and understand this code.

The computer uses a language implementation to execute it.

---

# 7️⃣ What Is Syntax?

**Syntax is the set of rules that define how code must be written.**

Think about English.

Incorrect:

```text
I going school.
```

Better:

```text
I am going to school.
```

Programming languages also have rules.

Example Python:

```python
print("Hello")
```

Incorrect syntax may cause an error.

```python
print("Hello"
```

The closing `)` is missing.

### Key idea

```text
Syntax = How code must be written
Logic  = What the code should do
```

---

# 8️⃣ What Is Logic?

**Logic is the reasoning used to make a program behave correctly.**

Example:

```text
IF username is correct
AND password is correct
THEN login successfully

ELSE
    show login error
```

The programming language expresses this logic as executable code.

---

# 9️⃣ What Is an Algorithm?

An **algorithm** is a step-by-step procedure for solving a problem.

### Example: Login algorithm

```text
START
  ↓
Enter username
  ↓
Enter password
  ↓
Validate username
  ↓
Validate password
  ↓
Are both correct?
  ├── YES → Login successful
  └── NO  → Show error
  ↓
END
```

### Programming relationship

```text
Problem
   ↓
Algorithm
   ↓
Logic
   ↓
Source Code
   ↓
Program
```

---

# 🔟 What Is a Flowchart?

A flowchart visually represents a process or algorithm.

Example:

```text
       ┌───────────┐
       │   START   │
       └─────┬─────┘
             ↓
     ┌───────────────┐
     │ Enter password│
     └───────┬───────┘
             ↓
      ┌─────────────┐
      │ Password OK?│
      └──────┬──────┘
          YES│   │NO
             ↓   ↓
       ┌───────┐ ┌────────────┐
       │ Login │ │ Show Error │
       └───┬───┘ └─────┬──────┘
           ↓           ↓
          END         END
```

Flowcharts are useful before writing complex automation or application logic.

---

# 1️⃣1️⃣ What Is Data?

**Data is information that a program stores, processes, or uses.**

Examples:

```text
Name       → "Vishwa"
Age        → 39
Price      → 999.50
Login      → True
Product ID → "P1001"
```

Later in Python, you will learn different **data types** for representing this data.

---

# 1️⃣2️⃣ What Is a Variable?

A variable is a **name used by a program to refer to a value**.

Example:

```python
name = "Vishwa"
age = 39
price = 999.50
```

Conceptually:

```text
name  ─────→ "Vishwa"
age   ─────→ 39
price ─────→ 999.50
```

### Important

In Python, it is more accurate to think of a variable as a **name/reference associated with an object/value**, rather than a box containing a fixed type.

---

# 1️⃣3️⃣ Input → Process → Output

One of the most important programming models is:

```text
INPUT
  ↓
PROCESS
  ↓
OUTPUT
```

### Example

```python
price = 100
quantity = 3

total = price * quantity

print(total)
```

### Explanation

```text
Input
  price = 100
  quantity = 3

       ↓

Process
  total = price × quantity

       ↓

Output
  300
```

---

# 1️⃣4️⃣ First Python Example

Python is one of the most useful languages for software testing and AI-related development.

```python
print("Hello, World!")
```

### What happens?

`print()` displays information on the screen.

Output:

```text
Hello, World!
```

---

# 1️⃣5️⃣ A Small Real-World Program

Imagine a test result.

```python
test_name = "Login Test"
status = "PASS"

print(test_name)
print(status)
```

Output:

```text
Login Test
PASS
```

This same basic programming concept eventually becomes:

```text
Test Case
   ↓
Automation Code
   ↓
Execution
   ↓
Assertion
   ↓
PASS / FAIL
   ↓
Report
```

---

# 1️⃣6️⃣ Conditions

Programs often need to make decisions.

Example:

```python
age = 20

if age >= 18:
    print("Eligible")
else:
    print("Not eligible")
```

Conceptually:

```text
Condition
   ↓
True? ─── YES → Action A
   │
   NO
   ↓
Action B
```

Conditions are heavily used in:

- application logic
- test automation
- API validation
- test data handling
- AI evaluation rules

---

# 1️⃣7️⃣ Loops

A loop repeats instructions.

Example:

```python
for i in range(3):
    print("Running test")
```

Output:

```text
Running test
Running test
Running test
```

### Why testers need loops

Suppose you need to test 100 usernames.

Instead of writing:

```text
Test username 1
Test username 2
Test username 3
...
Test username 100
```

you can write automation that processes test data repeatedly.

```text
Test Data
   ↓
Loop
   ↓
Execute Test
   ↓
Validate
   ↓
Next Data
```

---

# 1️⃣8️⃣ Functions

A function is a reusable block of code designed to perform a task.

Example:

```python
def add(a, b):
    return a + b

result = add(10, 20)

print(result)
```

Output:

```text
30
```

### Why functions matter

Without functions:

```text
Repeated code
Repeated code
Repeated code
```

With functions:

```text
Reusable Function
       ↓
Call whenever needed
```

Automation frameworks depend heavily on reusable functions and abstractions.

---

# 1️⃣9️⃣ Bugs

A **bug** is a defect or unexpected behavior in software.

Example:

```python
price = 100
quantity = 2

total = price + quantity
```

Expected:

```text
200
```

Actual:

```text
102
```

The logic is wrong.

Correct:

```python
total = price * quantity
```

---

# 2️⃣0️⃣ Debugging

**Debugging is the process of finding and fixing the cause of a problem in software.**

Typical process:

```text
Bug
 ↓
Reproduce
 ↓
Investigate
 ↓
Find Root Cause
 ↓
Fix
 ↓
Retest
 ↓
Verify
```

Testing and debugging are related but not identical.

> **Testing finds evidence of problems. Debugging investigates and fixes the cause.**

---

# 2️⃣1️⃣ Programming and Software Testing

Programming becomes extremely valuable when moving from manual testing to automation.

### Manual testing

```text
Tester
 ↓
Execute test manually
 ↓
Observe result
 ↓
Record PASS/FAIL
```

### Automation testing

```text
Test Code
 ↓
Automation Framework
 ↓
Application
 ↓
Validation / Assertion
 ↓
PASS / FAIL
 ↓
Report
```

Programming allows the tester to create the instructions that perform these actions.

---

# 2️⃣2️⃣ Programming + Testing Terminology

| Programming Concept | Testing Usage |
|---|---|
| Variable | Store test data |
| Data type | Represent test values |
| Condition | Conditional test logic |
| Loop | Repeat test execution |
| Function | Reusable test action |
| Exception | Handle unexpected errors |
| File | Read/write test data |
| JSON | API request/response data |
| Class | Framework abstraction |
| Object | Test/page/API object |
| Assertion | Validate expected vs actual |
| Logging | Record execution information |

---

# 2️⃣3️⃣ Programming → Automation

The journey looks like this:

```text
Programming Fundamentals
          ↓
Python
          ↓
Testing Fundamentals
          ↓
pytest
          ↓
API Testing
          ↓
Playwright
          ↓
Automation Framework
          ↓
CI/CD
```

---

# 2️⃣4️⃣ Programming → AI Testing

Modern applications increasingly contain AI components.

The testing journey can therefore become:

```text
Python
   ↓
Software Testing
   ↓
Automation
   ↓
AI Application Testing
   ↓
LLM Testing
   ↓
AI Evaluation
   ↓
AI Quality Engineering
   ↓
CI/CD Quality Gates
```

---

# 2️⃣5️⃣ What Is AI Application Testing?

Traditional application:

```text
Input → Code → Output
```

AI application:

```text
Input
  ↓
Prompt / Request
  ↓
AI Model
  ↓
Generated Response
  ↓
Evaluation
```

Testing AI applications can involve checking:

- correctness
- relevance
- groundedness
- safety
- consistency
- latency
- cost
- hallucination
- prompt behavior
- tool/function calling
- retrieval quality

Programming becomes the foundation for automating these checks.

---

# 2️⃣6️⃣ Example: Automated AI Quality Check

A simplified example:

```python
response = "The capital of France is Paris."

expected = "Paris"

if expected in response:
    print("PASS")
else:
    print("FAIL")
```

This is only a basic example. Real AI evaluation requires much stronger evaluation strategies.

---

# 2️⃣7️⃣ Programming Languages

There are many programming languages.

| Language | Common Areas |
|---|---|
| Python | Automation, AI, testing, backend, data |
| Java | Enterprise, backend, automation |
| JavaScript | Web, frontend, Node.js |
| TypeScript | Web, automation, enterprise |
| C | Systems, embedded |
| C++ | Systems, performance applications |
| C# | .NET, enterprise, testing |
| Go | Cloud, infrastructure, backend |
| Rust | Systems, security, performance |

### For this learning path

We primarily use:

```text
Python
  ↓
pytest
  ↓
API Testing
  ↓
Playwright
  ↓
AI Testing
  ↓
AI Quality Engineering
```

---

# 2️⃣8️⃣ Compiler vs Interpreter

At a simplified level:

### Compiler

```text
Source Code
    ↓
Compiler
    ↓
Compiled Representation
    ↓
Execution
```

Examples include languages commonly associated with compiled workflows such as C/C++.

### Interpreter / Runtime

```text
Source Code
    ↓
Language Runtime
    ↓
Execution
```

Python uses an implementation/runtime model involving compilation to bytecode and execution by the Python virtual machine.

> The simple “compiler vs interpreter” distinction is useful for beginners, but real language implementations can be more sophisticated.

---

# 2️⃣9️⃣ Software vs Program vs Application

| Term | Simple Meaning |
|---|---|
| Program | Instructions that perform a task |
| Software | Collection of programs/components that provide functionality |
| Application | Software designed for users or a particular purpose |
| Automation Script | Program that automates a task |
| Test Script | Program that executes and validates a test |

Example:

```text
Shopping Application
      ↓
Login Feature
      ↓
Login Test
      ↓
Automation Script
```

---

# 3️⃣0️⃣ Mini Example: Login Logic

```python
username = "admin"
password = "secret"

if username == "admin" and password == "secret":
    print("Login successful")
else:
    print("Login failed")
```

### Testing perspective

We can create test scenarios:

| Scenario | Username | Password | Expected |
|---|---|---|---|
| Valid login | admin | secret | PASS |
| Invalid password | admin | wrong | FAIL |
| Invalid username | user | secret | FAIL |
| Both invalid | user | wrong | FAIL |

This is how programming logic starts connecting with test design.

---

# 3️⃣1️⃣ Mini Example: Test Result

```python
expected = "PASS"
actual = "PASS"

if expected == actual:
    print("Test Passed")
else:
    print("Test Failed")
```

Later, testing frameworks provide proper **assertions**:

```python
assert actual == expected
```

You will learn assertions in the pytest module.

---

# 3️⃣2️⃣ Common Beginner Mistakes

### ❌ Mistake 1: Learning syntax without understanding logic

Don't only memorize:

```python
if
for
while
def
```

Understand **why** each construct exists.

### ❌ Mistake 2: Copying code without understanding it

Before executing code, ask:

```text
What is the input?
What is the process?
What is the output?
Why is this line required?
```

### ❌ Mistake 3: Thinking testing requires zero programming

Modern automation requires programming knowledge.

### ❌ Mistake 4: Trying to learn everything at once

You do **not** need every advanced Python feature before starting testing.

Focus on:

```text
Fundamentals
   ↓
Testing
   ↓
Automation
   ↓
Advanced concepts when needed
```

---

# 🧪 Mini Exercises

## Exercise 1 — Hello Program

Write a program that prints:

```text
My name is Vishwa
I am learning Python
I want to become an Automation Engineer
```

---

## Exercise 2 — Calculator

Create variables:

```text
price = 100
quantity = 5
```

Calculate and print the total.

Expected:

```text
500
```

---

## Exercise 3 — Login

Create:

```text
username
password
```

Print:

```text
Login successful
```

when both values are correct.

---

## Exercise 4 — Test Result

Create:

```text
expected = "PASS"
actual = "PASS"
```

Print whether the test passed or failed.

---

## Exercise 5 — Multiple Test Data

Create a list of test names and use a loop to print each one.

Expected idea:

```text
Login Test
Search Test
Cart Test
Checkout Test
```

---

# 🎯 Beginner Challenge

Build a tiny **Test Result Processor**.

Input:

```text
Test Name
Expected Result
Actual Result
```

Process:

```text
Compare expected and actual
```

Output:

```text
PASS / FAIL
```

Example:

```text
Test Name: Login Test
Expected: PASS
Actual: PASS

Result: PASS
```

---

# 💼 Real-World Testing Connection

A real automation framework eventually looks conceptually like:

```text
Test Data
    ↓
Test Case
    ↓
Automation Code
    ↓
Application / API / AI System
    ↓
Assertion / Evaluation
    ↓
PASS / FAIL
    ↓
Report
    ↓
CI/CD Quality Gate
```

Programming is the foundation underneath this entire workflow.

---

# 🎤 Interview Questions

### Beginner

1. What is a program?
2. What is programming?
3. What is a programming language?
4. What is source code?
5. What is syntax?
6. What is programming logic?
7. What is an algorithm?
8. What is a flowchart?
9. What is a variable?
10. What is data?
11. What is a bug?
12. What is debugging?
13. What is a function?
14. What is a loop?
15. What is a condition?

### Testing-oriented

16. Why does an automation tester need programming?
17. How are variables used in test automation?
18. Why are loops useful in automation?
19. Why are functions useful in test frameworks?
20. How does programming help automate repetitive tests?
21. What is the relationship between programming and assertions?
22. How can programming be used to validate API responses?
23. How can programming help test AI responses?

---

# 🧠 Remember This

```text
PROGRAM
= Instructions

PROGRAMMING
= Creating those instructions

PROGRAMMING LANGUAGE
= Language used to write those instructions

LOGIC
= Reasoning behind the behavior

ALGORITHM
= Step-by-step solution

SOURCE CODE
= Human-readable implementation

BUG
= Defect / unexpected behavior

DEBUGGING
= Finding and fixing the cause
```

---

# 🚀 Your Learning Journey

```text
                 PROGRAMMING
                      │
                      ▼
                    PYTHON
                      │
                      ▼
              TESTING FUNDAMENTALS
                      │
                      ▼
                    PYTEST
                      │
             ┌────────┴────────┐
             ▼                 ▼
        API TESTING       PLAYWRIGHT
             │                 │
             └────────┬────────┘
                      ▼
             AUTOMATION FRAMEWORK
                      │
                      ▼
             AI APPLICATION TESTING
                      │
                      ▼
                LLM TESTING
                      │
                      ▼
                AI EVALUATION
                      │
                      ▼
          AI QUALITY ENGINEERING
                      │
                      ▼
              CI/CD QUALITY GATES
```

> ⭐ **You don't learn programming just to write code. You learn programming so you can solve problems, automate work, validate software, and eventually engineer quality into modern AI systems.**

---

# 🔗 Official Learning Resources

- [Python Official Documentation](https://docs.python.org/3/)
- [Python Beginner's Guide](https://wiki.python.org/moin/BeginnersGuide)
- [Python Tutorial](https://docs.python.org/3/tutorial/)
- [pytest Documentation](https://docs.pytest.org/)
- [Playwright Documentation](https://playwright.dev/)
- [GitHub Documentation](https://docs.github.com/)

---

# ✅ Completion Checklist

- [ ] I understand what a program is
- [ ] I understand programming
- [ ] I understand programming languages
- [ ] I understand source code
- [ ] I understand syntax
- [ ] I understand logic
- [ ] I understand algorithms
- [ ] I understand variables
- [ ] I understand input → process → output
- [ ] I understand conditions
- [ ] I understand loops
- [ ] I understand functions
- [ ] I understand bugs
- [ ] I understand debugging
- [ ] I understand why programming is important for testing
- [ ] I can explain how programming leads to automation
- [ ] I can explain how programming supports AI testing

---

## 🏁 Next Chapter

➡️ **[01 — Python Introduction](../01-python-introduction/README.md)**

Your next step is to learn **Python itself** and begin writing real Python programs.

---

<p align="center">

### 🚀 Learn → Practice → Automate → Test → Evaluate → Engineer Quality

**Python → Testing → Automation → AI Testing → AI Quality Engineering**

</p>
