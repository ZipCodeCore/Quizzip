
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
#

git1_questions = [
    {"question": "What Git command creates a new repository?",
     "options": ["git init", "git start", "git create", "git new"],
     "answer": "git init", "tech": "github"},

    {"question": "How do you clone a repository?",
     "options": ["git clone <url>", "git copy <url>", "git download <url>", "git pull <url>"],
     "answer": "git clone <url>", "tech": "github"},

    {"question": "What command shows commit history?",
     "options": ["git log", "git history", "git show", "git commits"],
     "answer": "git log", "tech": "github"},

    {"question": "How to stage all changes?",
     "options": ["git add .", "git stage all", "git commit all", "git push all"],
     "answer": "git add .", "tech": "github"},

    {"question": "What creates a new branch?",
     "options": ["git branch <name>", "git new branch", "git create <name>", "git checkout new"],
     "answer": "git branch <name>", "tech": "github"},

    {"question": "How to switch branches?",
     "options": ["git checkout <branch>", "git switch <branch>", "git change <branch>", "git move <branch>"],
     "answer": "git checkout <branch>", "tech": "github"},

    {"question": "What does `git pull` do?",
     "options": ["Fetches and merges changes", "Only fetches changes", "Pushes local changes", "Creates new branch"],
     "answer": "Fetches and merges changes", "tech": "github"},

    {"question": "How to discard local changes?",
     "options": ["git checkout -- <file>", "git discard <file>", "git remove changes", "git clean <file>"],
     "answer": "git checkout -- <file>", "tech": "github"},

    {"question": "What shows modified files?",
     "options": ["git status", "git show", "git modified", "git changes"],
     "answer": "git status", "tech": "github"},

    {"question": "How to rename a branch?",
     "options": ["git branch -m <name>", "git rename branch", "git change name", "git modify branch"],
     "answer": "git branch -m <name>", "tech": "github"},

    {"question": "What command deletes a branch?",
     "options": ["git branch -d <name>", "git delete <name>", "git remove branch", "git clean branch"],
     "answer": "git branch -d <name>", "tech": "github"},

    {"question": "How to create and switch to new branch?",
     "options": ["git checkout -b <name>", "git branch new", "git create switch", "git new checkout"],
     "answer": "git checkout -b <name>", "tech": "github"},

    {"question": "What lists all branches?",
     "options": ["git branch", "git show branches", "git list", "git all"],
     "answer": "git branch", "tech": "github"},

    {"question": "How to merge branches?",
     "options": ["git merge <branch>", "git combine <branch>", "git join <branch>", "git unite <branch>"],
     "answer": "git merge <branch>", "tech": "github"},

    {"question": "What shows commit differences?",
     "options": ["git diff", "git show diff", "git compare", "git changes"],
     "answer": "git diff", "tech": "github"},

    {"question": "How to add remote repository?",
     "options": ["git remote add origin <url>", "git add remote", "git create remote", "git new remote"],
     "answer": "git remote add origin <url>", "tech": "github"},

    {"question": "What creates a tag?",
     "options": ["git tag <name>", "git create tag", "git new tag", "git add tag"],
     "answer": "git tag <name>", "tech": "github"},

    {"question": "How to push tags to remote?",
     "options": ["git push --tags", "git push tags", "git upload tags", "git send tags"],
     "answer": "git push --tags", "tech": "github"},

    {"question": "What removes a file from git?",
     "options": ["git rm <file>", "git delete <file>", "git remove <file>", "git clean <file>"],
     "answer": "git rm <file>", "tech": "github"},

    {"question": "How to stash changes?",
     "options": ["git stash", "git save", "git store", "git hide"],
     "answer": "git stash", "tech": "github"},

    {"question": "What applies stashed changes?",
     "options": ["git stash apply", "git stash use", "git stash get", "git stash pull"],
     "answer": "git stash apply", "tech": "github"},

    {"question": "How to view remote URLs?",
     "options": ["git remote -v", "git show remote", "git list remote", "git urls"],
     "answer": "git remote -v", "tech": "github"},

    {"question": "What shows branch graphs?",
     "options": ["git log --graph", "git show graph", "git branch graph", "git tree"],
     "answer": "git log --graph", "tech": "github"},

    {"question": "How to revert last commit?",
     "options": ["git revert HEAD", "git undo commit", "git remove commit", "git delete commit"],
     "answer": "git revert HEAD", "tech": "github"},

    {"question": "What shows commit details?",
     "options": ["git show <commit>", "git detail <commit>", "git info <commit>", "git read <commit>"],
     "answer": "git show <commit>", "tech": "github"},

    {"question": "How to force push changes?",
     "options": ["git push -f", "git push force", "git force push", "git override push"],
     "answer": "git push -f", "tech": "github"},

    {"question": "What creates .gitignore?",
     "options": ["touch .gitignore", "git ignore create", "git new ignore", "git make ignore"],
     "answer": "touch .gitignore", "tech": "github"},

    {"question": "How to see commit author?",
     "options": ["git log --author", "git show author", "git who", "git blame"],
     "answer": "git log --author", "tech": "github"},

    {"question": "What fetches from remote?",
     "options": ["git fetch", "git download", "git get", "git retrieve"],
     "answer": "git fetch", "tech": "github"},

    {"question": "How to rename remote?",
     "options": ["git remote rename", "git change remote", "git modify remote", "git update remote"],
     "answer": "git remote rename", "tech": "github"}
]

# Extend the existing quiz_data with new questions
quiz_data.extend(git1_questions)

