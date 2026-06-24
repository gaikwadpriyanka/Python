p = '           j   A     99999  v   7777    A    '
s = p.replace(" ","")
print(s)


###################################################
# check casefold and lowercase()

'''Feature	lower()	casefold()
Purpose	Converts uppercase letters to lowercase.
Use Case Basic lowercase conversion for general text processing.
Doesn't handle special or language-specific cases.
Example	"HELLO".lower() => "hello"	"HELLO".casefold() => "hello"

Converts uppercase letters to lowercase, including special characters and locale-specific cases.
Handles special cases like German "ß" (sharp S) correctly (e.g., "ß".casefold() => "ss").
Best for case-insensitive comparisons, especially for multilingual text.
Handling of Special Characters

Example with Special Characters	"ß".lower() => "ß"	"ß".casefold() => "ss"
'''