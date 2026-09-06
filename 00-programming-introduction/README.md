# 💻 00 — Introduction to Programming

![Programming](https://img.shields.io/badge/Topic-Programming%20Fundamentals-6f42c1?style=for-the-badge)
![Beginner](https://img.shields.io/badge/Level-Beginner-2ea44f?style=for-the-badge)
![Testing](https://img.shields.io/badge/Goal-Software%20Testing%20%26%20Automation-ff8c00?style=for-the-badge)
![AI](https://img.shields.io/badge/Path-AI%20Quality%20Engineering-8a2be2?style=for-the-badge)

> 🌟 **Before learning Python, understand what programming actually is.**
>
> Programming is not about memorizing syntax. It is about **understanding a problem, designing a solution, expressing that solution as instructions, executing it, and validating the result.**

---

## 🧭 Where This Fits in Your Journey

```text
🧠 Problem
   ↓
💡 Logic / Algorithm
   ↓
📝 Program
   ↓
⚙️ Programming Language
   ↓
🖥️ Computer Execution
   ↓
✅ Output
   ↓
🧪 Testing
   ↓
🤖 Automation
   ↓
🧠 AI Quality Engineering
```

This module gives you the foundation for everything that follows.

---

# 1️⃣ What Is a Program?

A **program** is a set of instructions written for a computer to perform a specific task.

In simple words:

> 📌 **Program = Instructions + Data + Logic + Execution**

For example, imagine a login system.

```text
User enters username
        ↓
User enters password
        ↓
Application validates credentials
        ↓
If valid → Login successful
If invalid → Login failed
```

Those instructions can be represented by a program.

### 🧑‍💻 Simple example

```python
username = "tester"
password = "secret"

if username == "tester" and password == "secret":
    print("Login successful")
else:
    print("Login failed")
```

The computer does not understand our intention.

It follows the instructions we provide.

---

# 2️⃣ What Is Programming?

**Programming** is the process of designing and writing instructions that a computer can execute to solve a problem or perform a task.

Programming involves:

| Step | Activity |
|---|---|
| 🧩 1 | Understand the problem |
| 🔍 2 | Analyze requirements |
| 💡 3 | Design the solution |
| 🧮 4 | Create an algorithm |
| 📝 5 | Write code |
| ▶️ 6 | Execute the program |
| 🧪 7 | Test the result |
| 🐞 8 | Debug problems |
| 🔧 9 | Improve the solution |
| 🚀 10 | Maintain and deploy |

So programming is much more than typing code.

---

# 3️⃣ Program vs Programming vs Programming Language

These three terms are often confused.

### 📦 Program

A **program** is the actual set of instructions.

```python
print("Hello")
```

### 🛠️ Programming

**Programming** is the activity/process of creating that program.

```text
Problem
  ↓
Think
  ↓
Design
  ↓
Code
  ↓
Test
  ↓
Fix
```

### 🗣️ Programming Language

A **programming language** is the language used to express instructions to a computer.

Examples:

```text
🐍 Python
☕ Java
🟨 JavaScript
🔷 C#
⚙️ C/C++
🦀 Rust
🐹 Go
```

### Easy analogy

```text
English
   ↓
Language

Writing a letter
   ↓
Activity

The actual letter
   ↓
Output
```

Similarly:

```text
Python
   ↓
Programming Language

Writing Python code
   ↓
Programming

Python application
   ↓
Program
```

---

# 4️⃣ Why Do We Need Programming?

Computers are extremely fast at executing instructions, but they need instructions from humans.

Programming allows us to build:

- 🌐 Websites
- 📱 Mobile applications
- 🖥️ Desktop applications
- ☁️ Cloud systems
- 🗄️ Databases
- 🔌 APIs
- 🤖 Automation
- 🧪 Testing frameworks
- 🧠 AI applications
- 📊 Data systems
- 🎮 Games
- 🔐 Security tools
- ⚙️ DevOps platforms

Almost every modern software system contains programs.

---

# 5️⃣ How Does a Computer Execute a Program?

At a high level:

```text
👨‍💻 Human
   │
   │ writes code
   ▼
📝 Source Code
   │
   ▼
⚙️ Compiler / Interpreter / Runtime
   │
   ▼
🖥️ Machine-level execution
   │
   ▼
📤 Output
```

The exact process depends on the programming language.

For example, Python generally uses an interpreter/runtime environment to execute Python code.

```python
print("Hello World")
```

When executed, Python processes the instruction and produces:

```text
Hello World
```

---

# 6️⃣ What Is Source Code?

**Source code** is the human-readable code written by a developer or engineer.

Example:

```python
name = "Vishwa"
print("Hello", name)
```

A source-code file can contain:

- Variables
- Functions
- Conditions
- Loops
- Classes
- Data structures
- Imports
- Error handling
- Business logic

Python files normally use:

```text
.py
```

Example:

```text
login_test.py
api_client.py
calculator.py
```

---

# 7️⃣ What Is Syntax?

**Syntax** means the rules for writing valid code in a programming language.

Think of syntax like grammar in a human language.

### Human language

❌ Incorrect:

```text
I going school.
```

✅ Correct:

```text
I am going to school.
```

### Python

```python
if status == 200:
    print("PASS")
```

Python expects specific syntax.

Incorrect indentation or invalid syntax can cause an error.

---

# 8️⃣ What Is Logic?

**Logic** is the reasoning used to decide what a program should do.

Example:

```text
IF payment is successful
    THEN create order
ELSE
    show payment failure
```

Python:

```python
if payment_successful:
    create_order()
else:
    show_payment_error()
```

Logic is extremely important for testers.

Why?

Because testing is largely about asking:

> 🧪 **"Does the software behave correctly for every important condition?"**

---

# 9️⃣ What Is an Algorithm?

An **algorithm** is a step-by-step procedure for solving a problem.

Example: Find whether a number is even.

### Algorithm

```text
1. Take a number
2. Divide it by 2
3. Check the remainder
4. If remainder = 0 → Even
5. Otherwise → Odd
```

Python:

```python
number = 10

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

### Algorithm vs Program

```text
Algorithm
   ↓
Solution steps

Program
   ↓
Algorithm expressed in a programming language
```

---

# 🔟 What Is a Flowchart?

A flowchart visually represents program logic.

Example:

```text
        ┌─────────────┐
        │ Start       │
        └──────┬──────┘
               ↓
        ┌─────────────┐
        │ Enter age   │
        └──────┬──────┘
               ↓
        ┌─────────────┐
        │ age >= 18 ? │
        └──────┬──────┘
          Yes /   \ No
             ↓     ↓
       ┌───────┐ ┌────────┐
       │Adult  │ │Minor   │
       └───┬───┘ └───┬────┘
           └─────┬───┘
                 ↓
          ┌────────────┐
          │    End     │
          └────────────┘
```

Flowcharts help beginners understand logic before writing code.

---

# 1️⃣1️⃣ What Is a Variable?

A variable is a name used by a program to refer to a value.

Example:

```python
name = "Vishwa"
age = 39
```

Conceptually:

```text
name ─────► "Vishwa"
age  ─────► 39
```

Variables allow programs to work with changing data.

For testing:

```python
username = "tester"
expected_status = 200
timeout = 5
```

---

# 1️⃣2️⃣ What Is Data?

**Data** is information processed by a program.

Examples:

```text
Name
Age
Email
Password
Product
Price
Order ID
HTTP status
Response body
AI prompt
AI response
```

A program takes data, processes it using logic, and produces a result.

```text
📥 Input Data
     ↓
⚙️ Processing
     ↓
📤 Output
```

---

# 1️⃣3️⃣ Input → Process → Output

This is one of the most important programming concepts.

```text
          ┌────────────┐
          │   INPUT    │
          └─────┬──────┘
                ↓
          ┌────────────┐
          │  PROCESS   │
          └─────┬──────┘
                ↓
          ┌────────────┐
          │   OUTPUT   │
          └────────────┘
```

### Example

```python
price = 100
quantity = 3

total = price * quantity

print(total)
```

```text
Input
100 × 3

   ↓

Process
price * quantity

   ↓

Output
300
```

---

# 1️⃣4️⃣ What Is a Function?

A function is a reusable block of code designed to perform a task.

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

Functions are important because automation frameworks contain many reusable operations.

Examples:

```text
login()
logout()
create_user()
delete_user()
send_request()
validate_response()
generate_report()
```

---

# 1️⃣5️⃣ What Are Conditions?

Conditions allow programs to make decisions.

```python
status_code = 200

if status_code == 200:
    print("PASS")
else:
    print("FAIL")
```

Testing is full of conditions:

```text
IF status == 200 → PASS
IF status == 500 → FAIL

IF login succeeds → dashboard visible
IF login fails → error message visible
```

---

# 1️⃣6️⃣ What Are Loops?

A loop repeats instructions.

```python
for test_case in ["TC001", "TC002", "TC003"]:
    print(test_case)
```

Output:

```text
TC001
TC002
TC003
```

Automation uses loops constantly.

For example:

```text
Read 100 test cases
      ↓
Execute each test
      ↓
Capture result
      ↓
Generate report
```

---

# 1️⃣7️⃣ What Is Debugging?

**Debugging** is the process of finding and fixing problems in software.

Example:

```python
expected = 10
actual = 8

print(expected)
print(actual)
```

A tester/developer investigates:

```text
Expected = 10
Actual   = 8
             ↓
        Why different?
             ↓
       Find root cause
             ↓
          Fix it
```

### Common debugging techniques

- 🔍 Read error messages
- 📝 Add logs
- 🧪 Reproduce the problem
- 🔬 Inspect variables
- 🪜 Use a debugger
- 🔁 Create a small reproducible example
- ✅ Add a regression test

---

# 1️⃣8️⃣ What Is a Bug?

A **bug/defect** is a problem where software behaves differently from its intended or expected behavior.

Example:

```text
Requirement:
Users with valid credentials should log in.

Actual:
Valid credentials produce "Invalid password".
```

That difference needs investigation.

---

# 1️⃣9️⃣ Programming and Software Testing

Programming and testing are closely connected.

### Developer mindset

```text
"How do I build this?"
```

### Tester mindset

```text
"How do I prove this works?"
"How can it fail?"
"What happens with invalid input?"
"What happens at the boundaries?"
```

### Automation engineer mindset

```text
"How can I test this repeatedly with code?"
```

### AI Quality Engineer mindset

```text
"How can I measure whether this AI system is
correct, safe, reliable, grounded and production-ready?"
```

---

# 2️⃣0️⃣ Manual Testing → Automation → AI Quality

Your learning journey:

```text
🧑‍💻 Programming Fundamentals
            ↓
🧪 Manual Testing Fundamentals
            ↓
🐍 Python
            ↓
🧪 pytest
            ↓
🔌 API Automation
            ↓
🎭 Playwright
            ↓
🏗️ Automation Framework
            ↓
🤖 AI Application Testing
            ↓
🧠 LLM Evaluation
            ↓
📊 AI Quality Engineering
            ↓
🚀 CI/CD Quality Gates
```

---

# 2️⃣1️⃣ Why Learn Programming Before Python?

Python is a **programming language**.

Before learning Python syntax, students should understand:

- What a program is
- What programming means
- What an algorithm is
- What logic means
- What variables represent
- What data is
- What input/output means
- What functions do
- What conditions do
- What loops do
- What debugging means
- What testing means

Then Python becomes much easier.

Instead of learning:

```python
if
for
def
list
dict
```

as isolated syntax, students understand:

```text
Decision
 ↓
if

Repetition
 ↓
for

Reusable operation
 ↓
function

Collection of data
 ↓
list/dict
```

---

# 2️⃣2️⃣ Programming Languages — Big Picture

Programming languages can be grouped in different ways.

## By abstraction

```text
Low-level
   ↓
Machine-oriented
   ↓
Assembly
   ↓
High-level
   ↓
Python / Java / JavaScript / C#
```

## By common usage

| Area | Examples |
|---|---|
| 🌐 Web | JavaScript, TypeScript |
| 🐍 Automation | Python |
| 🏢 Enterprise | Java, C# |
| ⚙️ Systems | C, C++, Rust |
| 📱 Mobile | Kotlin, Swift |
| ☁️ Cloud/Platform | Go, Python, Java |
| 🤖 AI/Data | Python |
| 🧪 Testing | Python, Java, JavaScript, C# |

There is no single "best" programming language.

The right language depends on the problem, ecosystem, team and tooling.

---

# 2️⃣3️⃣ Compiler vs Interpreter — Beginner View

### Compiler

A compiler generally translates source code into another executable/intermediate form before execution.

Examples commonly associated with compiled languages include:

```text
C
C++
Rust
Go
```

### Interpreter / Runtime

An interpreter/runtime executes or evaluates program instructions through a runtime system.

Python is commonly described as an interpreted language at the beginner level, although its implementation involves compilation to bytecode before execution by the Python virtual machine.

### Important

Don't get stuck on terminology.

For beginners, remember:

```text
Source Code
    ↓
Language Runtime / Toolchain
    ↓
Execution
    ↓
Result
```

---

# 2️⃣4️⃣ What Is Software?

**Software** is a collection of programs, data, configuration and related components that instruct a computing system to perform tasks.

Examples:

```text
🌐 Browser
📱 Mobile App
🏦 Banking Application
🛒 E-commerce Platform
☁️ Cloud Platform
🤖 AI Chatbot
```

A useful simplified model:

```text
Software
├── Application Code
├── Data
├── Configuration
├── Dependencies
├── Infrastructure
└── Runtime Environment
```

---

# 2️⃣5️⃣ What Is an Application?

An **application** is software designed to perform tasks for users or other systems.

Example:

```text
E-commerce Application
│
├── Login
├── Product Search
├── Cart
├── Payment
├── Order
└── Notifications
```

Each feature contains programming logic.

Each feature can also have tests.

---

# 2️⃣6️⃣ What Is Automation?

**Automation** means using software to perform tasks with reduced manual intervention.

Example:

### Manual

```text
Open browser
   ↓
Login
   ↓
Search product
   ↓
Add product
   ↓
Checkout
   ↓
Verify result
```

### Automated

```text
Test Script
    ↓
Browser Automation
    ↓
Login
    ↓
Search
    ↓
Checkout
    ↓
Assertions
    ↓
Report
```

Python + Playwright can automate browser testing.

Python + requests can automate API testing.

Python + pytest can organize and execute tests.

---

# 2️⃣7️⃣ What Is AI Programming?

AI applications are also software.

A simplified AI application can look like:

```text
User Prompt
    ↓
Application Logic
    ↓
Model / AI Service
    ↓
Response
    ↓
Post-processing
    ↓
User
```

The quality problem becomes more complex because AI output may not always be deterministic.

Therefore:

```text
Traditional Testing
      +
AI Evaluation
      +
Safety
      +
Security
      +
Performance
      +
Observability
      ↓
AI Quality Engineering
```

---

# 2️⃣8️⃣ Programming Concepts You Will Learn Next

After this introduction, you will learn Python concepts in this order:

```text
01 🐍 Python Introduction
02 ⚙️ Installation & IDE
03 📦 Virtual Environments
04 📝 Syntax
05 📦 Variables
06 🔢 Data Types
07 🔄 Type Casting
08 🛠️ Operations & Methods
09 ➕ Operators
10 🔀 Control Flow
11 🔧 Functions
12 📚 Collections
13 🔤 Strings
14 🚨 Exceptions
15 📁 File Handling
16 🗂️ JSON & CSV
17 🔁 Iterators & enumerate()
18 ⚡ Generators
19 🎯 Decorators & Closures
20 📦 Modules
21 🗃️ Packages
22 📚 Libraries & Frameworks
23 📥 pip
24 📦 PyPI / Packaging
25 🧱 Classes & Objects
26 🧠 OOP
27 🚀 Advanced Python
28 ⚙️ Configuration
29 🔐 Environment Variables & Secrets
30 📝 Logging
31 📏 Coding Standards
32 🧪 Python for Testing
```

Not all topics need the same depth.

> ⭐ **Learn the fundamentals deeply. Learn advanced topics when they become useful.**

---

# 2️⃣9️⃣ Beginner Mini Exercises

### 🟢 Exercise 1 — Hello

Write a program that prints:

```text
Hello, Software Tester!
```

### 🟢 Exercise 2 — Addition

Create two numbers and print their sum.

### 🟢 Exercise 3 — Login Decision

Create username and password variables.

Print:

```text
Login successful
```

when both are correct.

### 🟡 Exercise 4 — Test Result

Given:

```python
status_code = 200
```

print `PASS` when the status code is in the successful HTTP range.

### 🟡 Exercise 5 — Multiple Tests

Create:

```python
test_cases = ["TC001", "TC002", "TC003", "TC004"]
```

Loop through them and print each test case.

### 🔴 Challenge

Build a small program that accepts:

```text
Test Case ID
Expected Status
Actual Status
```

and produces:

```text
TC001 → PASS
```

or

```text
TC001 → FAIL
```

---

# 3️⃣0️⃣ Interview Questions

### Beginner

**Q1. What is a program?**

A set of instructions that a computer executes to perform a task.

**Q2. What is programming?**

The process of designing, writing, testing, debugging and maintaining computer programs.

**Q3. What is an algorithm?**

A step-by-step procedure for solving a problem.

**Q4. What is source code?**

Human-readable code written using a programming language.

**Q5. What is syntax?**

The rules that define how valid code must be written.

**Q6. What is debugging?**

Finding and fixing defects in a program.

**Q7. What is automation?**

Using software to perform tasks automatically or with reduced manual effort.

**Q8. Why does a tester need programming?**

Programming enables testers to create reusable automated checks, test data, API tests, UI tests, utilities and quality gates.

---

# 🏆 Final Takeaway

If you remember only one thing from this module, remember this:

```text
             PROBLEM
                ↓
             ANALYZE
                ↓
             ALGORITHM
                ↓
              LOGIC
                ↓
             PROGRAM
                ↓
              RUN
                ↓
              TEST
                ↓
             DEBUG
                ↓
            AUTOMATE
                ↓
        MEASURE QUALITY
```

### 🚀 Your next step

Now that you understand **what programming is**, move to:

> 🐍 **01 — Python Introduction**

There we will learn what Python is, why it is popular, where it is used, why it is especially useful for testing and AI, and how Python fits into your automation journey.

---

## 🔗 Useful Official Resources

- 🐍 [Python Official Documentation](https://docs.python.org/3/)
- 📘 [Python Beginner's Guide](https://wiki.python.org/moin/BeginnersGuide)
- 🧑‍💻 [Python Tutorial](https://docs.python.org/3/tutorial/)
- 🧪 [pytest Documentation](https://docs.pytest.org/)
- 🎭 [Playwright Python](https://playwright.dev/python/)
- 📦 [Python Packaging User Guide](https://packaging.python.org/)

---

## 💙 Remember

> **You don't need to become a computer scientist before becoming a tester.**
>
> You need to understand the fundamentals, practice consistently, and connect every programming concept to a real software problem.

**Next:** `01-python-introduction` 🐍
