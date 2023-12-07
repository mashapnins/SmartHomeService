class Device:
    """
    Представляет устройство в умном доме.

    Атрибуты:
    - name (str): Название устройства.
    - type (str): Тип устройства.
    - is_on (bool): Указывает, включено ли устройство в данный момент или выключено.
    """
    def __init__(self, device_id, name):
        """
        Инициализирует новый экземпляр класса Device.

        Параметры:
        - name (str): Название устройства.
        - device_type (str): Тип устройства.
        """
        self.id = device_id
        self.name = name
        self.status = "off"

    def turn_on(self):
        """
        Включает устройство.
        """
        self.status = 'on'
        print(f"{self.name} теперь включено")

    def turn_off(self):
        """
        Выключает устройство.
        """
        self.status = 'off'
        print(f"{self.name} теперь выключено")
    
    def change_status(self, new_status):
        """
        Меняет статус устройства
        """
        self.status = new_status

    def get_status(self):
        """
        Получение статуса устройства
        """
        return self.status