git2_questions = [
    {"question": "What's the purpose of .github/workflows?",
     "options": ["Store GitHub Actions", "Keep documentation", "Store images", "Configure settings"],
     "answer": "Store GitHub Actions", "tech": "github"},

    {"question": "How to create a pull request template?",
     "options": ["Add PULL_REQUEST_TEMPLATE.md", "Create pr_template.txt", "Use template.yaml", "Edit settings.json"],
     "answer": "Add PULL_REQUEST_TEMPLATE.md", "tech": "github"},

    {"question": "What indicates a GitHub repo is a template?",
     "options": ["Green 'Use this template' button", "Template label", "Special icon", "README badge"],
     "answer": "Green 'Use this template' button", "tech": "github"},

    {"question": "Where are GitHub Actions secrets stored?",
     "options": ["Repository settings", "Actions folder", "Security tab", "Config files"],
     "answer": "Repository settings", "tech": "github"},

    {"question": "What creates GitHub release notes?",
     "options": ["Releases tab", "README file", "Actions workflow", "Issues page"],
     "answer": "Releases tab", "tech": "github"},

    {"question": "How to enable GitHub Pages?",
     "options": ["Repository settings", "Pages folder", "Actions workflow", "Special branch"],
     "answer": "Repository settings", "tech": "github"},

    {"question": "What's the default branch protection rule?",
     "options": ["None", "Require reviews", "Block force push", "Require tests"],
     "answer": "None", "tech": "github"},

    {"question": "Where to configure branch rules?",
     "options": ["Settings/Branches", "Security tab", "Actions page", "Repo front page"],
     "answer": "Settings/Branches", "tech": "github"},

    {"question": "What shows repo traffic data?",
     "options": ["Insights tab", "Analytics page", "Statistics view", "Traffic folder"],
     "answer": "Insights tab", "tech": "github"},

    {"question": "How to mark issue as duplicate?",
     "options": ["Comment 'duplicate of #X'", "Use label", "Close issue", "Mark checkbox"],
     "answer": "Comment 'duplicate of #X'", "tech": "github"},

    {"question": "What triggers GitHub Actions workflow?",
     "options": ["on: push specification", "run: command", "trigger: event", "action: start"],
     "answer": "on: push specification", "tech": "github"},

    {"question": "Default visibility for new repo?",
     "options": ["Public", "Private", "Internal", "Protected"],
     "answer": "Private", "tech": "github"},

    {"question": "What shows code frequency?",
     "options": ["Insights/Code frequency", "Statistics tab", "Commits page", "Analytics view"],
     "answer": "Insights/Code frequency", "tech": "github"},

    {"question": "How to lock conversations?",
     "options": ["Lock conversation button", "Security settings", "Moderation tab", "Admin panel"],
     "answer": "Lock conversation button", "tech": "github"},

    {"question": "What's a GitHub gist?",
     "options": ["Code snippet", "Issue template", "Pull request", "Action workflow"],
     "answer": "Code snippet", "tech": "github"},

    {"question": "Purpose of CODEOWNERS file?",
     "options": ["Assign review responsibilities", "Set permissions", "List contributors", "Track changes"],
     "answer": "Assign review responsibilities", "tech": "github"},

    {"question": "Where to set repo description?",
     "options": ["About section", "README file", "Settings page", "Profile view"],
     "answer": "About section", "tech": "github"},

    {"question": "What shows repo dependencies?",
     "options": ["Insights/Dependency graph", "Package list", "Requirements file", "Security tab"],
     "answer": "Insights/Dependency graph", "tech": "github"},

    {"question": "How to archive a repository?",
     "options": ["Settings/Archive", "Delete option", "Close repo", "Mark inactive"],
     "answer": "Settings/Archive", "tech": "github"},

    {"question": "What creates issue templates?",
     "options": [".github/ISSUE_TEMPLATE/", "templates/", "docs/", ".issues/"],
     "answer": ".github/ISSUE_TEMPLATE/", "tech": "github"},

    {"question": "Default branch name setting location?",
     "options": ["Repository settings", "Global settings", "Branch page", "Config file"],
     "answer": "Repository settings", "tech": "github"},

    {"question": "How to enable discussions?",
     "options": ["Settings/Features", "Discussions tab", "Community page", "Forum settings"],
     "answer": "Settings/Features", "tech": "github"},

    {"question": "What shows contribution activity?",
     "options": ["Profile contribution graph", "Activity tab", "Statistics page", "Timeline view"],
     "answer": "Profile contribution graph", "tech": "github"},

    {"question": "How to transfer repository ownership?",
     "options": ["Settings/Transfer", "Admin panel", "Permissions page", "Owner tab"],
     "answer": "Settings/Transfer", "tech": "github"},

    {"question": "What creates release tags?",
     "options": ["Releases page", "Tags section", "Version control", "Branch settings"],
     "answer": "Releases page", "tech": "github"},

    {"question": "How to set repo topics?",
     "options": ["About section", "Tags page", "Categories tab", "Settings menu"],
     "answer": "About section", "tech": "github"},

    {"question": "What shows repo network?",
     "options": ["Insights/Network", "Connections tab", "Graph view", "Tree diagram"],
     "answer": "Insights/Network", "tech": "github"},

    {"question": "How to enable wikis?",
     "options": ["Settings/Features", "Wiki tab", "Docs section", "Pages settings"],
     "answer": "Settings/Features", "tech": "github"},

    {"question": "What shows security alerts?",
     "options": ["Security tab", "Alerts page", "Issues list", "Notifications"],
     "answer": "Security tab", "tech": "github"},

    {"question": "How to set repository visibility?",
     "options": ["Settings/Danger Zone", "Privacy tab", "Security settings", "Access control"],
     "answer": "Settings/Danger Zone", "tech": "github"}
]

# Extend the quiz_data with more questions
quiz_data.extend(git2_questions)

