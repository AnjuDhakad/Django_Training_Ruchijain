
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import TestResult


# =========================================================
# HOME
# =========================================================

def home(request):

    if request.user.is_authenticated:
        return redirect('dashboard')

    return render(request, 'home.html')


# =========================================================
# SIGNUP
# =========================================================

def signup(request):

    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':

        full_name = request.POST.get('full_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:

            messages.error(
                request,
                'Passwords do not match.'
            )

            return render(
                request,
                'signup.html'
            )

        if User.objects.filter(username=username).exists():

            messages.error(
                request,
                'Username already exists.'
            )

            return render(
                request,
                'signup.html'
            )

        if User.objects.filter(email=email).exists():

            messages.error(
                request,
                'Email already exists.'
            )

            return render(
                request,
                'signup.html'
            )

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=full_name
        )

        user.save()

        messages.success(
            request,
            'Account created successfully. Please login.'
        )

        return redirect('login')

    return render(
        request,
        'signup.html'
    )


# =========================================================
# LOGIN
# =========================================================

def user_login(request):

    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect('dashboard')

        messages.error(
            request,
            'Invalid username or password.'
        )

    return render(
        request,
        'login.html'
    )


# =========================================================
# LOGOUT
# =========================================================

def user_logout(request):

    logout(request)

    return redirect('login')


# =========================================================
# ALL TESTS
# =========================================================

