# Вложенные функции
def message (name):
    def sent_message():
        return "Hello, " + name + "!"
    return sent_message()
print(message("Маша"))