java_questions = [
    {"question": "What is the default value of int variable?",
     "options": ["0", "null", "undefined", "1"],
     "answer": "0", "tech": "java"},

    {"question": "Which is not a valid access modifier?",
     "options": ["friendly", "public", "private", "protected"],
     "answer": "friendly", "tech": "java"},

    {"question": "What is the size of double in Java?",
     "options": ["8 bytes", "4 bytes", "2 bytes", "1 byte"],
     "answer": "8 bytes", "tech": "java"},

    {"question": "ArrayList implements which interface?",
     "options": ["List", "Set", "Map", "Queue"],
     "answer": "List", "tech": "java"},

    {"question": "What does JVM stand for?",
     "options": ["Java Virtual Machine", "Java Video Machine", "Java Visual Machine", "Java Vital Machine"],
     "answer": "Java Virtual Machine", "tech": "java"},

    {"question": "Which collection is thread-safe?",
     "options": ["Vector", "ArrayList", "LinkedList", "HashMap"],
     "answer": "Vector", "tech": "java"},

    {"question": "What does 'final' keyword do?",
     "options": ["Prevents inheritance", "Allows inheritance", "Creates interface", "None"],
     "answer": "Prevents inheritance", "tech": "java"},

    {"question": "String objects are stored in:",
     "options": ["String Pool", "Heap Memory", "Stack Memory", "Cache"],
     "answer": "String Pool", "tech": "java"},

    {"question": "Which interface has compareTo() method?",
     "options": ["Comparable", "Comparator", "Both", "Neither"],
     "answer": "Comparable", "tech": "java"},

    {"question": "What is autoboxing?",
     "options": ["Primitive to Wrapper", "Wrapper to Primitive", "Type casting", "Type checking"],
     "answer": "Primitive to Wrapper", "tech": "java"},

    {"question": "HashSet implements which interface?",
     "options": ["Set", "List", "Map", "Queue"],
     "answer": "Set", "tech": "java"},

    {"question": "What is marker interface?",
     "options": ["Empty interface", "Functional interface", "Abstract interface", "Static interface"],
     "answer": "Empty interface", "tech": "java"},

    {"question": "Which collection allows duplicates?",
     "options": ["ArrayList", "HashSet", "TreeSet", "LinkedHashSet"],
     "answer": "ArrayList", "tech": "java"},

    {"question": "What is the parent class of all classes?",
     "options": ["Object", "String", "Class", "Main"],
     "answer": "Object", "tech": "java"},

    {"question": "Which is immutable class?",
     "options": ["String", "StringBuilder", "StringBuffer", "None"],
     "answer": "String", "tech": "java"},

    {"question": "What does static keyword do?",
     "options": ["Class level member", "Instance member", "Local variable", "Parameter"],
     "answer": "Class level member", "tech": "java"},

    {"question": "Which operator is right associative?",
     "options": ["=", "+", "*", "-"],
     "answer": "=", "tech": "java"},

    {"question": "What is constructor overloading?",
     "options": ["Multiple constructors", "Multiple methods", "Multiple classes", "Multiple interfaces"],
     "answer": "Multiple constructors", "tech": "java"},

    {"question": "Which collection is ordered?",
     "options": ["LinkedHashMap", "HashMap", "HashSet", "TreeSet"],
     "answer": "LinkedHashMap", "tech": "java"},

    {"question": "What is method overriding?",
     "options": ["Same method in subclass", "Different method in subclass", "New method in subclass", "Abstract method"],
     "answer": "Same method in subclass", "tech": "java"},

    {"question": "Default interface methods are:",
     "options": ["public", "private", "protected", "package-private"],
     "answer": "public", "tech": "java"},

    {"question": "Which supports multiple inheritance?",
     "options": ["Interfaces", "Classes", "Abstract classes", "None"],
     "answer": "Interfaces", "tech": "java"},

    {"question": "What is try-with-resources?",
     "options": ["Auto resource management", "Exception handling", "File handling", "Thread management"],
     "answer": "Auto resource management", "tech": "java"},

    {"question": "Which collection is LIFO?",
     "options": ["Stack", "Queue", "List", "Set"],
     "answer": "Stack", "tech": "java"},

    {"question": "What is lambda expression?",
     "options": ["Anonymous function", "Named function", "Static method", "Abstract method"],
     "answer": "Anonymous function", "tech": "java"},

    {"question": "Which package is imported by default?",
     "options": ["java.lang", "java.util", "java.io", "java.net"],
     "answer": "java.lang", "tech": "java"},

    {"question": "What is the scope of package-private?",
     "options": ["Same package", "All packages", "Subclasses", "Same class"],
     "answer": "Same package", "tech": "java"},

    {"question": "Which is not a primitive type?",
     "options": ["String", "int", "char", "boolean"],
     "answer": "String", "tech": "java"},

    {"question": "What does volatile keyword do?",
     "options": ["Thread visibility", "Thread safety", "Thread creation", "Thread scheduling"],
     "answer": "Thread visibility", "tech": "java"},

    {"question": "Which collection is synchronized?",
     "options": ["Hashtable", "HashMap", "TreeMap", "LinkedHashMap"],
     "answer": "Hashtable", "tech": "java"}
]

# Extend the quiz_data with Java questions
quiz_data.extend(java_questions)

