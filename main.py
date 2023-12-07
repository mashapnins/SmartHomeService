from home_manager import HomeManager
import threading
def main():
    home_manager = HomeManager()

    # Добавляем устройства для тестирования
    device1 = home_manager.add_device(1, "Smart Light")
    device2 = home_manager.add_device(2, "Smart Thermostat")

    # Создаем потоки для включения и выключения устройств
    turn_on_thread = threading.Thread(target=device1.turn_on)
    turn_off_thread = threading.Thread(target=device2.turn_off)

    # Запускаем потоки
    turn_on_thread.start()
    turn_off_thread.start()

    # Ждем завершения потоков перед выводом статусов устройств
    turn_on_thread.join()
    turn_off_thread.join()

    # Выводим текущее состояние устройств
    print("Current Devices:")
    for device in home_manager.get_devices():
        print(f"{device.name}: {device.get_status()}")


if __name__ == "__main__":
    main()
