import pystray
from pystray import MenuItem as item
from PIL import Image, ImageDraw
import subprocess
import threading
import os
import signal
import psutil
# Глобальная переменная для состояния переключателя и процессов
switch_state = False
process_winws = None  # Процесс для winws.exe
service_name = "zapret_service"
repo_url = "https://github.com/username/project"  # Замените на URL вашего репозитория
repo_dir = script_dir = os.path.dirname(os.path.realpath(__file__)) 
print(repo_dir) 

# Функция для рисования изображения переключателя
def create_switch_image(state):
    image = Image.new('RGBA', (64, 32), (255, 255, 255, 255))
    draw = ImageDraw.Draw(image)
    if state:
        draw.rectangle([32, 4, 60, 28], fill="green")
    else:
        draw.rectangle([4, 4, 32, 28], fill="red")
    return image

# Функция для переключения состояния
def toggle_switch(icon, item):
    global switch_state, process_winws
    switch_state = not switch_state
    icon.icon = create_switch_image(switch_state)

    if switch_state:
        start_script()
    else:
        stop_script()

    print("Переключатель", "Включен" if switch_state else "Выключен")
    icon.update_menu()

def read_output(process):
    """Функция для чтения и вывода stdout и stderr в реальном времени"""
    for line in process.stdout:
        print("stdout:", line.strip())
    for line in process.stderr:
        print("stderr:", line.strip())

def create_service(icon=None):
    global process_create_service, switch_state

    try:
        script_dir = os.path.dirname(os.path.realpath(__file__))
        cmd_path = os.path.join(script_dir, "service.cmd")

        # Запуск через PowerShell с правами администратора
        subprocess.run([
            "powershell", 
            "-Command", 
            f"Start-Process '{cmd_path}' -Verb RunAs"
        ])
        
        switch_state = True
        icon.icon = create_switch_image(switch_state)
        icon.update_menu()

        print("Запуск service.cmd с правами администратора прошел успешно")
    except Exception as e:
        print(f"Ошибка при запуске service.cmd: {e}")

# Функция для запуска скриптов
def start_script():
    global service_winws_start

    try:
        script_dir = os.path.dirname(os.path.realpath(__file__))
        # Полная команда с параметрами, которую нужно выполнить
        subprocess.run(
            ["powershell", "-Command", f"Start-Process sc -ArgumentList 'start {service_name}' -Verb RunAs"],
            check=True,
            creationflags=subprocess.CREATE_NO_WINDOW
        )
        print(f"Служба {service_name} запущена успешно.")


        print("Запуск службы прошел успешно")

    except Exception as e:
        print(f"Ошибка при запуске службы: {e}")

# Функция для остановки скриптов
def stop_script():
    global service_winws_stop
    try:
        # Полная команда с параметрами, которую нужно выполнить
        subprocess.run(
            ["powershell", "-Command", f"Start-Process sc -ArgumentList 'stop {service_name}' -Verb RunAs"],
            check=True,
            creationflags=subprocess.CREATE_NO_WINDOW
        )
        print(f"Служба {service_name} остановлена успешно.")

    except Exception as e:
        print(f"Ошибка при остановке службы: {e}")


def update_from_github(icon, item):
    try:
        # Проверяем, существует ли локальная папка проекта
        if not os.path.isdir(repo_dir):
            print("Клонирование репозитория...")
            subprocess.run(["git", "clone", repo_url, repo_dir], check=True)
        else:
            print("Получение обновлений из GitHub...")
            subprocess.run(["git", "-C", repo_dir, "pull"], check=True)
        print("Файлы успешно обновлены из GitHub.")
    except Exception as e:
        print(f"Ошибка при обновлении из GitHub: {e}")


# Функция для создания меню
def create_menu():
    return (
        item("Переключить", toggle_switch),
        item("Создать службу", lambda icon, item: create_service(icon)),
        item("Установить последнее обновление", update_from_github),
        item("Выход", exit_application)
    )

# Функция для выхода из приложения
def exit_application(icon, item):
    stop_script()
    icon.stop()

# Функция для запуска иконки в системном трее
def run_tray_icon():
    icon = pystray.Icon("test_icon", create_switch_image(switch_state), menu=create_menu())
    # Передаем icon в create_service через lambda
    icon.menu = pystray.Menu(
        item("Переключить", toggle_switch),
        item("Создать службу", lambda item: create_service(icon)),
        item("Установить последнее обновление", update_from_github),
        item("Выход", exit_application)
    )
    icon.run()

# Запускаем в отдельном потоке, чтобы GUI не блокировал выполнение
def start_tray():
    tray_thread = threading.Thread(target=run_tray_icon)
    tray_thread.daemon = True
    tray_thread.start()

# Главная функция
if __name__ == "__main__":
    start_tray()
    while True:
        pass