more_java_questions = [
    {"question": "What is the return type of main method?",
     "options": ["void", "int", "String", "Object"],
     "answer": "void", "tech": "java"},

    {"question": "Which stream reads binary data?",
     "options": ["DataInputStream", "BufferedReader", "Scanner", "PrintWriter"],
     "answer": "DataInputStream", "tech": "java"},

    {"question": "What is the size of char in Java?",
     "options": ["2 bytes", "1 byte", "4 bytes", "8 bytes"],
     "answer": "2 bytes", "tech": "java"},

    {"question": "Which interface is for sorting?",
     "options": ["Comparator", "Serializable", "Cloneable", "Runnable"],
     "answer": "Comparator", "tech": "java"},

    {"question": "What is a daemon thread?",
     "options": ["Background thread", "Main thread", "User thread", "System thread"],
     "answer": "Background thread", "tech": "java"},

    {"question": "Which class cannot be inherited?",
     "options": ["Final class", "Abstract class", "Static class", "Public class"],
     "answer": "Final class", "tech": "java"},

    {"question": "What is try-catch-finally order?",
     "options": ["try-catch-finally", "catch-try-finally", "finally-try-catch", "try-finally-catch"],
     "answer": "try-catch-finally", "tech": "java"},

    {"question": "What does instanceof operator check?",
     "options": ["Object type", "Method type", "Variable type", "Class type"],
     "answer": "Object type", "tech": "java"},

    {"question": "Which supports primitive arrays?",
     "options": ["Arrays class", "Collections class", "List interface", "Set interface"],
     "answer": "Arrays class", "tech": "java"},

    {"question": "What is method overloading?",
     "options": ["Different parameters", "Same parameters", "Different return type", "Same return type"],
     "answer": "Different parameters", "tech": "java"},

    {"question": "Which collection is thread-safe?",
     "options": ["ConcurrentHashMap", "HashMap", "TreeMap", "LinkedHashMap"],
     "answer": "ConcurrentHashMap", "tech": "java"},

    {"question": "What is default method access?",
     "options": ["package-private", "public", "private", "protected"],
     "answer": "package-private", "tech": "java"},

    {"question": "Which is checked exception?",
     "options": ["IOException", "NullPointerException", "ArrayIndexOutOfBoundsException", "ArithmeticException"],
     "answer": "IOException", "tech": "java"},

    {"question": "What does super keyword do?",
     "options": ["Calls parent method", "Calls child method", "Creates object", "Deletes object"],
     "answer": "Calls parent method", "tech": "java"},

    {"question": "Which collection is sorted?",
     "options": ["TreeSet", "HashSet", "LinkedHashSet", "ArrayList"],
     "answer": "TreeSet", "tech": "java"},

    {"question": "What is StringBuffer characteristic?",
     "options": ["Synchronized", "Not synchronized", "Immutable", "Fixed size"],
     "answer": "Synchronized", "tech": "java"},

    {"question": "Which is valid identifier?",
     "options": ["_name", "2name", "#name", "@name"],
     "answer": "_name", "tech": "java"},

    {"question": "What is default array value?",
     "options": ["null for objects", "0", "undefined", "false"],
     "answer": "null for objects", "tech": "java"},

    {"question": "Which interface is functional?",
     "options": ["Runnable", "Serializable", "Cloneable", "Random"],
     "answer": "Runnable", "tech": "java"},

    {"question": "What is anonymous class?",
     "options": ["Class without name", "Empty class", "Abstract class", "Final class"],
     "answer": "Class without name", "tech": "java"},

    {"question": "Which method is thread-safe?",
     "options": ["StringBuffer append", "StringBuilder append", "String concat", "Array copy"],
     "answer": "StringBuffer append", "tech": "java"},

    {"question": "What is polymorphism type?",
     "options": ["Runtime", "Compiletime", "Both", "Neither"],
     "answer": "Runtime", "tech": "java"},

    {"question": "Which supports variable arguments?",
     "options": ["varargs (...)", "array[]", "ArrayList", "Vector"],
     "answer": "varargs (...)", "tech": "java"},

    {"question": "What is default interface method?",
     "options": ["Has implementation", "No implementation", "Abstract", "Static"],
     "answer": "Has implementation", "tech": "java"},

    {"question": "Which is immutable class?",
     "options": ["Integer", "StringBuilder", "StringBuffer", "Array"],
     "answer": "Integer", "tech": "java"},

    {"question": "What is transient keyword for?",
     "options": ["Skip serialization", "Force serialization", "Enable threading", "Disable threading"],
     "answer": "Skip serialization", "tech": "java"},

    {"question": "Which collection is fail-fast?",
     "options": ["ArrayList", "CopyOnWriteArrayList", "Vector", "Stack"],
     "answer": "ArrayList", "tech": "java"},

    {"question": "What is static block used for?",
     "options": ["Class initialization", "Object initialization", "Method initialization", "Variable initialization"],
     "answer": "Class initialization", "tech": "java"},

    {"question": "Which supports multiple inheritance?",
     "options": ["Default methods", "Abstract classes", "Concrete classes", "Static methods"],
     "answer": "Default methods", "tech": "java"},

    {"question": "What is reflection used for?",
     "options": ["Runtime manipulation", "Compile time checking", "Code optimization", "Memory management"],
     "answer": "Runtime manipulation", "tech": "java"}
]

# Extend the quiz_data with more Java questions
quiz_data.extend(more_java_questions)

bash_questions = [
    {"question": "What command lists directory contents?",
     "options": ["ls", "dir", "list", "show"],
     "answer": "ls", "tech": "bash"},

    {"question": "How to change directory permissions?",
     "options": ["chmod", "chown", "chgrp", "chdir"],
     "answer": "chmod", "tech": "bash"},

    {"question": "What displays current directory?",
     "options": ["pwd", "cd", "dir", "path"],
     "answer": "pwd", "tech": "bash"},

    {"question": "How to create empty file?",
     "options": ["touch", "make", "create", "new"],
     "answer": "touch", "tech": "bash"},

    {"question": "Which redirects stdout and stderr?",
     "options": ["2>&1", ">", ">>", "<"],
     "answer": "2>&1", "tech": "bash"},

    {"question": "What shows running processes?",
     "options": ["ps", "proc", "top", "list"],
     "answer": "ps", "tech": "bash"},

    {"question": "How to search file contents?",
     "options": ["grep", "find", "search", "lookup"],
     "answer": "grep", "tech": "bash"},

    {"question": "What represents home directory?",
     "options": ["~", "/", "./", "../"],
     "answer": "~", "tech": "bash"},

    {"question": "How to display file contents?",
     "options": ["cat", "show", "display", "print"],
     "answer": "cat", "tech": "bash"},

    {"question": "Which finds files by name?",
     "options": ["find", "search", "locate", "grep"],
     "answer": "find", "tech": "bash"},

    {"question": "What shows disk usage?",
     "options": ["df", "du", "disk", "space"],
     "answer": "df", "tech": "bash"},

    {"question": "How to rename file?",
     "options": ["mv", "ren", "rename", "change"],
     "answer": "mv", "tech": "bash"},

    {"question": "What kills a process?",
     "options": ["kill", "end", "stop", "terminate"],
     "answer": "kill", "tech": "bash"},

    {"question": "How to create directory?",
     "options": ["mkdir", "md", "makedir", "create"],
     "answer": "mkdir", "tech": "bash"},

    {"question": "Which shows command history?",
     "options": ["history", "show", "past", "commands"],
     "answer": "history", "tech": "bash"},

    {"question": "What compresses files?",
     "options": ["tar", "zip", "compress", "archive"],
     "answer": "tar", "tech": "bash"},

    {"question": "How to check file type?",
     "options": ["file", "type", "what", "check"],
     "answer": "file", "tech": "bash"},

    {"question": "Which shows system info?",
     "options": ["uname", "sys", "info", "system"],
     "answer": "uname", "tech": "bash"},

    {"question": "What shows network connections?",
     "options": ["netstat", "network", "net", "conn"],
     "answer": "netstat", "tech": "bash"},

    {"question": "How to sort file contents?",
     "options": ["sort", "order", "arrange", "organize"],
     "answer": "sort", "tech": "bash"},

    {"question": "What shows file differences?",
     "options": ["diff", "compare", "cmp", "change"],
     "answer": "diff", "tech": "bash"},

    {"question": "How to count words in file?",
     "options": ["wc", "count", "words", "length"],
     "answer": "wc", "tech": "bash"},

    {"question": "Which shows calendar?",
     "options": ["cal", "calendar", "date", "time"],
     "answer": "cal", "tech": "bash"},

    {"question": "What shows system load?",
     "options": ["top", "load", "sys", "cpu"],
     "answer": "top", "tech": "bash"},

    {"question": "How to change file owner?",
     "options": ["chown", "owner", "change", "modify"],
     "answer": "chown", "tech": "bash"},

    {"question": "Which shows disk space?",
     "options": ["du", "disk", "space", "usage"],
     "answer": "du", "tech": "bash"},

    {"question": "What shows current user?",
     "options": ["whoami", "user", "who", "me"],
     "answer": "whoami", "tech": "bash"},

    {"question": "How to make script executable?",
     "options": ["chmod +x", "make exec", "run", "execute"],
     "answer": "chmod +x", "tech": "bash"},

    {"question": "Which shows file permissions?",
     "options": ["ls -l", "perms", "rights", "access"],
     "answer": "ls -l", "tech": "bash"},

    {"question": "What checks disk integrity?",
     "options": ["fsck", "check", "disk", "verify"],
     "answer": "fsck", "tech": "bash"}
]

