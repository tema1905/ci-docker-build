import os
import sys
import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def load_asset(path):
    base = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    assets = os.path.join(base, "assets")
    return os.path.join(assets, path)


class App:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("700x500")
        self.window.configure(bg="#ffffff")
        self.window.title("SegmTel")

        # Словарь для хранения окон
        self.frames = {}

        # Создаем все окна
        for F in (MainWindow, AboutWindow, TeamWindow, SupportWindow, ClusteringWindow):
            frame = F(self.window, self)
            self.frames[F.__name__] = frame

        # Показываем главное окно
        self.show_frame("MainWindow")

    def show_frame(self, frame_name):
        # Скрываем все окна
        for frame in self.frames.values():
            frame.pack_forget()

        # Устанавливаем заголовок в зависимости от окна
        titles = {
            "MainWindow": "SegmTel - Главная",
            "AboutWindow": "SegmTel - О нас",
            "TeamWindow": "SegmTel - Команда",
            "SupportWindow": "SegmTel - Поддержка",
            "ClusteringWindow": "SegmTel - Кластеризация"
        }
        self.window.title(titles.get(frame_name, "SegmTel"))

        # Показываем нужное окно
        frame = self.frames[frame_name]
        frame.pack(fill="both", expand=True)

        # Устанавливаем геометрию
        if frame_name == "TeamWindow":
            self.window.geometry("600x340")
        elif frame_name == "SupportWindow":
            self.window.geometry("550x300")
        elif frame_name == "ClusteringWindow":
            self.window.geometry("1100x700")
        else:
            self.window.geometry("700x500")


