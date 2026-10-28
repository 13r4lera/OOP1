class People:
    def __init__(self):
        self.data = []

    def add(self, surname, name, phone, date):
        self.data.append({
            "фамилия": surname,
            "имя": name,
            "телефон": phone,
            "дата": date
        })

    def show(self, month):
        found = False
        for p in sorted(self.data, key=lambda x: x["фамилия"]):
            if p["дата"][1] == month:
                print(p)
                found = True
        if not found:
            print("Никого нет")

__all__ = ["People"]