# Extend the quiz_data with bash questions
quiz_data.extend(bash_questions)

more_bash_questions = [
    {"question": "What symbol represents pipeline?",
     "options": ["|", "&", ">>", "<<"],
     "answer": "|", "tech": "bash"},

    {"question": "How to view last n lines?",
     "options": ["tail -n", "head -n", "last -n", "end -n"],
     "answer": "tail -n", "tech": "bash"},

    {"question": "What's the 'not' operator in bash?",
     "options": ["!", "not", "~", "^"],
     "answer": "!", "tech": "bash"},

    {"question": "How to set environment variable?",
     "options": ["export VAR=value", "set VAR=value", "var VAR=value", "env VAR=value"],
     "answer": "export VAR=value", "tech": "bash"},

    {"question": "Which finds pattern in files?",
     "options": ["awk", "sed", "cut", "paste"],
     "answer": "awk", "tech": "bash"},

    {"question": "What represents background job?",
     "options": ["&", "#", "@", "$"],
     "answer": "&", "tech": "bash"},

    {"question": "How to view file start?",
     "options": ["head", "start", "begin", "top"],
     "answer": "head", "tech": "bash"},

    {"question": "What represents current process ID?",
     "options": ["$$", "$PID", "$@", "$#"],
     "answer": "$$", "tech": "bash"},

    {"question": "How to create symbolic link?",
     "options": ["ln -s", "link -s", "symlink", "mklink"],
     "answer": "ln -s", "tech": "bash"},

    {"question": "Which removes directory?",
     "options": ["rmdir", "deletedir", "remove", "deldir"],
     "answer": "rmdir", "tech": "bash"},

    {"question": "What shows memory usage?",
     "options": ["free", "mem", "memory", "ram"],
     "answer": "free", "tech": "bash"},

    {"question": "How to replace text in file?",
     "options": ["sed", "replace", "change", "modify"],
     "answer": "sed", "tech": "bash"},

    {"question": "What shows mounted filesystems?",
     "options": ["mount", "mnt", "mounted", "shows"],
     "answer": "mount", "tech": "bash"},

    {"question": "How to extract tar file?",
     "options": ["tar -xf", "untar", "extract", "decompress"],
     "answer": "tar -xf", "tech": "bash"},

    {"question": "Which shows CPU info?",
     "options": ["lscpu", "cpu", "processor", "cpuinfo"],
     "answer": "lscpu", "tech": "bash"},

    {"question": "What represents all arguments?",
     "options": ["$@", "$*", "$#", "$$"],
     "answer": "$@", "tech": "bash"},

    {"question": "How to join files horizontally?",
     "options": ["paste", "join", "merge", "combine"],
     "answer": "paste", "tech": "bash"},

    {"question": "Which command schedules tasks?",
     "options": ["crontab", "schedule", "task", "at"],
     "answer": "crontab", "tech": "bash"},

    {"question": "What shows hardware info?",
     "options": ["lshw", "hardware", "hw", "system"],
     "answer": "lshw", "tech": "bash"},

    {"question": "How to check file existence?",
     "options": ["-f file", "test file", "exists file", "check file"],
     "answer": "-f file", "tech": "bash"},

    {"question": "Which finds duplicate lines?",
     "options": ["uniq", "duplicate", "dup", "same"],
     "answer": "uniq", "tech": "bash"},

    {"question": "What shows block devices?",
     "options": ["lsblk", "block", "devices", "drives"],
     "answer": "lsblk", "tech": "bash"},

    {"question": "How to set file timestamp?",
     "options": ["touch -t", "time -t", "stamp", "date"],
     "answer": "touch -t", "tech": "bash"},

    {"question": "Which shows USB devices?",
     "options": ["lsusb", "usb", "devices", "hardware"],
     "answer": "lsusb", "tech": "bash"},

    {"question": "What shows process tree?",
     "options": ["pstree", "ptree", "processtree", "tree"],
     "answer": "pstree", "tech": "bash"},

    {"question": "How to create archive?",
     "options": ["tar -cf", "archive", "compress", "zip"],
     "answer": "tar -cf", "tech": "bash"},

    {"question": "Which shows PCI devices?",
     "options": ["lspci", "pci", "devices", "hardware"],
     "answer": "lspci", "tech": "bash"},

    {"question": "What represents exit status?",
     "options": ["$?", "$!", "$@", "$#"],
     "answer": "$?", "tech": "bash"},

    {"question": "How to check disk blocks?",
     "options": ["df -h", "blocks", "check", "disk"],
     "answer": "df -h", "tech": "bash"},

    {"question": "Which shows boot messages?",
     "options": ["dmesg", "boot", "messages", "log"],
     "answer": "dmesg", "tech": "bash"}
]

