import tkinter as tk
import tkinter.ttk as ttk

from sqlite3 import *


class Table(tk.Frame):
    def __init__(self, parent=None, headings=tuple(), rows=tuple()):
        super().__init__(parent)

        table = ttk.Treeview(self, show="headings", selectmode="browse")
        table["columns"] = headings
        table["displaycolumns"] = headings

        for head in headings:
            table.heading(head, text=head, anchor=tk.CENTER)
            table.column(head, anchor=tk.CENTER)

        for row in rows:
            table.insert('', tk.END, values=tuple(row))

        scrolltable = tk.Scrollbar(self, command=table.yview)
        table.configure(yscrollcommand=scrolltable.set)
        scrolltable.pack(side=tk.RIGHT, fill=tk.Y)
        table.pack(expand=tk.YES, fill=tk.BOTH)


class records:
    def __init__(self):
        root = tk.Tk()
        root.title('Рекорды')
        names = (
            'Сортировка "пузырьком".', 'Сортировка "Вставками"', '"Быстрая" сортировка.',
            '"Быстрая" сортировка с асинхронностью.',
            'Сортировка подсчётом.')
        conn = connect('project_trpo')
        cursor = conn.cursor()
        cursor.execute("SELECT USERNAME, result, topic FROM Records ORDER BY topic, result DESC")
        table = Table(root, headings=('Имя пользователя', 'Результат', 'Тема'),
                      rows=tuple(((*polya, names[topic]) for *polya, topic in cursor.fetchall())))
        table.pack(expand=tk.YES, fill=tk.BOTH)
        root.mainloop()


if __name__ == "__main__":
    records()
