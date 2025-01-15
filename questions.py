
# Quiz questions
quiz_data = [
    {"question": "What is the output of `print(2**3)`?", 
     "options": ["6", "8", "9", "12"], "answer": "8", "tech": "python", "tech": "python"},
    {"question": "Which data type is mutable in Python?", 
     "options": ["tuple", "string", "list", "int"], "answer": "list", "tech": "python", "tech": "python"},
    {"question": "What does `len()` do in Python?", 
     "options": ["Finds length", "Sorts list", "Checks type", "Converts type"], "answer": "Finds length", "tech": "python", "tech": "python"},
    {"question": "Which keyword is used to create a function in Python?", 
     "options": ["function", "define", "def", "lambda"], "answer": "def", "tech": "python", "tech": "python"},
    {"question": "What is the time complexity of accessing an element in a dictionary?", 
     "options": ["O(1)", "O(n)", "O(log n)", "O(n^2)"], "answer": "O(1)", "tech": "python", "tech": "python"},

    {"question": "What is the output of `[1,2,3] + [4,5,6]`?", 
     "options": ["[1,2,3,4,5,6]", "[1,2,3],[4,5,6]", "Error", "[5,7,9]"], 
     "answer": "[1,2,3,4,5,6]", "tech": "python", "tech": "python"},
    
    {"question": "Which method adds an element to the end of a list?", 
     "options": ["append()", "extend()", "insert()", "add()"], 
     "answer": "append()", "tech": "python"},
    
    {"question": "What is the output of `[1,2,3].pop()`?", 
     "options": ["1", "2", "3", "[1,2]"], 
     "answer": "3", "tech": "python"},
    
    {"question": "How do you get the length of list `my_list`?", 
     "options": ["my_list.length()", "my_list.size()", "len(my_list)", "size(my_list)"], 
     "answer": "len(my_list)", "tech": "python"},
    
    {"question": "What is the time complexity of `list.append()`?", 
     "options": ["O(1)", "O(n)", "O(log n)", "O(n^2)"], 
     "answer": "O(1)", "tech": "python"},
    
    {"question": "How do you access the last element of list `lst`?", 
     "options": ["lst[-1]", "lst[end]", "lst[len(lst)]", "lst.last()"], 
     "answer": "lst[-1]", "tech": "python"},
    
    {"question": "What does `lst.extend([4,5])` do?", 
     "options": ["Adds [4,5] as one element", "Adds 4 and 5 individually", "Creates new list", "Raises error"], 
     "answer": "Adds 4 and 5 individually", "tech": "python"},
    
    {"question": "What is the output of `[x*2 for x in [1,2,3]]`?", 
     "options": ["[2,4,6]", "[1,2,3,1,2,3]", "[1,4,9]", "Error"], 
     "answer": "[2,4,6]", "tech": "python"},
    
    {"question": "How do you remove first occurrence of value 'x' from list?", 
     "options": ["list.remove('x')", "list.pop('x')", "list.delete('x')", "del list['x']"], 
     "answer": "list.remove('x')", "tech": "python"},
    
    {"question": "What is `lst[::2]`?", 
     "options": ["Every second element", "First two elements", "Last two elements", "Middle elements"], 
     "answer": "Every second element", "tech": "python"},
    
    {"question": "What is the output of `[1,2,3].index(2)`?", 
     "options": ["1", "2", "3", "Error"], 
     "answer": "1", "tech": "python"},
    
    {"question": "How do you reverse a list in place?", 
     "options": ["list.reverse()", "reversed(list)", "list[::-1]", "list.sort(reverse=True)"], 
     "answer": "list.reverse()", "tech": "python"},
    
    {"question": "What is the output of `list('python')`?", 
     "options": ["['p','y','t','h','o','n']", "'python'", "['python']", "Error"], 
     "answer": "['p','y','t','h','o','n']", "tech": "python"},
    
    {"question": "Which creates empty list?", 
     "options": ["[]", "list()", "Both A and B", "None"], 
     "answer": "Both A and B", "tech": "python"},
    
    {"question": "What is the time complexity of `in` operator for lists?", 
     "options": ["O(n)", "O(1)", "O(log n)", "O(n^2)"], 
     "answer": "O(n)", "tech": "python"},
    
    {"question": "What does `sorted(lst)` return?", 
     "options": ["New sorted list", "None", "Original list sorted", "Error"], 
     "answer": "New sorted list", "tech": "python"},
    
    {"question": "How to get first 3 elements of list?", 
     "options": ["lst[:3]", "lst[0:3]", "Both A and B", "lst[3]"], 
     "answer": "Both A and B", "tech": "python"},
    
    {"question": "What is `[0] * 3`?", 
     "options": ["[0,0,0]", "[3]", "[0]", "Error"], 
     "answer": "[0,0,0]", "tech": "python"},
    
    {"question": "How to check if list is empty?", 
     "options": ["if not lst:", "if lst == []", "Both A and B", "if lst.empty()"], 
     "answer": "Both A and B", "tech": "python"},
    
    {"question": "What does `del lst[1:3]` do?", 
     "options": ["Removes elements 1 through 2", "Removes elements 1 through 3", "Removes first 3 elements", "Removes last element"], 
     "answer": "Removes elements 1 through 2", "tech": "python"},

    {"question": "What is the output of `{'a':1, 'b':2}.keys()`?", 
     "options": ["['a', 'b']", "('a', 'b')", "dict_keys(['a', 'b'])", "{a, b}"], 
     "answer": "dict_keys(['a', 'b'])", "tech": "python"},
    
    {"question": "How do you create an empty dictionary?", 
     "options": ["{}", "dict()", "Both A and B", "[]"], 
     "answer": "Both A and B", "tech": "python"},
    
    {"question": "What is the time complexity of dictionary lookup?", 
     "options": ["O(1)", "O(n)", "O(log n)", "O(n^2)"], 
     "answer": "O(1)", "tech": "python"},
    
    {"question": "What happens if you access missing key without get()?", 
     "options": ["KeyError", "None", "False", "Empty string"], 
     "answer": "KeyError", "tech": "python"},
    
    {"question": "What does `dict.get(key, default)` do?", 
     "options": ["Returns default if key missing", "Raises error", "Always returns default", "Returns None"], 
     "answer": "Returns default if key missing", "tech": "python"},
    
    {"question": "How to merge two dictionaries in Python 3.9+?", 
     "options": ["dict1 | dict2", "dict1 + dict2", "dict1.merge(dict2)", "dict1.update(dict2)"], 
     "answer": "dict1 | dict2", "tech": "python"},
    
    {"question": "What is `{x:x*2 for x in range(3)}`?", 
     "options": ["{0:0, 1:2, 2:4}", "[0,2,4]", "{0,2,4}", "Error"], 
     "answer": "{0:0, 1:2, 2:4}", "tech": "python"},
    
    {"question": "How to remove key 'k' from dictionary?", 
     "options": ["del dict['k']", "dict.remove('k')", "dict.pop('k')", "Both A and C"], 
     "answer": "Both A and C", "tech": "python"},
    
    {"question": "What method returns (key,value) pairs?", 
     "options": ["items()", "pairs()", "elements()", "values()"], 
     "answer": "items()", "tech": "python"},
    
    {"question": "What is `dict.setdefault(key,val)` used for?", 
     "options": ["Set default if key missing", "Always set value", "Remove key", "Check if key exists"], 
     "answer": "Set default if key missing", "tech": "python"},
    
    {"question": "How to check if key exists in dict?", 
     "options": ["key in dict", "dict.has_key(key)", "dict.contains(key)", "key.exists(dict)"], 
     "answer": "key in dict", "tech": "python"},
    
    {"question": "What happens: `dict1.update(dict2)`?", 
     "options": ["Updates dict1 in place", "Creates new dict", "Returns merged dict", "Updates dict2"], 
     "answer": "Updates dict1 in place", "tech": "python"},
    
    {"question": "Valid dictionary key types include:", 
     "options": ["str,int,tuple", "list,set,dict", "None,bool,float", "All mentioned"], 
     "answer": "str,int,tuple", "tech": "python"},
    
    {"question": "What is `dict.fromkeys(['a','b'], 0)`?", 
     "options": ["{'a':0, 'b':0}", "['a','b']", "{0:'a', 1:'b'}", "Error"], 
     "answer": "{'a':0, 'b':0}", "tech": "python"},
    
    {"question": "How to get all values from dict?", 
     "options": ["dict.values()", "dict.get()", "dict.items()", "dict.keys()"], 
     "answer": "dict.values()", "tech": "python"},
    
    {"question": "What happens: `dict[missing_key] = val`?", 
     "options": ["Adds new key-value", "Raises error", "Returns None", "Updates existing"], 
     "answer": "Adds new key-value", "tech": "python"},
    
    {"question": "Best way to copy a dictionary?", 
     "options": ["dict.copy()", "dict[:]", "dict()", "list(dict)"], 
     "answer": "dict.copy()", "tech": "python"},
    
    {"question": "What is `{**dict1, **dict2}`?", 
     "options": ["Merges dictionaries", "Creates tuple", "Raises error", "Creates set"], 
     "answer": "Merges dictionaries", "tech": "python"},
    
    {"question": "Time complexity of `key in dict`?", 
     "options": ["O(1)", "O(n)", "O(log n)", "O(n^2)"], 
     "answer": "O(1)", "tech": "python"},
    
    {"question": "What does `dict.clear()` return?", 
     "options": ["None", "Empty dict", "Original dict", "Error"], 
     "answer": "None", "tech": "python"},

    {"question": "What is the output of `1 if True else 0`?", 
     "options": ["1", "0", "True", "Error"], 
     "answer": "1", "tech": "python"},
    
    {"question": "Which statement exits a loop completely?", 
     "options": ["break", "continue", "pass", "return"], 
     "answer": "break", "tech": "python"},
    
    {"question": "What does `while True:` create?", 
     "options": ["Infinite loop", "Single iteration", "Syntax error", "Empty loop"], 
     "answer": "Infinite loop", "tech": "python"},
    
    {"question": "Which is valid in a for loop?", 
     "options": ["else clause", "elif clause", "case clause", "when clause"], 
     "answer": "else clause", "tech": "python"},
    
    {"question": "What does `pass` do?", 
     "options": ["Nothing", "Breaks loop", "Continues loop", "Raises error"], 
     "answer": "Nothing", "tech": "python"},
    
    {"question": "Which creates a generator?", 
     "options": ["yield keyword", "gen()", "make_generator()", "create()"], 
     "answer": "yield keyword", "tech": "python"},
    
    {"question": "What does `try/finally` ensure?", 
     "options": ["Cleanup code runs", "No errors occur", "Better performance", "Multiple attempts"], 
     "answer": "Cleanup code runs", "tech": "python"},
    
    {"question": "Which is correct ternary syntax?", 
     "options": ["a if b else c", "if b then a else c", "b ? a : c", "if b: a else: c"], 
     "answer": "a if b else c", "tech": "python"},
    
    {"question": "What catches all exceptions?", 
     "options": ["except:", "except *:", "except all:", "except Exception:"], 
     "answer": "except:", "tech": "python"},
    
    {"question": "Valid context manager keyword?", 
     "options": ["with", "using", "context", "manage"], 
     "answer": "with", "tech": "python"},
    
    {"question": "What does `else` in try/except do?", 
     "options": ["Runs if no exception", "Always runs", "Runs on error", "Never runs"], 
     "answer": "Runs if no exception", "tech": "python"},
    
    {"question": "Which is not a loop control?", 
     "options": ["skip", "break", "continue", "pass"], 
     "answer": "skip", "tech": "python"},
    
    {"question": "What creates list comprehension?", 
     "options": ["Square brackets", "Parentheses", "Curly braces", "Angle brackets"], 
     "answer": "Square brackets", "tech": "python"},
    
    {"question": "When does `finally` run?", 
     "options": ["Always", "On success", "On error", "Never"], 
     "answer": "Always", "tech": "python"},
    
    {"question": "Valid in match/case statement?", 
     "options": ["case _:", "default:", "else:", "otherwise:"], 
     "answer": "case _:", "tech": "python"},
    
    {"question": "How to skip loop iteration?", 
     "options": ["continue", "skip", "next", "pass"], 
     "answer": "continue", "tech": "python"},
    
    {"question": "What does `for/else` do?", 
     "options": ["Runs if no break", "Always runs", "Never runs", "Runs on break"], 
     "answer": "Runs if no break", "tech": "python"},
    
    {"question": "Which checks multiple conditions?", 
     "options": ["elif", "else if", "otherwise", "or if"], 
     "answer": "elif", "tech": "python"},
    
    {"question": "Generator expression uses:", 
     "options": ["Parentheses", "Square brackets", "Curly braces", "Angle brackets"], 
     "answer": "Parentheses", "tech": "python"},
    
    {"question": "Valid way to raise error?", 
     "options": ["raise ValueError", "throw ValueError", "error ValueError", "except ValueError"], 
     "answer": "raise ValueError", "tech": "python"},

    {"question": "What does `*args` in a function do?", 
     "options": ["Accepts multiple positional args", "Accepts keyword args", "Marks as private", "Creates generator"], 
     "answer": "Accepts multiple positional args", "tech": "python"},
    
    {"question": "Which creates a lambda function?", 
     "options": ["lambda x: x*2", "def lambda(x): x*2", "function(x): x*2", "anonymous(x): x*2"], 
     "answer": "lambda x: x*2", "tech": "python"},
    
    {"question": "What's the purpose of `**kwargs`?", 
     "options": ["Accept keyword arguments", "Unpack dictionary", "Both A and B", "Create dictionary"], 
     "answer": "Both A and B", "tech": "python"},
    
    {"question": "How to document a function?", 
     "options": ["Docstring", "# comments", "/** */", "<!-- -->"], 
     "answer": "Docstring", "tech": "python"},
    
    {"question": "Valid function return types:", 
     "options": ["Any Python object", "Only one value", "Maximum two values", "Numbers only"], 
     "answer": "Any Python object", "tech": "python"},
    
    {"question": "What is a decorator?", 
     "options": ["Function modifier", "Class creator", "Variable type", "Import statement"], 
     "answer": "Function modifier", "tech": "python"},
    
    {"question": "Default arguments are evaluated:", 
     "options": ["At definition time", "At runtime", "When called", "Never"], 
     "answer": "At definition time", "tech": "python"},
    
    {"question": "Purpose of `global` keyword?", 
     "options": ["Modify global variable", "Create global", "Import global", "Delete global"], 
     "answer": "Modify global variable", "tech": "python"},
    
    {"question": "What does `return` alone do?", 
     "options": ["Returns None", "Error", "Exits program", "Continues execution"], 
     "answer": "Returns None", "tech": "python"},
    
    {"question": "Function type hints use:", 
     "options": ["-> notation", "@ notation", "# notation", "$ notation"], 
     "answer": "-> notation", "tech": "python"},
    
    {"question": "What creates closure?", 
     "options": ["Nested function", "Class method", "Global variable", "Module import"], 
     "answer": "Nested function", "tech": "python"},
    
    {"question": "Valid decorator syntax:", 
     "options": ["@decorator", "@(decorator)", "decorator@", "#decorator"], 
     "answer": "@decorator", "tech": "python"},
    
    {"question": "Purpose of `nonlocal`?", 
     "options": ["Modify enclosing scope", "Create global", "Import function", "Delete variable"], 
     "answer": "Modify enclosing scope", "tech": "python"},
    
    {"question": "What is `func.__name__`?", 
     "options": ["Function name string", "Memory address", "Return value", "Documentation"], 
     "answer": "Function name string", "tech": "python"},
    
    {"question": "How to unpack arguments?", 
     "options": ["*list, **dict", "*args", "**kwargs", "unpack()"], 
     "answer": "*list, **dict", "tech": "python"},
    
    {"question": "First class functions can:", 
     "options": ["Be passed as args", "Be declared only", "Not be assigned", "Not be returned"], 
     "answer": "Be passed as args", "tech": "python"},
    
    {"question": "Purpose of `partial()`?", 
     "options": ["Fix some arguments", "Split function", "Merge functions", "Delete function"], 
     "answer": "Fix some arguments", "tech": "python"},
    
    {"question": "Valid in function body:", 
     "options": ["yield", "async", "Both A and B", "None"], 
     "answer": "Both A and B", "tech": "python"},
    
    {"question": "What is recursion limit?", 
     "options": ["1000 by default", "100 by default", "Unlimited", "System dependent"], 
     "answer": "1000 by default", "tech": "python"},
    
    {"question": "Purpose of `__call__`?", 
     "options": ["Make object callable", "Create function", "Delete function", "Rename function"], 
     "answer": "Make object callable"}
]

# quiz_data2 = [{**q, "tech": "python"} for q in quiz_data]