# Extend the quiz_data with more bash questions
quiz_data.extend(more_bash_questions)

java_generics_questions = [
    {"question": "What symbol represents type parameter?",
     "options": ["<T>", "(T)", "{T}", "[T]"],
     "answer": "<T>", "tech": "java generics"},

    {"question": "What is type erasure?",
     "options": ["Removing generic type at runtime", "Adding generic type", "Checking type", "Converting type"],
     "answer": "Removing generic type at runtime", "tech": "java generics"},

    {"question": "Which is valid generic type?",
     "options": ["List<String>", "List<string>", "List<5>", "List<void>"],
     "answer": "List<String>", "tech": "java generics"},

    {"question": "What does <?> represent?",
     "options": ["Wildcard type", "Unknown type", "Any type", "Object type"],
     "answer": "Wildcard type", "tech": "java generics"},

    {"question": "Valid bounded type parameter?",
     "options": ["<T extends Number>", "<T implements Number>", "<T inherit Number>", "<T from Number>"],
     "answer": "<T extends Number>", "tech": "java generics"},

    {"question": "What is upper bounded wildcard?",
     "options": ["<? extends Type>", "<? super Type>", "<? implements Type>", "<? Type>"],
     "answer": "<? extends Type>", "tech": "java generics"},

    {"question": "Cannot create array of:",
     "options": ["Generic type", "Object type", "Primitive type", "String type"],
     "answer": "Generic type", "tech": "java generics"},

    {"question": "What is lower bounded wildcard?",
     "options": ["<? super Type>", "<? extends Type>", "<? Type>", "<? implements Type>"],
     "answer": "<? super Type>", "tech": "java generics"},

    {"question": "Valid generic method declaration?",
     "options": ["<T> void method(T t)", "void <T> method(T t)", "void method<T>(T t)", "method <T> void(T t)"],
     "answer": "<T> void method(T t)", "tech": "java generics"},

    {"question": "What can't be generic?",
     "options": ["Exception class", "Interface", "Method", "Class"],
     "answer": "Exception class", "tech": "java generics"},

    {"question": "Multiple type parameters use:",
     "options": ["<T,U>", "<T;U>", "<T:U>", "<T&U>"],
     "answer": "<T,U>", "tech": "java generics"},

    {"question": "Raw type compatibility is:",
     "options": ["Backward compatible", "Forward compatible", "Not compatible", "Type safe"],
     "answer": "Backward compatible", "tech": "java generics"},

    {"question": "Valid generic interface?",
     "options": ["interface Box<T>", "interface Box(T)", "interface Box[T]", "interface Box{T}"],
     "answer": "interface Box<T>", "tech": "java generics"},

    {"question": "Generic type inheritance uses:",
     "options": ["extends", "implements", "super", "throws"],
     "answer": "extends", "tech": "java generics"},

    {"question": "What is PECS principle?",
     "options": ["Producer extends Consumer super", "Producer extends Compiler super", "Provider extends Consumer super", "Public extends Consumer super"],
     "answer": "Producer extends Consumer super", "tech": "java generics"},

    {"question": "Generic methods can be:",
     "options": ["Static", "Native", "Synchronized", "Final"],
     "answer": "Static", "tech": "java generics"},

    {"question": "Type parameter naming convention:",
     "options": ["Single uppercase letter", "Single lowercase letter", "Multiple letters", "Any name"],
     "answer": "Single uppercase letter", "tech": "java generics"},

    {"question": "Valid recursive type bound:",
     "options": ["<T extends Comparable<T>>", "<T super Comparable<T>>", "<T implements Comparable<T>>", "<T extends T>"],
     "answer": "<T extends Comparable<T>>", "tech": "java generics"},

    {"question": "Cannot use generic type with:",
     "options": ["instanceof", "new", "extends", "implements"],
     "answer": "instanceof", "tech": "java generics"},

    {"question": "Unbounded wildcard is:",
     "options": ["<?>", "<T>", "<Object>", "<*>"],
     "answer": "<?>", "tech": "java generics"},

    {"question": "Generic constructors use:",
     "options": ["Type before constructor name", "Type after constructor name", "No type parameter", "Type in parameters"],
     "answer": "Type before constructor name", "tech": "java generics"},

    {"question": "Valid generic array creation:",
     "options": ["(T[]) new Object[size]", "new T[size]", "new Generic<T>[size]", "Array.newInstance(T, size)"],
     "answer": "(T[]) new Object[size]", "tech": "java generics"},

    {"question": "Bridge methods are created for:",
     "options": ["Type erasure compatibility", "Performance optimization", "Memory management", "Exception handling"],
     "answer": "Type erasure compatibility", "tech": "java generics"},

    {"question": "Generic methods must:",
     "options": ["Declare type parameter", "Be static", "Return void", "Take parameters"],
     "answer": "Declare type parameter", "tech": "java generics"},

    {"question": "Wildcards can be used in:",
     "options": ["Variable declarations", "Return types", "Both A and B", "Neither"],
     "answer": "Both A and B", "tech": "java generics"},

    {"question": "Generic type information is:",
     "options": ["Compile-time only", "Runtime only", "Both", "Neither"],
     "answer": "Compile-time only", "tech": "java generics"},

    {"question": "Valid generic type parameter bound:",
     "options": ["<T extends A & B>", "<T implements A & B>", "<T extends A, B>", "<T implements A, B>"],
     "answer": "<T extends A & B>", "tech": "java generics"},

    {"question": "Raw types are:",
     "options": ["Not type-safe", "Type-safe", "Compile-time safe", "Runtime safe"],
     "answer": "Not type-safe", "tech": "java generics"},

    {"question": "Generic methods can:",
     "options": ["Infer type arguments", "Create generic arrays", "Use primitive types", "Override Object methods"],
     "answer": "Infer type arguments", "tech": "java generics"},

    {"question": "Type parameter scope is:",
     "options": ["Method/class declaration", "Entire package", "Entire program", "Runtime"],
     "answer": "Method/class declaration", "tech": "java generics"}
]

