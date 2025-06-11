# Клас, що представляє окремий коментар
class Comment:
    def __init__(self, text, author):
        self.text = text  # текст коментаря
        self.author = author  # автор коментаря
        self.replies = []  # список відповідей
        self.is_deleted = False  # прапорець, чи був коментар видалений

    # Метод для додавання відповіді
    def add_reply(self, reply):
        self.replies.append(reply)

    # Метод для видалення відповіді (змінює текст та ставить прапорець is_deleted)
    def remove_reply(self):
        self.text = "Цей коментар було видалено."
        self.is_deleted = True

    # Метод для виводу коментаря і всіх його відповідей з відступами
    def display(self, level=0):
        indent = "    " * level
        if self.is_deleted:
            print(f"{indent}{self.text}")  # вивід без автора
        else:
            print(f"{indent}{self.author}: {self.text}")  # вивід з автором
        for reply in self.replies:
            reply.display(level + 1)


# Приклад використання:
root_comment = Comment("Яка чудова книга!", "Бодя")
reply1 = Comment("Книга повне розчарування :(", "Андрій")
reply2 = Comment("Що в ній чудового?", "Марина")

root_comment.add_reply(reply1)
root_comment.add_reply(reply2)

reply1_1 = Comment("Не книжка, а перевели купу паперу ні нащо...", "Сергій")
reply1.add_reply(reply1_1)

reply1.remove_reply()

root_comment.display()
