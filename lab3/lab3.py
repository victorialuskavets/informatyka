import re

#1

def remove_special_characters(text):
    return re.sub(r'\W+', ' ', text)


def match_word_with_character(text, char):
    return re.findall(r'\b\w*' + re.escape(char) + r'\w*\b', text)

def match_word_length(text, length):
    return re.findall(r'\b\w{' + str(length) + r'}\b', text)

def match_word_start_end(text):
    return re.findall(r'\b[a-b]\w*s\b', text)



#2

def collect_and_sum_amounts(text):
    amounts = re.findall(r'\$(\d+\.\d+|\d+)', text)
    amounts = [float(amount) for amount in amounts]  
    return sum(amounts)



#3

def clean_python_code(code):
    cleaned_code = re.sub(r'#.*', '', code)
    cleaned_code = re.sub(r'\n\s*\n', '\n', cleaned_code)
    return cleaned_code.strip()



#4

def convert_date_format(text):
    return re.sub(r'(\d{4})-(\d{2})-(\d{2})', r'\3-\2-\1', text)



text1 = "Привіт! Як ти? #!la-la @23"
print("1.1: Видалення спеціальних символів")
print(remove_special_characters(text1))

text2 = "Синтаксис завжди є багато в Python."
print("1.2: Пошук слова, яке містить символ 'y'")
print(match_word_with_character(text2, 'y')) 

text3 = "Ось деякі слова як слід, лід, весна, мех-мат ніч."
print("1.3: Пошук слова довжиною 3")
print(match_word_length(text3, 3))

text4 = "cats books apples rabbit bikes"
print("1.4: слова, яке починається на a or b та закінчуються на s")
print(match_word_start_end(text4))

text5 = "Перша сума $123.45, друга сума $400"
print("2: Collect and sum amounts: ")
print(collect_and_sum_amounts(text5))

text6 = "Подія відбудеться 2024-02-11."
print("4: Конвертація дати: ")
print(convert_date_format(text6))

#3
python_code = """
print("Злвьіл")  

x = 5  
y = x + 2
"""

result = clean_python_code(python_code)

print("Очищений код:")
print(result)