# Extend the quiz_data with Java Generics questions
quiz_data.extend(java_generics_questions)

advanced_python_questions = [
    {"question": "What is a metaclass in Python?",
     "options": ["Class that creates classes", "Class instance", "Module type", "Function decorator"],
     "answer": "Class that creates classes", "tech": "advanced python"},

    {"question": "What does @property decorator do?",
     "options": ["Creates getter method", "Creates class", "Defines static method", "Creates instance"],
     "answer": "Creates getter method", "tech": "advanced python"},

    {"question": "What is a context manager?",
     "options": ["Implements __enter__ and __exit__", "Creates context", "Manages memory", "Handles exceptions"],
     "answer": "Implements __enter__ and __exit__", "tech": "advanced python"},

    {"question": "What is method resolution order?",
     "options": ["Class inheritance lookup path", "Method calling order", "Class creation order", "Import order"],
     "answer": "Class inheritance lookup path", "tech": "advanced python"},

    {"question": "Purpose of __slots__?",
     "options": ["Restrict attributes", "Define methods", "Create properties", "Handle exceptions"],
     "answer": "Restrict attributes", "tech": "advanced python"},

    {"question": "What is a descriptor?",
     "options": ["Implements __get__/__set__", "Describes class", "Documents code", "Creates attributes"],
     "answer": "Implements __get__/__set__", "tech": "advanced python"},

    {"question": "What does yield from do?",
     "options": ["Delegates to sub-generator", "Creates generator", "Returns value", "Raises exception"],
     "answer": "Delegates to sub-generator", "tech": "advanced python"},

    {"question": "Purpose of __new__?",
     "options": ["Creates instance", "Initializes instance", "Deletes instance", "Copies instance"],
     "answer": "Creates instance", "tech": "advanced python"},

    {"question": "What is asyncio used for?",
     "options": ["Asynchronous I/O", "Synchronous operations", "Multi-threading", "Parallel processing"],
     "answer": "Asynchronous I/O", "tech": "advanced python"},

    {"question": "What are abstract base classes?",
     "options": ["Define interface", "Create instances", "Handle errors", "Store data"],
     "answer": "Define interface", "tech": "advanced python"},

    {"question": "Purpose of @classmethod?",
     "options": ["Takes class as first arg", "Creates instance", "Modifies instance", "Handles class data"],
     "answer": "Takes class as first arg", "tech": "advanced python"},

    {"question": "What is monkey patching?",
     "options": ["Runtime modification", "Code optimization", "Error handling", "Memory management"],
     "answer": "Runtime modification", "tech": "advanced python"},

    {"question": "What are coroutines?",
     "options": ["Async functions", "Regular functions", "Class methods", "Static methods"],
     "answer": "Async functions", "tech": "advanced python"},

    {"question": "Purpose of __call__?",
     "options": ["Makes instance callable", "Creates instance", "Deletes instance", "Copies instance"],
     "answer": "Makes instance callable", "tech": "advanced python"},

    {"question": "What is GIL?",
     "options": ["Global Interpreter Lock", "General Interface Layer", "Global Instance Lock", "Generic Input Lock"],
     "answer": "Global Interpreter Lock", "tech": "advanced python"},

    {"question": "What are dataclasses?",
     "options": ["Auto-implements methods", "Creates database", "Handles data", "Stores constants"],
     "answer": "Auto-implements methods", "tech": "advanced python"},

    {"question": "Purpose of __getattr__?",
     "options": ["Handles missing attributes", "Creates attributes", "Deletes attributes", "Lists attributes"],
     "answer": "Handles missing attributes", "tech": "advanced python"},

    {"question": "What is weak reference?",
     "options": ["Non-incrementing reference", "Strong reference", "Variable reference", "Constant reference"],
     "answer": "Non-incrementing reference", "tech": "advanced python"},

    {"question": "What does @staticmethod do?",
     "options": ["Creates independent method", "Creates instance method", "Modifies class", "Handles data"],
     "answer": "Creates independent method", "tech": "advanced python"},

    {"question": "Purpose of __await__?",
     "options": ["Makes object awaitable", "Creates async", "Handles waiting", "Manages time"],
     "answer": "Makes object awaitable", "tech": "advanced python"},

    {"question": "What is duck typing?",
     "options": ["Type based on behavior", "Static typing", "Dynamic typing", "Strong typing"],
     "answer": "Type based on behavior", "tech": "advanced python"},

    {"question": "What are magic methods?",
     "options": ["Double underscore methods", "Special functions", "Hidden methods", "Protected methods"],
     "answer": "Double underscore methods", "tech": "advanced python"},

    {"question": "Purpose of @functools.lru_cache?",
     "options": ["Memoizes function calls", "Creates cache", "Handles memory", "Stores data"],
     "answer": "Memoizes function calls", "tech": "advanced python"},

    {"question": "What is method chaining?",
     "options": ["Returns self from methods", "Links methods", "Combines functions", "Creates chain"],
     "answer": "Returns self from methods", "tech": "advanced python"},

    {"question": "Purpose of __iter__?",
     "options": ["Makes object iterable", "Creates iterator", "Handles iteration", "Counts items"],
     "answer": "Makes object iterable", "tech": "advanced python"},

    {"question": "What is a closure?",
     "options": ["Function with environment", "Closed function", "Private method", "Hidden variable"],
     "answer": "Function with environment", "tech": "advanced python"},

    {"question": "Purpose of __slots__ vs dict?",
     "options": ["Memory optimization", "Speed improvement", "Better organization", "Code clarity"],
     "answer": "Memory optimization", "tech": "advanced python"},

    {"question": "What is operator overloading?",
     "options": ["Customizing operators", "Creating operators", "Removing operators", "Combining operators"],
     "answer": "Customizing operators", "tech": "advanced python"},

    {"question": "Purpose of @contextmanager?",
     "options": ["Simplifies context managers", "Creates context", "Handles context", "Manages scope"],
     "answer": "Simplifies context managers", "tech": "advanced python"},

    {"question": "What is a generator expression?",
     "options": ["Memory efficient iterator", "List comprehension", "Set builder", "Dictionary creator"],
     "answer": "Memory efficient iterator", "tech": "advanced python"}
]

