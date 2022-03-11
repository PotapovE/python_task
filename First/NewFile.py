# 13. Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.
text_user, user_text = input(), input()
user_text_list = user_text.split()
counter = 0
for i in user_text_list:
    if i == text_user:
        counter += 1
print(counter)