TESTS = {

    # =====================================================
    # TEST 1 - PYTHON
    # =====================================================

    10: {

        "name": "Python Fundamentals",

        "questions": [

            {
                "question":
                "Which keyword is used to define a function in Python?",

                "options": [
                    "function",
                    "def",
                    "define",
                    "fun"
                ],

                "answer": "def"
            },

            {
                "question":
                "Which of the following is a Python data type?",

                "options": [
                    "List",
                    "Document",
                    "Page",
                    "Browser"
                ],

                "answer": "List"
            },

            {
                "question":
                "Which symbol is used for comments in Python?",

                "options": [
                    "//",
                    "#",
                    "/* */",
                    "<!-- -->"
                ],

                "answer": "#"
            },

            {
                "question":
                "Which function is used to display output in Python?",

                "options": [
                    "display()",
                    "show()",
                    "print()",
                    "output()"
                ],

                "answer": "print()"
            },

            {
                "question":
                "Which collection is ordered and changeable?",

                "options": [
                    "Tuple",
                    "Set",
                    "List",
                    "String"
                ],

                "answer": "List"
            },

            {
                "question":
                "Which operator is used for exponentiation?",

                "options": [
                    "^",
                    "**",
                    "//",
                    "%%"
                ],

                "answer": "**"
            },

            {
                "question":
                "What is the correct extension of a Python file?",

                "options": [
                    ".java",
                    ".html",
                    ".py",
                    ".python"
                ],

                "answer": ".py"
            },

            {
                "question":
                "Which value represents True in Python?",

                "options": [
                    "true",
                    "TRUE",
                    "True",
                    "yes"
                ],

                "answer": "True"
            },

            {
                "question":
                "Which keyword is commonly used for a loop?",

                "options": [
                    "loop",
                    "repeat",
                    "for",
                    "iterate"
                ],

                "answer": "for"
            },

            {
                "question":
                "Which database is used by default in Django?",

                "options": [
                    "MySQL",
                    "MongoDB",
                    "SQLite",
                    "Oracle"
                ],

                "answer": "SQLite"
            }
        ]
    },


    # =====================================================
    # TEST 2 - WEB DEVELOPMENT
    # =====================================================

    20: {

        "name": "Web Development",

        "questions": [

            {
                "question": "HTML stands for?",

                "options": [
                    "Hyper Text Markup Language",
                    "High Text Machine Language",
                    "Hyper Transfer Markup Language",
                    "Home Tool Markup Language"
                ],

                "answer": "Hyper Text Markup Language"
            },

            {
                "question": "CSS stands for?",

                "options": [
                    "Creative Style Sheets",
                    "Cascading Style Sheets",
                    "Computer Style System",
                    "Colorful Style Sheets"
                ],

                "answer": "Cascading Style Sheets"
            },

            {
                "question": "Which tag creates a hyperlink?",

                "options": [
                    "<link>",
                    "<a>",
                    "<href>",
                    "<url>"
                ],

                "answer": "<a>"
            },

            {
                "question": "Which language is used to style web pages?",

                "options": [
                    "HTML",
                    "Python",
                    "CSS",
                    "SQL"
                ],

                "answer": "CSS"
            },

            {
                "question": "Which is the largest heading tag?",

                "options": [
                    "<h6>",
                    "<head>",
                    "<h1>",
                    "<heading>"
                ],

                "answer": "<h1>"
            },

            {
                "question": "Which CSS property changes text color?",

                "options": [
                    "font-color",
                    "text-color",
                    "color",
                    "foreground"
                ],

                "answer": "color"
            },

            {
                "question": "Which tag is used for a paragraph?",

                "options": [
                    "<paragraph>",
                    "<p>",
                    "<para>",
                    "<text>"
                ],

                "answer": "<p>"
            },

            {
                "question": "Which CSS property changes background color?",

                "options": [
                    "bgcolor",
                    "background",
                    "background-color",
                    "color-background"
                ],

                "answer": "background-color"
            },

            {
                "question": "Which protocol is used for secure websites?",

                "options": [
                    "HTTP",
                    "FTP",
                    "HTTPS",
                    "SMTP"
                ],

                "answer": "HTTPS"
            },

            {
                "question": "Which language is mainly used to make web pages interactive?",

                "options": [
                    "HTML",
                    "CSS",
                    "JavaScript",
                    "SQL"
                ],

                "answer": "JavaScript"
            },

            {
                "question": "Which tag is used to insert an image?",

                "options": [
                    "<picture>",
                    "<image>",
                    "<img>",
                    "<src>"
                ],

                "answer": "<img>"
            },

            {
                "question": "Which CSS property changes font size?",

                "options": [
                    "text-size",
                    "font-size",
                    "size",
                    "font"
                ],

                "answer": "font-size"
            },

            {
                "question": "Which tag creates an unordered list?",

                "options": [
                    "<ol>",
                    "<list>",
                    "<ul>",
                    "<li>"
                ],

                "answer": "<ul>"
            },

            {
                "question": "Which tag defines a list item?",

                "options": [
                    "<item>",
                    "<li>",
                    "<list-item>",
                    "<ul>"
                ],

                "answer": "<li>"
            },

            {
                "question": "Which CSS property makes text bold?",

                "options": [
                    "font-bold",
                    "bold",
                    "font-weight",
                    "text-bold"
                ],

                "answer": "font-weight"
            },

            {
                "question": "Which symbol is used for an ID selector in CSS?",

                "options": [
                    ".",
                    "#",
                    "@",
                    "*"
                ],

                "answer": "#"
            },

            {
                "question": "Which symbol is used for a class selector in CSS?",

                "options": [
                    "#",
                    ".",
                    "@",
                    "&"
                ],

                "answer": "."
            },

            {
                "question": "Which attribute specifies an image source?",

                "options": [
                    "href",
                    "link",
                    "src",
                    "source"
                ],

                "answer": "src"
            },

            {
                "question": "Which attribute provides alternative text for an image?",

                "options": [
                    "title",
                    "alt",
                    "text",
                    "description"
                ],

                "answer": "alt"
            },

            {
                "question": "Which technology is used to query databases?",

                "options": [
                    "HTML",
                    "CSS",
                    "SQL",
                    "XML"
                ],

                "answer": "SQL"
            }
        ]
    },


    # =====================================================
    # TEST 3 - COMPUTER SCIENCE
    # =====================================================

    30: {

        "name": "Computer Science Basics",

        "questions": [

            {
                "question": "What does CPU stand for?",

                "options": [
                    "Central Processing Unit",
                    "Computer Processing Unit",
                    "Central Program Unit",
                    "Control Processing Unit"
                ],

                "answer": "Central Processing Unit"
            },

            {
                "question": "What does RAM stand for?",

                "options": [
                    "Random Access Memory",
                    "Read Access Memory",
                    "Rapid Access Machine",
                    "Random Application Memory"
                ],

                "answer": "Random Access Memory"
            },

            {
                "question": "Which of the following is an operating system?",

                "options": [
                    "Windows",
                    "Python",
                    "HTML",
                    "SQL"
                ],

                "answer": "Windows"
            },

            {
                "question": "Which number system uses 0 and 1?",

                "options": [
                    "Decimal",
                    "Binary",
                    "Octal",
                    "Hexadecimal"
                ],

                "answer": "Binary"
            },

            {
                "question": "Which data structure follows FIFO?",

                "options": [
                    "Stack",
                    "Queue",
                    "Tree",
                    "Graph"
                ],

                "answer": "Queue"
            },

            {
                "question": "Which data structure follows LIFO?",

                "options": [
                    "Queue",
                    "Stack",
                    "Array",
                    "Tree"
                ],

                "answer": "Stack"
            },

            {
                "question": "What does DBMS stand for?",

                "options": [
                    "Database Management System",
                    "Data Basic Management System",
                    "Database Machine System",
                    "Data Management Software"
                ],

                "answer": "Database Management System"
            },

            {
                "question": "Which of the following is a programming language?",

                "options": [
                    "Python",
                    "HTML",
                    "CSS",
                    "HTTP"
                ],

                "answer": "Python"
            },

            {
                "question": "Which device connects different networks?",

                "options": [
                    "Keyboard",
                    "Router",
                    "Monitor",
                    "Printer"
                ],

                "answer": "Router"
            },

            {
                "question": "What does URL stand for?",

                "options": [
                    "Uniform Resource Locator",
                    "Universal Resource Link",
                    "Uniform Reference Link",
                    "Universal Reference Locator"
                ],

                "answer": "Uniform Resource Locator"
            },

            {
                "question": "Which is a relational database?",

                "options": [
                    "MySQL",
                    "HTML",
                    "Python",
                    "Linux"
                ],

                "answer": "MySQL"
            },

            {
                "question": "What does AI stand for?",

                "options": [
                    "Artificial Intelligence",
                    "Automatic Internet",
                    "Advanced Information",
                    "Artificial Internet"
                ],

                "answer": "Artificial Intelligence"
            },

            {
                "question": "Which algorithm can find the shortest path?",

                "options": [
                    "Bubble Sort",
                    "Dijkstra",
                    "Binary Search",
                    "Merge Sort"
                ],

                "answer": "Dijkstra"
            },

            {
                "question": "Which sorting algorithm compares adjacent elements?",

                "options": [
                    "Bubble Sort",
                    "Selection Sort",
                    "Quick Sort",
                    "Merge Sort"
                ],

                "answer": "Bubble Sort"
            },

            {
                "question": "What does OOP stand for?",

                "options": [
                    "Object Oriented Programming",
                    "Object Operating Program",
                    "Open Object Programming",
                    "Object Order Process"
                ],

                "answer": "Object Oriented Programming"
            },

            {
                "question": "Which keyword is used to create a class in Python?",

                "options": [
                    "object",
                    "class",
                    "define",
                    "struct"
                ],

                "answer": "class"
            },

            {
                "question": "Which keyword is used for exception handling?",

                "options": [
                    "catch",
                    "error",
                    "try",
                    "exception"
                ],

                "answer": "try"
            },

            {
                "question": "Which command installs a Python package?",

                "options": [
                    "python install",
                    "pip install",
                    "package install",
                    "install pip"
                ],

                "answer": "pip install"
            },

            {
                "question": "What does API stand for?",

                "options": [
                    "Application Programming Interface",
                    "Application Program Internet",
                    "Advanced Programming Interface",
                    "Application Process Interface"
                ],

                "answer": "Application Programming Interface"
            },

            {
                "question": "Which is a widely used version control system?",

                "options": [
                    "Git",
                    "Django",
                    "React",
                    "Linux"
                ],

                "answer": "Git"
            },

            {
                "question": "Which command can list files in PowerShell?",

                "options": [
                    "dir",
                    "show",
                    "files",
                    "list"
                ],

                "answer": "dir"
            },

            {
                "question": "Which Django file contains URL patterns?",

                "options": [
                    "views.py",
                    "models.py",
                    "urls.py",
                    "settings.py"
                ],

                "answer": "urls.py"
            },

            {
                "question": "Which Django file contains database models?",

                "options": [
                    "models.py",
                    "views.py",
                    "urls.py",
                    "admin.py"
                ],

                "answer": "models.py"
            },

            {
                "question": "Which command starts the Django development server?",

                "options": [
                    "django start",
                    "python manage.py runserver",
                    "django run",
                    "python server"
                ],

                "answer": "python manage.py runserver"
            },

            {
                "question": "Which HTTP method is commonly used to submit form data?",

                "options": [
                    "GET",
                    "POST",
                    "PUT",
                    "READ"
                ],

                "answer": "POST"
            },

            {
                "question": "Which HTTP method is commonly used to retrieve data?",

                "options": [
                    "POST",
                    "GET",
                    "SEND",
                    "PUSH"
                ],

                "answer": "GET"
            },

            {
                "question": "Which language is used for database queries?",

                "options": [
                    "Python",
                    "SQL",
                    "HTML",
                    "CSS"
                ],

                "answer": "SQL"
            },

            {
                "question": "Which Python data structure stores key-value pairs?",

                "options": [
                    "List",
                    "Tuple",
                    "Dictionary",
                    "Set"
                ],

                "answer": "Dictionary"
            },

            {
                "question": "Which keyword is used to import a module?",

                "options": [
                    "include",
                    "require",
                    "import",
                    "module"
                ],

                "answer": "import"
            },

            {
                "question": "Which symbol is commonly used to access dictionary values by key?",

                "options": [
                    "()",
                    "{}",
                    "[]",
                    "<>"
                ],

                "answer": "[]"
            }
        ]
    },


    # =====================================================
    # TEST 4 - JAVASCRIPT
    # =====================================================

    40: {

        "name": "JavaScript Basics",

        "questions": [

            {
                "question":
                "Which keyword is used to declare a variable in JavaScript?",

                "options": [
                    "var",
                    "int",
                    "string",
                    "define"
                ],

                "answer": "var"
            },

            {
                "question":
                "Which symbol is used for single-line comments?",

                "options": [
                    "//",
                    "#",
                    "<!--",
                    "**"
                ],

                "answer": "//"
            },

            {
                "question":
                "Which function prints output in the browser console?",

                "options": [
                    "print()",
                    "console.log()",
                    "display()",
                    "write()"
                ],

                "answer": "console.log()"
            },

            {
                "question":
                "Which data type represents true or false?",

                "options": [
                    "String",
                    "Boolean",
                    "Integer",
                    "Array"
                ],

                "answer": "Boolean"
            },

            {
                "question":
                "Which symbol is used for strict equality?",

                "options": [
                    "=",
                    "==",
                    "===",
                    "!="
                ],

                "answer": "==="
            },

            {
                "question":
                "Which keyword is used to define a constant?",

                "options": [
                    "constant",
                    "const",
                    "let",
                    "fixed"
                ],

                "answer": "const"
            },

            {
                "question":
                "Which method adds an element to the end of an array?",

                "options": [
                    "push()",
                    "add()",
                    "append()",
                    "insert()"
                ],

                "answer": "push()"
            },

            {
                "question":
                "Which HTML tag is used to include JavaScript?",

                "options": [
                    "<js>",
                    "<javascript>",
                    "<script>",
                    "<code>"
                ],

                "answer": "<script>"
            },

            {
                "question":
                "Which operator is used for logical AND?",

                "options": [
                    "||",
                    "&&",
                    "!",
                    "&"
                ],

                "answer": "&&"
            },

            {
                "question":
                "Which keyword is used to create a function?",

                "options": [
                    "function",
                    "def",
                    "func",
                    "method"
                ],

                "answer": "function"
            }
        ]
    },


    # =====================================================
    # TEST 5 - SQL
    # =====================================================

    50: {

        "name": "SQL & Database",

        "questions": [

            {
                "question": "What does SQL stand for?",

                "options": [
                    "Structured Query Language",
                    "Simple Query Language",
                    "System Query Language",
                    "Structured Question Language"
                ],

                "answer": "Structured Query Language"
            },

            {
                "question":
                "Which command is used to retrieve data?",

                "options": [
                    "GET",
                    "SELECT",
                    "FETCH",
                    "READ"
                ],

                "answer": "SELECT"
            },

            {
                "question":
                "Which command is used to add new data?",

                "options": [
                    "INSERT",
                    "ADD",
                    "CREATE",
                    "PUT"
                ],

                "answer": "INSERT"
            },

            {
                "question":
                "Which command modifies existing data?",

                "options": [
                    "CHANGE",
                    "UPDATE",
                    "MODIFY",
                    "ALTER"
                ],

                "answer": "UPDATE"
            },

            {
                "question":
                "Which command removes data?",

                "options": [
                    "REMOVE",
                    "DELETE",
                    "DROP",
                    "CLEAR"
                ],

                "answer": "DELETE"
            },

            {
                "question":
                "Which key uniquely identifies a record?",

                "options": [
                    "Foreign Key",
                    "Primary Key",
                    "Unique Key",
                    "Candidate Key"
                ],

                "answer": "Primary Key"
            },

            {
                "question":
                "Which SQL clause filters records?",

                "options": [
                    "WHERE",
                    "FILTER",
                    "HAVING",
                    "SEARCH"
                ],

                "answer": "WHERE"
            },

            {
                "question":
                "Which database is used by default in Django?",

                "options": [
                    "MySQL",
                    "MongoDB",
                    "SQLite",
                    "Oracle"
                ],

                "answer": "SQLite"
            },

            {
                "question":
                "Which command creates a new table?",

                "options": [
                    "MAKE TABLE",
                    "CREATE TABLE",
                    "NEW TABLE",
                    "ADD TABLE"
                ],

                "answer": "CREATE TABLE"
            },

            {
                "question":
                "What is a collection of related data called?",

                "options": [
                    "Database",
                    "Variable",
                    "Function",
                    "Program"
                ],

                "answer": "Database"
            }
        ]
    },


    # =====================================================
    # TEST 6 - AI & DATA SCIENCE
    # =====================================================

    60: {

        "name": "AI & Data Science",

        "questions": [

            {
                "question": "What does AI stand for?",

                "options": [
                    "Artificial Intelligence",
                    "Automated Information",
                    "Advanced Internet",
                    "Artificial Information"
                ],

                "answer": "Artificial Intelligence"
            },

            {
                "question": "What does ML stand for?",

                "options": [
                    "Machine Learning",
                    "Machine Language",
                    "Model Learning",
                    "Modern Logic"
                ],

                "answer": "Machine Learning"
            },

            {
                "question":
                "Which language is widely used in Data Science?",

                "options": [
                    "Python",
                    "HTML",
                    "CSS",
                    "XML"
                ],

                "answer": "Python"
            },

            {
                "question":
                "Which library is used for numerical computing?",

                "options": [
                    "NumPy",
                    "Django",
                    "Flask",
                    "Tkinter"
                ],

                "answer": "NumPy"
            },

            {
                "question":
                "Which library is commonly used for data analysis?",

                "options": [
                    "Pandas",
                    "React",
                    "Django",
                    "Bootstrap"
                ],

                "answer": "Pandas"
            },

            {
                "question":
                "What is the process of training a model using data called?",

                "options": [
                    "Machine Learning",
                    "Web Designing",
                    "Debugging",
                    "Compilation"
                ],

                "answer": "Machine Learning"
            },

            {
                "question":
                "Which algorithm can be used for classification?",

                "options": [
                    "Decision Tree",
                    "HTML",
                    "SQL",
                    "CSS"
                ],

                "answer": "Decision Tree"
            },

            {
                "question":
                "What does CSV stand for?",

                "options": [
                    "Comma Separated Values",
                    "Computer Stored Values",
                    "Common Separated Variables",
                    "Comma Stored Variables"
                ],

                "answer": "Comma Separated Values"
            },

            {
                "question":
                "Which technique is used to handle missing data?",

                "options": [
                    "Imputation",
                    "Compilation",
                    "Encryption",
                    "Rendering"
                ],

                "answer": "Imputation"
            },

            {
                "question":
                "What is a dataset?",

                "options": [
                    "A collection of data",
                    "A programming language",
                    "A computer",
                    "A database command"
                ],

                "answer": "A collection of data"
            }
        ]
    }

}


