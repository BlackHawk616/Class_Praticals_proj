# Python Fundamentals 
## Date :- 2-8-23

## Non Graphic (Escape) Characters
- They are the special characters which cannot be typed directly from keyword like backspace, tab, enter etc. When The Characters are Typed They Perform Some Action These are represented by Escape Character. Escape character are always begin from backspace ( \ ) Character

## List Of Escape Characters 
| Escape Sequence | What It Does |
|--|--|--|--|
| \\\ | Back Slash |
|\\'|Single Quote|
|\\" | Double Quotes
|\\b| back Space| 
| \n | New Line |  

## String Type in Python
- Python Allows You To Have Two String Types
## Single Line String 
- The String We Create Using single )r Double Quotes Are normally Single-Line string i.e. They Must Terminate In One Line
For Example :- If You Type This 
```py
Name = "KV # And Press Enter
```
- Python Will Show You An Error "EOL While Scanning String Literal"
- The Reason Is quite Clear, Python By Default Creates Single Line String With both Single Quotes And It Must Terminate In The Same Line By Quotes
## Multiline String 
- Some Times We Need To Store Some Test Across Multiline For That Python After multi line string
- To Store Multi Line String Python Provides 2 Ways
**A) By Adding AA Back Slash At The End Of Normal Single / Double Quoted String For Example**
```py
>>> Name = "1/6 Mall Road \ 
kanpur"
>>> Name 
    '1/6 Mall Road Kanpur'
>>>
```
**B) By Typing Text In Triple Quotation marks**
```py
>>> address = """1/7 Preet Vihar
New Delhi
India"""
>>> print (Address)
# OutPut 
1/7 preet Vihar
New Delhi
India
```
## Size Of String 
- Python Determines The Size of string as the count of characters in the string. For Example Size of String "xyz" is 3 and of "Welcome" is 7. But If Your string literal has an escape sequence contained in it make sure to count The Escape Sequence Character For Eg.
- 
|String| Size  |
|--|--|
| "\\\\" |1|
| "abc"| 3
| "\ab"| 2|
| "Meera \\'s Toy"|11
|"Vicky's"| 7
