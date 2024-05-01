import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image

class Watch:
    def __init__(self, brandname, material, creationdate):
        self.brandname = brandname  # Назва бренду годинника
        self.material = material    # Матеріал годинника
        self.creationdate = creationdate  # Дата створення годинника

class WristWatch(Watch):
    def __init__(self, name="Rolex", material="Сталь", creationdate=2019, weight=150):
        super().__init__(name, material, creationdate)
        self.weight = weight  # Вага годинника

    def run_application(self):
        root = tk.Tk()
        root.title("Інформація")  # Заголовок вікна
        root.geometry("600x400")   # Розмір вікна
        root.configure(bg='black') # Чорний колір фону
        self.current_image_index = 0

        text_frame = tk.Frame(root, bg='black')  # Фрейм для введення тексту з чорним фоном
        text_frame.pack(side=tk.LEFT, padx=10, pady=10)

        tk.Label(text_frame, text="Назва бренду:", bg='black', fg='white').pack()  # Мітка для назви бренду
        self.name_entry = tk.Entry(text_frame)   # Поле введення для назви бренду
        self.name_entry.pack()
        self.name_entry.insert(0, self.brandname)

        tk.Label(text_frame, text="Матеріал:", bg='black', fg='white').pack()   # Мітка для матеріалу
        self.material_entry = tk.Entry(text_frame)  # Поле введення для матеріалу
        self.material_entry.pack()
        self.material_entry.insert(0, self.material)

        tk.Label(text_frame, text="Дата створення:", bg='black', fg='white').pack()  # Мітка для дати створення
        self.creationdate_entry = tk.Entry(text_frame)  # Поле введення для дати створення
        self.creationdate_entry.pack()
        self.creationdate_entry.insert(0, self.creationdate)

        tk.Label(text_frame, text="Вага:", bg='black', fg='white').pack()  # Мітка для ваги
        self.weight_entry = tk.Entry(text_frame)  # Поле введення для ваги
        self.weight_entry.pack()
        self.weight_entry.insert(0, self.weight)

        tk.Button(text_frame, text="Створити наручний годинник",
                  command=self.create_wristwatch, bg='white').pack()  # Кнопка для створення годинника

        self.info_label = tk.Label(text_frame, text="", bg='black', fg='white')  # Мітка для відображення інформації
        self.info_label.pack()

        image_frame = tk.Frame(root, bg='black')  # Фрейм для зображення з чорним фоном
        image_frame.pack(side=tk.RIGHT, padx=10, pady=10)

        self.load_images(image_frame)  # Завантаження зображень

        tk.Button(image_frame, text="Попереднє зображення",
                  command=self.show_previous_image, bg='white').pack(side=tk.BOTTOM)  # Кнопка для попереднього зображення
        tk.Button(image_frame, text="Наступне зображення",
                  command=self.show_next_image, bg='white').pack(side=tk.BOTTOM)  # Кнопка для наступного зображення

        root.mainloop()

    def create_wristwatch(self):
        name = self.name_entry.get()         # Отримання значення назви бренду
        material = self.material_entry.get() # Отримання значення матеріалу
        creationdate = self.creationdate_entry.get() # Отримання значення дати створення
        weight = self.weight_entry.get()     # Отримання значення ваги

        if name and material and creationdate and weight:
            try:
                creationdate = int(creationdate)
                weight = float(weight)
                self.watch = WristWatch(name, material, creationdate, weight)
                info_text = f"Назва бренду: {self.watch.brandname}\n"    # Формування рядка інформації
                info_text += f"Матеріал: {self.watch.material}\n"
                info_text += f"Дата створення: {self.watch.creationdate}\n"
                info_text += f"Вага: {self.watch.weight}"
                self.info_label.config(text=info_text)  # Відображення інформації
            except ValueError:
                messagebox.showerror("Error", "Некоректний формат введених даних для дати створення або ваги.")
        else:
            messagebox.showerror("Error", "Будь ласка, введіть всі дані.")

    def load_images(self, container):
        try:
            self.images = [
                ImageTk.PhotoImage(Image.open("picture1.jpg").resize((500, 500))),  # Зображення 1
                ImageTk.PhotoImage(Image.open("picture2.png").resize((500, 500))), # Зображення 2
                ImageTk.PhotoImage(Image.open("picture3.jpg").resize((500, 500)))  # Зображення 3
            ]
        except FileNotFoundError:
            messagebox.showerror("Error", "Один або кілька файлів зображень не знайдено.")
            exit()

        if self.images:
            self.image_label = tk.Label(container, image=self.images[self.current_image_index], bg='black')
            self.image_label.pack(pady=20)  # Горизонтальна відстань 150 від верхньої границі віджету

    def show_next_image(self):
        if self.images:
            self.current_image_index = (self.current_image_index + 1) % len(self.images)
            self.image_label.config(image=self.images[self.current_image_index])

    def show_previous_image(self):
        if self.images:
            self.current_image_index = (self.current_image_index - 1) % len(self.images)
            self.image_label.config(image=self.images[self.current_image_index])

if __name__ == "__main__":
    watch = WristWatch()
    watch.run_application()
