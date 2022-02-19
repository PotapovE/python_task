# Вложенные функции
def message (name):
    def sent_message():
        return "Hello, " + name + "!"
    return sent_message()
print(message("Маша"))

# Замыкания
def key (x):
    def open_key (y):
        return x + y
    return open_key
save_key = key(5)
print(save_key)
print(save_key(6))
print(save_key(11))