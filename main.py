from home_manager import HomeManager

def main():
    home_manager = HomeManager()

    # Добавляем устройства для тестирования
    device1 = home_manager.add_device(1, "Smart Light")
    device2 = home_manager.add_device(2, "Smart Thermostat")
    
    # Изменяем статус устройств
    device1.change_status("on")
    device2.change_status("off")

    # Выводим текущее состояние устройств
    print("Current Devices:")
    for device in home_manager.get_devices():
        print(f"{device.name}: {device.status}")


if __name__ == "__main__":
    main()
