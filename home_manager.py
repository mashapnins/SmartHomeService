from device import Device

class HomeManager:
    def __init__(self):
        self.devices = []

    def add_device(self, device_id, name):
        new_device = Device(device_id, name)
        self.devices.append(new_device)
        return new_device

    def get_devices(self):
        return self.devices

    def remove_device(self, device_id):
        # Заглушка для удаления устройства по его идентификатору
        pass

    def execute_action(self, device_id, action):
        # Заглушка для выполнения действия на устройстве
        pass

    def log_action(self, action):
        # Заглушка для логирования действий
        pass