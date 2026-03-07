import pyautogui
from gigachat import GigaChat
import pyperclip

# Твой ключ остается тем же
AUTH_KEY = "MDE5YTYxMjQtMTEwYy03Zjg0LWFlNTgtZTg1NDBmYjA5YTc4OjUxMzFiNjlkLTgyNmYtNDhkMS1iZjUwLTJjYjg1MmJkNjNiNA=="

def fast_solve():
    print("📸 1. Делаю скриншот окна (на всякий случай)...")
    pyautogui.screenshot("my_screen.png")
    
    print("📋 2. Беру текст из буфера...")
    text_from_buffer = pyperclip.paste()
    
    if not text_from_buffer:
        return "Елена, выдели текст ошибки и нажми Ctrl+C!"

    print("🧠 3. GigaChat анализирует твой код...")
    with GigaChat(credentials=AUTH_KEY, verify_ssl_certs=False) as giga:
        prompt = f"Я программист. Вот мой код или ошибка: '{text_from_buffer}'. Объясни по-русски, что не так?"
        
        response = giga.chat(prompt)
        # ИСПРАВЛЕНИЕ: берем нулевой элемент списка [0]
        return response.choices[0].message.content

if __name__ == "__main__":
    try:
        print("\n📝 ОТВЕТ ОТ СБЕРА:")
        print("-" * 30)
        print(fast_solve())
        print("-" * 30)
    except Exception as e:
        print(f"❌ Ошибка связи: {e}")