# Extend the quiz_data with Advanced Python questions
quiz_data.extend(advanced_python_questions)

python_ds_questions = [
    {"question": "Which method modifies list in place?",
     "options": ["sort()", "sorted()", "order()", "arrange()"],
     "answer": "sort()", "tech": "python builtin data structures"},

    {"question": "What's the time complexity of dict.get()?",
     "options": ["O(1)", "O(n)", "O(log n)", "O(n^2)"],
     "answer": "O(1)", "tech": "python builtin data structures"},

    {"question": "How to remove duplicates from list?",
     "options": ["set(list)", "list.unique()", "list.dedupe()", "list.distinct()"],
     "answer": "set(list)", "tech": "python builtin data structures"},

    {"question": "What's unique about frozenset?",
     "options": ["Immutable", "Ordered", "Indexed", "Sorted"],
     "answer": "Immutable", "tech": "python builtin data structures"},

    {"question": "Tuple vs List main difference?",
     "options": ["Immutability", "Size", "Order", "Type"],
     "answer": "Immutability", "tech": "python builtin data structures"},

    {"question": "Dict comprehension syntax uses:",
     "options": ["{k:v for...}", "[k:v for...]", "{k,v for...}", "(k:v for...)"],
     "answer": "{k:v for...}", "tech": "python builtin data structures"},

    {"question": "What's deque advantage over list?",
     "options": ["O(1) ends operations", "Sorting", "Searching", "Memory usage"],
     "answer": "O(1) ends operations", "tech": "python builtin data structures"},

    {"question": "Set operations time complexity?",
     "options": ["O(min(len(s),len(t)))", "O(n)", "O(1)", "O(n^2)"],
     "answer": "O(min(len(s),len(t)))", "tech": "python builtin data structures"},

    {"question": "OrderedDict vs dict in Python 3.7+?",
     "options": ["Regular dict is ordered", "OrderedDict is faster", "Different methods", "Size difference"],
     "answer": "Regular dict is ordered", "tech": "python builtin data structures"},

    {"question": "What's Counter object base class?",
     "options": ["dict", "list", "set", "tuple"],
     "answer": "dict", "tech": "python builtin data structures"},

    {"question": "defaultdict returns for missing key:",
     "options": ["Default factory value", "None", "Error", "Empty value"],
     "answer": "Default factory value", "tech": "python builtin data structures"},

    {"question": "ChainMap is used for:",
     "options": ["Multiple dict lookup", "List joining", "Set operations", "Tuple chaining"],
     "answer": "Multiple dict lookup", "tech": "python builtin data structures"},

    {"question": "namedtuple is subclass of:",
     "options": ["tuple", "list", "dict", "set"],
     "answer": "tuple", "tech": "python builtin data structures"},

    {"question": "Set vs frozenset difference:",
     "options": ["Mutability", "Order", "Size", "Methods"],
     "answer": "Mutability", "tech": "python builtin data structures"},

    {"question": "Dict update() method behavior:",
     "options": ["Modifies in place", "Returns new dict", "Creates copy", "Returns None"],
     "answer": "Modifies in place", "tech": "python builtin data structures"},

    {"question": "List slice assignment:",
     "options": ["Replaces section", "Appends only", "Prepends only", "Raises error"],
     "answer": "Replaces section", "tech": "python builtin data structures"},

    {"question": "Set add() vs update():",
     "options": ["Single vs multiple items", "Speed difference", "Memory usage", "Return value"],
     "answer": "Single vs multiple items", "tech": "python builtin data structures"},

    {"question": "Dict merge operator (|) requires:",
     "options": ["Python 3.9+", "Python 3.7+", "Python 3.8+", "Python 3.6+"],
     "answer": "Python 3.9+", "tech": "python builtin data structures"},

    {"question": "Queue vs deque difference:",
     "options": ["Double-ended operations", "Thread safety", "Size limit", "Order guarantee"],
     "answer": "Double-ended operations", "tech": "python builtin data structures"},

    {"question": "heapq implements what type?",
     "options": ["Min heap", "Max heap", "Binary tree", "Red-black tree"],
     "answer": "Min heap", "tech": "python builtin data structures"},

    {"question": "bytes vs bytearray difference:",
     "options": ["Mutability", "Size", "Encoding", "Methods"],
     "answer": "Mutability", "tech": "python builtin data structures"},

    {"question": "array.array vs list difference:",
     "options": ["Homogeneous type", "Size", "Methods", "Order"],
     "answer": "Homogeneous type", "tech": "python builtin data structures"},

    {"question": "dict.setdefault() returns:",
     "options": ["Existing or new value", "None", "Key only", "Default only"],
     "answer": "Existing or new value", "tech": "python builtin data structures"},

    {"question": "range() object is:",
     "options": ["Iterator", "List", "Tuple", "Set"],
     "answer": "Iterator", "tech": "python builtin data structures"},

    {"question": "memoryview is used for:",
     "options": ["Memory efficient slicing", "Memory allocation", "Cache management", "Garbage collection"],
     "answer": "Memory efficient slicing", "tech": "python builtin data structures"},

    {"question": "dict.pop() without default:",
     "options": ["Raises KeyError if missing", "Returns None", "Returns False", "Ignores error"],
     "answer": "Raises KeyError if missing", "tech": "python builtin data structures"},

    {"question": "list.sort() vs sorted():",
     "options": ["In-place vs new list", "Speed", "Memory usage", "Algorithm"],
     "answer": "In-place vs new list", "tech": "python builtin data structures"},

    {"question": "set intersection operator:",
     "options": ["&", "|", "^", "~"],
     "answer": "&", "tech": "python builtin data structures"},

    {"question": "tuple unpacking requires:",
     "options": ["Matching items", "Same types", "Ordered elements", "Unique items"],
     "answer": "Matching items", "tech": "python builtin data structures"},

    {"question": "collections.abc provides:",
     "options": ["Abstract base classes", "Concrete classes", "Function decorators", "Context managers"],
     "answer": "Abstract base classes", "tech": "python builtin data structures"}
]

# Extend the quiz_data with Python data structure questions
quiz_data.extend(python_ds_questions)