# =========================================================
# DASHBOARD
# =========================================================

@login_required
def dashboard(request):

    results = TestResult.objects.filter(
        user=request.user
    ).order_by('-date_time')

    total_tests = results.count()

    if total_tests > 0:

        total_score = sum(
            result.score
            for result in results
        )

        total_questions = sum(
            result.total_questions
            for result in results
        )

        if total_questions > 0:

            average_score = round(
                (total_score / total_questions) * 100
            )

        else:

            average_score = 0

    else:

        average_score = 0


    return render(
        request,
        'dashboard.html',
        {
            'results': results,
            'total_tests': total_tests,
            'average_score': average_score
        }
    )


# =========================================================
# TEST PAGE
# =========================================================

@login_required
def test_page(request, test_id):

    test = TESTS.get(test_id)

    if not test:

        messages.error(
            request,
            'Test not found.'
        )

        return redirect('dashboard')


    if request.method == 'POST':

        correct = 0

        attempted = 0

        total_questions = len(
            test['questions']
        )


        for index, question in enumerate(
            test['questions']
        ):

            selected_answer = request.POST.get(
                f'question_{index}'
            )


            if selected_answer:

                attempted += 1


                if selected_answer == question['answer']:

                    correct += 1


        wrong = attempted - correct

        skipped = total_questions - attempted


        result = TestResult.objects.create(

            user=request.user,

            test_name=test['name'],

            total_questions=total_questions,

            attempted=attempted,

            correct=correct,

            wrong=wrong,

            skipped=skipped,

            score=correct
        )


        return redirect(
            'result',
            result_id=result.id
        )


    return render(
        request,
        'test.html',
        {
            'test': test,
            'test_id': test_id
        }
    )


# =========================================================
# RESULT
# =========================================================

@login_required
def result(request, result_id):

    result = get_object_or_404(
        TestResult,
        id=result_id,
        user=request.user
    )

    return render(
        request,
        'result.html',
        {
            'result': result
        }
    )


# =========================================================
# HISTORY
# =========================================================

@login_required
def history(request):

    results = TestResult.objects.filter(
        user=request.user
    ).order_by('-date_time')


    return render(
        request,
        'history.html',
        {
            'results': results
        }
    )