class MainWindow(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.controller.window.title("SegmTel - Главная")  # Установка заголовка

        canvas = tk.Canvas(
            self,
            bg="#ffffff",
            width=700,
            height=500,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        canvas.place(x=0, y=0)

        # Здесь должно быть ваше основное изображение (frame_1/1.png)
        image_14 = tk.PhotoImage(file=load_asset("frame_1/1.png"))
        canvas.create_image(448, 195, image=image_14)

        # Здесь должно быть ваше лого или заголовок (frame_1/2.png)
        image_15 = tk.PhotoImage(file=load_asset("frame_1/2.png"))
        canvas.create_image(315, 36, image=image_15)

        # Загружаем изображения для кнопки "О нас"
        button_8_normal = tk.PhotoImage(file=load_asset("frame_1/3.png"))  # Обычное состояние
        button_8_hover = tk.PhotoImage(file=load_asset("frame_1/4_hover.png"))  # При наведении
        button_8_press = tk.PhotoImage(file=load_asset("frame_1/4_hover.png"))  # При нажатии

        button_8 = tk.Button(
            self,
            image=button_8_normal,
            relief="flat",
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame("TeamWindow")
        )
        button_8.place(x=490, y=26, width=84, height=23)

        # Привязываем события для кнопки "О нас"
        button_8.bind("<Enter>", lambda e: button_8.config(image=button_8_hover))
        button_8.bind("<Leave>", lambda e: button_8.config(image=button_8_normal))
        button_8.bind("<ButtonPress-1>", lambda e: button_8.config(image=button_8_press))
        button_8.bind("<ButtonRelease-1>", lambda e: button_8.config(image=button_8_hover))

        # Загружаем изображения для кнопки "Команда"
        button_9_normal = tk.PhotoImage(file=load_asset("frame_1/4.png"))  # Обычное состояние
        button_9_hover = tk.PhotoImage(file=load_asset("frame_1/3_hover.png"))  # При наведении
        button_9_press = tk.PhotoImage(file=load_asset("frame_1/3_hover.png"))  # При нажатии

        button_9 = tk.Button(
            self,
            image=button_9_normal,
            relief="flat",
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame("AboutWindow")
        )
        button_9.place(x=390, y=26, width=84, height=23)

        # Привязываем события для кнопки "Команда"
        button_9.bind("<Enter>", lambda e: button_9.config(image=button_9_hover))
        button_9.bind("<Leave>", lambda e: button_9.config(image=button_9_normal))
        button_9.bind("<ButtonPress-1>", lambda e: button_9.config(image=button_9_press))
        button_9.bind("<ButtonRelease-1>", lambda e: button_9.config(image=button_9_hover))

        # Загружаем изображения для кнопки "Поддержка"
        button_10_normal = tk.PhotoImage(file=load_asset("frame_1/5.png"))  # Обычное состояние
        button_10_hover = tk.PhotoImage(file=load_asset("frame_1/5_hover.png"))  # При наведении
        button_10_press = tk.PhotoImage(file=load_asset("frame_1/5_hover.png"))  # При нажатии

        button_10 = tk.Button(
            self,
            image=button_10_normal,
            relief="flat",
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame("SupportWindow")
        )
        button_10.place(x=600, y=28, width=80, height=18)

        # Привязываем события для кнопки "Поддержка"
        button_10.bind("<Enter>", lambda e: button_10.config(image=button_10_hover))
        button_10.bind("<Leave>", lambda e: button_10.config(image=button_10_normal))
        button_10.bind("<ButtonPress-1>", lambda e: button_10.config(image=button_10_press))
        button_10.bind("<ButtonRelease-1>", lambda e: button_10.config(image=button_10_hover))

        # Здесь должно быть ваше изображение (frame_1/6.png)
        image_16 = tk.PhotoImage(file=load_asset("frame_1/6.png"))
        canvas.create_image(317, 432, image=image_16)

        # Здесь должно быть ваше изображение (frame_1/7.png)
        image_17 = tk.PhotoImage(file=load_asset("frame_1/7.png"))
        canvas.create_image(472, 439, image=image_17)

        # Здесь должно быть ваше изображение (frame_1/8.png)
        image_18 = tk.PhotoImage(file=load_asset("frame_1/8.png"))
        canvas.create_image(629, 437, image=image_18)

        # Загружаем изображения для кнопки "Начать"
        button_11_normal = tk.PhotoImage(file=load_asset("frame_1/9.png"))  # Обычное состояние
        button_11_hover = tk.PhotoImage(file=load_asset("frame_1/9_hover.png"))  # При наведении
        button_11_press = tk.PhotoImage(file=load_asset("frame_1/9_hover.png"))  # При нажатии

        button_11 = tk.Button(
            self,
            image=button_11_normal,
            relief="flat",
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame("ClusteringWindow")
        )
        button_11.place(x=255, y=299, width=153, height=43)

        # Привязываем события для кнопки "Начать"
        button_11.bind("<Enter>", lambda e: button_11.config(image=button_11_hover))
        button_11.bind("<Leave>", lambda e: button_11.config(image=button_11_normal))
        button_11.bind("<ButtonPress-1>", lambda e: button_11.config(image=button_11_press))
        button_11.bind("<ButtonRelease-1>", lambda e: button_11.config(image=button_11_hover))

        # Здесь должно быть ваше изображение (frame_1/10.png)
        image_19 = tk.PhotoImage(file=load_asset("frame_1/10.png"))
        canvas.create_image(111, 250, image=image_19)

        # Сохраняем ссылки на изображения, чтобы они не удалялись сборщиком мусора
        self.images = [image_14, image_15, image_16, image_17, image_18, image_19]
        self.buttons_images = {
            'button_8': [button_8_normal, button_8_hover, button_8_press],
            'button_9': [button_9_normal, button_9_hover, button_9_press],
            'button_10': [button_10_normal, button_10_hover, button_10_press],
            'button_11': [button_11_normal, button_11_hover, button_11_press]
        }


class AboutWindow(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        canvas = tk.Canvas(
            self,
            bg="#ffffff",
            width=700,
            height=500,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        canvas.place(x=0, y=0)

        # Загружаем изображения для кнопки "Назад"
        button_2_image = tk.PhotoImage(file=load_asset("frame_2/1.png"))
        button_2_hover_image = tk.PhotoImage(file=load_asset("frame_2/1_hover.png"))

        button_2 = tk.Button(
            self,
            image=button_2_image,
            relief="flat",
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame("MainWindow")
        )
        button_2.place(x=308, y=433, width=152, height=43)

        # Функции для обработки событий наведения
        def on_enter(e):
            button_2.config(image=button_2_hover_image)

        def on_leave(e):
            button_2.config(image=button_2_image)

        # Привязываем события к кнопке
        button_2.bind("<Enter>", on_enter)
        button_2.bind("<Leave>", on_leave)

        # Остальные изображения
        image_4 = tk.PhotoImage(file=load_asset("frame_2/2.png"))
        canvas.create_image(483, 243, image=image_4)

        image_5 = tk.PhotoImage(file=load_asset("frame_2/3.png"))
        canvas.create_image(483, 37, image=image_5)

        image_6 = tk.PhotoImage(file=load_asset("frame_2/4.png"))
        canvas.create_image(142, 223, image=image_6)

        # Сохраняем ссылки на изображения
        self.images = [image_4, image_5, image_6]
        self.button_images = [button_2_image, button_2_hover_image]


class TeamWindow(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        canvas = tk.Canvas(
            self,
            bg="#ffffff",
            width=600,
            height=340,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        canvas.place(x=0, y=0)

        # Загружаем изображения для кнопки "Назад"
        button_1_image = tk.PhotoImage(file=load_asset("frame_2/1.png"))
        button_1_hover_image = tk.PhotoImage(file=load_asset("frame_2/1_hover.png"))

        def on_enter(e):
            button_1.config(image=button_1_hover_image)

        def on_leave(e):
            button_1.config(image=button_1_image)

        button_1 = tk.Button(
            self,
            image=button_1_image,
            relief="flat",
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame("MainWindow")
        )
        button_1.bind("<Enter>", on_enter)
        button_1.bind("<Leave>", on_leave)
        button_1.place(x=273, y=275, width=152, height=43)

        # Остальные изображения
        image_1 = tk.PhotoImage(file=load_asset("frame_3/2.png"))
        canvas.create_image(406, 31, image=image_1)

        image_2 = tk.PhotoImage(file=load_asset("frame_3/3.png"))
        canvas.create_image(413, 163, image=image_2)

        image_3 = tk.PhotoImage(file=load_asset("frame_3/4.png"))
        canvas.create_image(131, 168, image=image_3)

        # Сохраняем ссылки на изображения
        self.images = [image_1, image_2, image_3]
        self.button_images = [button_1_image, button_1_hover_image]


class SupportWindow(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        canvas = tk.Canvas(
            self,
            bg="#ffffff",
            width=550,
            height=300,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        canvas.place(x=0, y=0)

        image_1 = tk.PhotoImage(file=load_asset("frame_4/1.png"))
        canvas.create_image(387, 31, image=image_1)

        # Загружаем изображения для кнопки "Назад"
        button_1_image = tk.PhotoImage(file=load_asset("frame_2/1.png"))
        button_1_image_hover = tk.PhotoImage(file=load_asset("frame_2/1_hover.png"))

        button_1 = tk.Button(
            self,
            image=button_1_image,
            relief="flat",
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame("MainWindow")
        )

        def on_enter(e):
            button_1.config(image=button_1_image_hover)

        def on_leave(e):
            button_1.config(image=button_1_image)

        button_1.bind("<Enter>", on_enter)
        button_1.bind("<Leave>", on_leave)
        button_1.place(x=270, y=233, width=152, height=43)

        image_2 = tk.PhotoImage(file=load_asset("frame_4/3.png"))
        canvas.create_image(389, 142, image=image_2)

        image_3 = tk.PhotoImage(file=load_asset("frame_4/4.png"))
        canvas.create_image(135, 155, image=image_3)

        # Сохраняем ссылки на изображения
        self.images = [image_1, image_2, image_3]
        self.button_images = [button_1_image, button_1_image_hover]


class ClusteringWindow(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.data = None
        self.df = None
        self.optimal_clusters = 3
        self.kmeans = None
        self.scaler = None
        self.ax = None
        self.cluster_colors = None

        canvas = tk.Canvas(
            self,
            bg="#ffffff",
            width=1100,
            height=700,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        canvas.place(x=0, y=0)

        # Основные кнопки управления
        button_y_positions = [18, 100, 182, 582]  # Позиции по Y для кнопок
        button_height = 64

        # Кнопка "Загрузить данные"
        button_load_image = tk.PhotoImage(file=load_asset("frame_5/2.png"))
        button_load_hover = tk.PhotoImage(file=load_asset("frame_5/2_hover.png"))

        button_load = tk.Button(
            self,
            image=button_load_image,
            relief="flat",
            borderwidth=0,
            highlightthickness=0,
            command=self.load_data
        )
        button_load.place(x=24, y=button_y_positions[0], width=197, height=button_height)

        # Кнопка "Метод локтя"
        button_elbow_image = tk.PhotoImage(file=load_asset("frame_5/1.png"))
        button_elbow_hover = tk.PhotoImage(file=load_asset("frame_5/1_hover.png"))

        button_elbow = tk.Button(
            self,
            image=button_elbow_image,
            relief="flat",
            borderwidth=0,
            highlightthickness=0,
            command=self.elbow_method
        )
        button_elbow.place(x=24, y=button_y_positions[1], width=197, height=button_height)

        # Кнопка "Выполнить кластеризацию"
        button_cluster_image = tk.PhotoImage(file=load_asset("frame_5/3.png"))
        button_cluster_hover = tk.PhotoImage(file=load_asset("frame_5/3_hover.png"))

        button_cluster = tk.Button(
            self,
            image=button_cluster_image,
            relief="flat",
            borderwidth=0,
            highlightthickness=0,
            command=self.perform_clustering
        )
        button_cluster.place(x=24, y=button_y_positions[2], width=197, height=button_height)

        # Кнопка "Предсказать кластер"
        button_predict_image = tk.PhotoImage(file=load_asset("frame_5/8.png"))
        button_predict_hover = tk.PhotoImage(file=load_asset("frame_5/8_hover.png"))

        button_predict = tk.Button(
            self,
            image=button_predict_image,
            relief="flat",
            borderwidth=0,
            highlightthickness=0,
            command=self.predict_cluster
        )
        button_predict.place(x=24, y=500, width=197, height=button_height)

        # Кнопка "Вернуться"
        button_back_image = tk.PhotoImage(file=load_asset("frame_5/4.png"))
        button_back_hover_image = tk.PhotoImage(file=load_asset("frame_5/4_hover.png"))

        button_back = tk.Button(
            self,
            image=button_back_image,
            relief="flat",
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame("MainWindow")
        )
        button_back.place(x=24, y=button_y_positions[3], width=197, height=button_height)

        # Функции для обработки событий наведения
        def on_enter(e):
            button_back.config(image=button_back_hover_image)

        def on_leave(e):
            button_back.config(image=button_back_image)

        # Привязываем события к кнопке
        button_back.bind("<Enter>", on_enter)
        button_back.bind("<Leave>", on_leave)


        # Привязка событий для всех кнопок
        buttons = [
            (button_load, button_load_image, button_load_hover),
            (button_elbow, button_elbow_image, button_elbow_hover),
            (button_cluster, button_cluster_image, button_cluster_hover),
            (button_predict, button_predict_image, button_predict_hover)
        ]

        for btn, img, hover_img in buttons:
            btn.bind("<Enter>", lambda e, b=btn, h=hover_img: b.config(image=h))
            btn.bind("<Leave>", lambda e, b=btn, i=img: b.config(image=i))

        # Создаем фрейм для графика
        self.plot_frame = tk.Frame(self, bg="white")
        self.plot_frame.place(x=250, y=20, width=800, height=650)

        # Combobox для выбора признаков
        self.feature_frame = tk.LabelFrame(
            self,
            text="Выбор признаков",
            bg="#ffffff",
            font=('Arial', 10)
        )
        self.feature_frame.place(x=24, y=300, width=255, height=80)

        tk.Label(
            self.feature_frame,
            text="Признак 1:",
            bg="#ffffff",
            font=('Arial', 9)
        ).grid(row=0, column=0, sticky="w", padx=5, pady=2)

        self.feature_combobox1 = ttk.Combobox(
            self.feature_frame,
            state="readonly",
            width=20,
            font=('Arial', 9)
        )
        self.feature_combobox1.grid(row=0, column=1, padx=5, pady=2, sticky="ew")

        tk.Label(
            self.feature_frame,
            text="Признак 2:",
            bg="#ffffff",
            font=('Arial', 9)
        ).grid(row=1, column=0, sticky="w", padx=5, pady=2)

        self.feature_combobox2 = ttk.Combobox(
            self.feature_frame,
            state="readonly",
            width=20,
            font=('Arial', 9)
        )
        self.feature_combobox2.grid(row=1, column=1, padx=5, pady=2, sticky="ew")

        # Поля для ввода значений для предсказания
        self.pred_frame = tk.LabelFrame(
            self,
            text="Предсказание кластера",
            bg="#ffffff",
            font=('Arial', 10)
        )
        self.pred_frame.place(x=24, y=400, width=255, height=80)

        tk.Label(
            self.pred_frame,
            text="Значение 1:",
            bg="#ffffff",
            font=('Arial', 9)
        ).grid(row=0, column=0, sticky="w", padx=5, pady=2)

        self.pred_x_entry = tk.Entry(
            self.pred_frame,
            bd=1,
            bg="#ffffff",
            fg="#000000",
            insertbackground="#000000",
            highlightthickness=1,
            font=('Arial', 9),
            width=15
        )
        self.pred_x_entry.grid(row=0, column=1, padx=5, pady=2, sticky="ew")

        tk.Label(
            self.pred_frame,
            text="Значение 2:",
            bg="#ffffff",
            font=('Arial', 9)
        ).grid(row=1, column=0, sticky="w", padx=5, pady=2)

        self.pred_y_entry = tk.Entry(
            self.pred_frame,
            bd=1,
            bg="#ffffff",
            fg="#000000",
            insertbackground="#000000",
            highlightthickness=1,
            font=('Arial', 9),
            width=15
        )
        self.pred_y_entry.grid(row=1, column=1, padx=5, pady=2, sticky="ew")

        # Label для отображения оптимального числа кластеров
        self.optimal_label = tk.Label(
            self,
            text="Оптимальное число кластеров: -",
            bg="#ffffff",
            fg="#333333",
            font=('Arial', 10)
        )
        self.optimal_label.place(x=24, y=264)

        # Сохраняем ссылки на изображения
        self.button_images = {
            'button_back': [button_back_image, button_back_hover_image],
            'button_load': [button_load_image, button_load_hover],
            'button_elbow': [button_elbow_image, button_elbow_hover],
            'button_cluster': [button_cluster_image, button_cluster_hover],
            'button_predict': [button_predict_image, button_predict_hover]
        }

    def load_data(self):
        filepath = filedialog.askopenfilename(
            filetypes=[("Excel files", "*.xlsx"), ("Excel files", "*.xls"), ("CSV files", "*.csv")]
        )
        if filepath:
            try:
                if filepath.endswith(".csv"):
                    self.df = pd.read_csv(filepath)
                elif filepath.endswith(".xlsx"):
                    self.df = pd.read_excel(filepath)
                elif filepath.endswith(".xls"):
                    self.df = pd.read_excel(filepath)

                numeric_cols = self.df.select_dtypes(include=['number']).columns.tolist()
                self.feature_combobox1['values'] = numeric_cols
                self.feature_combobox2['values'] = numeric_cols

                if len(numeric_cols) >= 2:
                    self.feature_combobox1.current(0)
                    self.feature_combobox2.current(1)

                for widget in self.plot_frame.winfo_children():
                    widget.destroy()

                tk.Label(
                    self.plot_frame,
                    text=f"Загружено {len(self.df)} записей",
                    bg="white",
                    fg="green",
                    font=('Arial', 12)
                ).pack(expand=True)

            except Exception as e:
                tk.Label(
                    self.plot_frame,
                    text=f"Ошибка загрузки: {str(e)}",
                    bg="white",
                    fg="red",
                    font=('Arial', 12)
                ).pack(expand=True)

    def elbow_method(self):
        if self.df is None or not self.feature_combobox1.get() or not self.feature_combobox2.get():
            tk.Label(
                self.plot_frame,
                text="Ошибка: данные не загружены или признаки не выбраны",
                bg="white",
                fg="red",
                font=('Arial', 12)
            ).pack(expand=True)
            return

        feature1 = self.feature_combobox1.get()
        feature2 = self.feature_combobox2.get()
        X = self.df[[feature1, feature2]].values

        # Проверка на достаточное количество данных
        if len(X) < 2:
            tk.Label(
                self.plot_frame,
                text="Ошибка: недостаточно данных для анализа",
                bg="white",
                fg="red",
                font=('Arial', 12)
            ).pack(expand=True)
            return

        try:
            # Нормализация данных
            scaler = StandardScaler()
            X_scaled = scaler.fit_transform(X)

            max_clusters = min(10, len(X) - 1)  # Не больше чем n_samples-1
            if max_clusters < 2:
                tk.Label(
                    self.plot_frame,
                    text="Ошибка: слишком мало данных для выбранного числа кластеров",
                    bg="white",
                    fg="red",
                    font=('Arial', 12)
                ).pack(expand=True)
                return

            inertia = []

            for k in range(1, max_clusters + 1):
                kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
                kmeans.fit(X_scaled)
                inertia.append(kmeans.inertia_)

            # Находим оптимальное число кластеров по методу локтя
            if len(inertia) >= 3:  # Нужно как минимум 3 точки для вычисления разниц
                diff = np.diff(inertia)
                diff_r = diff[1:] / diff[:-1]
                optimal_k = np.argmin(diff_r) + 2  # +2 потому что начинаем с k=1
                self.optimal_clusters = optimal_k
            else:
                self.optimal_clusters = 2  # Значение по умолчанию

            self.optimal_label.config(text=f"Оптимальное число кластеров: {self.optimal_clusters}")

            # Очищаем предыдущий график
            for widget in self.plot_frame.winfo_children():
                widget.destroy()

            # Создаем график метода локтя
            fig = plt.Figure(figsize=(8, 5), dpi=100)
            ax = fig.add_subplot(111)

            ax.plot(range(1, max_clusters + 1), inertia, marker='o')
            ax.axvline(x=self.optimal_clusters, color='r', linestyle='--')
            ax.set_title('Метод локтя')
            ax.set_xlabel('Число кластеров (к)')
            ax.set_ylabel('Сумма внутрикластерных расстояний')
            ax.grid(True)

            # Встраиваем график в интерфейс
            canvas = FigureCanvasTkAgg(fig, master=self.plot_frame)
            canvas.draw()
            canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        except Exception as e:
            tk.Label(
                self.plot_frame,
                text=f"Ошибка: {str(e)}",
                bg="white",
                fg="red",
                font=('Arial', 12)
            ).pack(expand=True)

    def perform_clustering(self):
        if self.df is None or not self.feature_combobox1.get() or not self.feature_combobox2.get():
            tk.Label(
                self.plot_frame,
                text="Ошибка: данные не загружены или признаки не выбраны",
                bg="white",
                fg="red",
                font=('Arial', 12)
            ).pack(expand=True)
            return

        if not hasattr(self, 'optimal_clusters'):
            tk.Label(
                self.plot_frame,
                text="Сначала выполните метод локтя",
                bg="white",
                fg="red",
                font=('Arial', 12)
            ).pack(expand=True)
            return

        feature1 = self.feature_combobox1.get()
        feature2 = self.feature_combobox2.get()
        X = self.df[[feature1, feature2]].values

        # Нормализация данных
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)

        try:
            # Выполняем кластеризацию с оптимальным числом кластеров
            kmeans = KMeans(n_clusters=self.optimal_clusters, random_state=42)
            labels = kmeans.fit_predict(X_scaled)

            # Очищаем предыдущий график
            for widget in self.plot_frame.winfo_children():
                widget.destroy()

            # Создаем график кластеров
            fig, ax = plt.subplots(figsize=(8, 6))

            # Визуализация кластеров
            scatter = ax.scatter(X[:, 0], X[:, 1], c=labels, cmap='tab20', s=50, alpha=0.8)

            # добавляем под сохранение центроидов
            self.cluster_colors = [  # список реальных RGBA-цветов кластеров
                scatter.cmap(scatter.norm(i)) for i in range(self.optimal_clusters)
            ]

            # Центроиды
            centroids = scaler.inverse_transform(kmeans.cluster_centers_)
            ax.scatter(centroids[:, 0], centroids[:, 1], marker='X', s=200, c='red', label='Центроиды')

            # Легенда
            legend_labels = [f'Кластер {i + 1}' for i in range(self.optimal_clusters)]
            ax.legend(
                handles=scatter.legend_elements()[0],
                labels=legend_labels,
                title="Кластеры",
                loc="upper right"
            )

            ax.set_title(
                f"K-Means кластеризация\nЧисло кластеров: {self.optimal_clusters}",
                pad=20
            )
            ax.set_xlabel(feature1)
            ax.set_ylabel(feature2)
            ax.grid(True, linestyle='--', alpha=0.6)

            # Встраиваем график в интерфейс
            canvas = FigureCanvasTkAgg(fig, master=self.plot_frame)
            canvas.draw()
            canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

            self.kmeans = kmeans   # пригодится для predict_cluster
            self.scaler = scaler
            self.ax = ax      # текущая ось с уже нарисованными точками

        except Exception as e:
            tk.Label(
                self.plot_frame,
                text=f"Ошибка кластеризации: {str(e)}",
                bg="white",
                fg="red",
                font=('Arial', 12)
            ).pack(expand=True)

        # Добавляем Label для отображения результата предсказания
        self.prediction_result = tk.Label(
            self.plot_frame,
            text="",
            bg="white",
            fg="green",
            font=('Arial', 12)
        )
        self.prediction_result.pack(side=tk.BOTTOM, fill=tk.X)

    def predict_cluster(self):
        """Берёт значения из полей ввода, предсказывает кластер и рисует звезду."""
        if not hasattr(self, 'kmeans'):
            self.prediction_result.config(text="Сначала выполните кластеризацию", fg="red")
            return
        try:
            x_val = float(self.pred_x_entry.get().replace(',', '.'))
            y_val = float(self.pred_y_entry.get().replace(',', '.'))
        except ValueError:
            self.prediction_result.config(text="Введите числовые значения X и Y", fg="red")
            return

        X_new_scaled = self.scaler.transform([[x_val, y_val]])
        cluster = int(self.kmeans.predict(X_new_scaled)[0])
        self.plot_new_point((x_val, y_val), cluster)
        self.prediction_result.config(
            text=f"Точка ({x_val:.2f}, {y_val:.2f}) принадлежит кластеру {cluster + 1}",
            fg="green"
        )


    def plot_new_point(self, point_xy, cluster_label):
        """Рисует новую точку ★ поверх существующей диаграммы."""
        if not hasattr(self, 'ax'):
            return
        color = self.cluster_colors[cluster_label]  # цвет кластера
        self.ax.scatter(
            point_xy[0], point_xy[1],
            marker='*', s=250, zorder=5,
            edgecolor='k', linewidths=1.5,
            c=[color]  # ✔ корректный RGBA
        )
        self.ax.figure.canvas.draw_idle()


if __name__ == "__main__":
    app = App()
    app.window.mainloop()