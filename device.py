class Device:
    def __init__(self, device_id, name):
        self.id = device_id
        self.name = name
        self.status = "off"

    def change_status(self, new_status):
        self.status = new_status

    def get_status(self):
        return self.status