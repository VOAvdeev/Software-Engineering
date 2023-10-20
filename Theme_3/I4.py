# Получаем предложение от пользователя
pred = input("Введите предложение на английском: ")
print("Длина предложения:", len(pred))
lowercase_pred = pred.lower()
print("Предложение в нижнем регистре:", lowercase_pred)
vowels = "aeiou"
vowel_count = sum(1 for char in lowercase_pred if char in vowels)
print("Количество гласных:", vowel_count)
replaced_pred = lowercase_pred.replace("ugly", "beauty")
print("Предложение с заменой 'ugly' на 'beauty':", replaced_pred)
starts_with_the = lowercase_pred.startswith("the")
ends_with_end = lowercase_pred.endswith("end")
if starts_with_the:
    print("Предложение начинается с 'The'")
else:
    print("Предложение не начинается с 'The'")
if ends_with_end:
    print("Предложение заканчивается на 'end'")
else:
    print("Предложение не заканчивается на 'end'")