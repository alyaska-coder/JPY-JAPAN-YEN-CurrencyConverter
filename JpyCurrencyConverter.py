import os
import requests
import tkinter as tk
import sys


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
response = requests.get("https://www.cbr-xml-daily.ru/daily_json.js", headers=headers)
data = response.json()


jpy_data = data["Valute"]["JPY"]
jpy_converter_to_1 = jpy_data["Value"] / 100

def resource_path(filename):
    if getattr(sys, "frozen", False):
        base = sys._MEIPASS
    else:
        base = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base, filename)


def start_convert():
    user_input = yen_entry.get()

    try:
        amount = float(user_input)
        rub_result = amount * jpy_converter_to_1
        conclusion.config(text=f"Результат: {rub_result:.2f} руб.")
        conclusion.config(fg="white")

    except ValueError:
        conclusion.config(text="Бро, введи число!", fg="red")


def center_window(win, width, height):
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    win.geometry(f"{width}x{height}+{x}+{y}")

window = tk.Tk()
window.config(bg="#1e1e1e")
window.title("JPY to RUB Converter")
window.resizable(False, False)
window.iconbitmap(resource_path("yui.ico"))

center_window(window, 400, 265)

yen_entry = tk.Entry(window, font=("Arial", 14, "bold"), fg="#333333", justify="center")
yen_entry.pack(pady=20)

convert_btn = tk.Button(
    window,
    text="Конвертировать",
    font=("Arial", 12, "bold"),
    bg="#2e2e2e",
    fg="white",
    bd=0,
    relief="flat",
    padx=10,
    pady=5,
    command=start_convert
)
convert_btn.pack(pady=10)

conclusion = tk.Label(window, text="", font=("Consolas", 15), fg="white", bg="#1e1e1e")
conclusion.pack(pady=15)

exchange_rate = tk.Label(
    window,
    text=f"1 YEN = {jpy_converter_to_1:.2f} RUB",
    font=("Arial", 18, "bold"),
    bg="#2e2e2e",
    fg="white"
)
exchange_rate.place(x=10, y=200)

image_path = resource_path("100x100 ayanami png.png")

my_icon = tk.PhotoImage(file=image_path)
image_label = tk.Label(window, image=my_icon, bg="#1e1e1e")
image_label.place(x=300, y=165)

window.mainloop()