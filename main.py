import js
import random
from pyodide.ffi import create_proxy

# Список німецьких цитат
quotes = [
    "„Der Weg ist das Ziel.“ – Konfuzius",
    "„Leben ist kein Ponyhof.“ – Volksmund",
    "„Alles hat ein Ende, nur die Wurst hat zwei.“ – Volkslied",
    "„Wer rastet, der rostet.“ – Sprichwort",
    "„Phantasie ist wichtiger als Wissen.“ – Albert Einstein",
    "„Probleme sind verkleidete Möglichkeiten.“ – Henry Ford",
    "„Wer wagt, gewinnt.“ – Sprichwort",
    "„Geduld ist eine Tugend.“ – Volksmund"
]

def generate_quote(event):
    # Вибираємо випадкову цитату
    random_quote = random.choice(quotes)
    # Виводимо її в HTML-елемент
    display = js.document.getElementById("quote-display")
    display.innerText = random_quote
    
    # Додаємо легку анімацію появи через JS стилі
    display.style.opacity = "0"
    js.setTimeout(create_proxy(lambda: setattr(display.style, "opacity", "1")), 50)

# Створюємо проксі для функції, щоб JS міг її викликати
click_proxy = create_proxy(generate_quote)
js.document.getElementById("quote-button").addEventListener("click", click_proxy)

# Анімація зірок (створення об'єктів)
star_field = js.document.getElementById("star-field")
for i in range(50):
    star = js.document.createElement("div")
    star.className = "star"
    star.style.left = f"{random.random() * 100}vw"
    star.style.animationDuration = f"{random.random() * 3 + 2}s"
    star.style.animationDelay = f"{random.random() * 5}s"
    star_field.appendChild(star)

# Приховуємо напис завантаження
js.document.getElementById("loading").style.display = "none"