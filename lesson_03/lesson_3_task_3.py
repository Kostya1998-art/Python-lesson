from address import Address
from mailing import Mailing

toaddress = Address("456148", "Санкт-Петербург", "Верности", "19", "6")
fromaddress = Address("198625", "Москва", "Щукинская", "46", "78")

Mail = Mailing(toaddress, fromaddress, 4800, "JKL457")

print(f"Отправление {Mail.track} из {Mail.fromaddress.index},"
      f"{Mail.fromaddress.city},"
      f"{Mail.fromaddress.street}, {Mail.fromaddress.house} -"
      f"{Mail.fromaddress.flat},"
      f"в {Mail.toaddress.index}, {Mail.toaddress.city},"
      f"{Mail.toaddress.street},"
      f"{Mail.toaddress.house} - {Mail.toaddress.flat}."
      f"Стоимость {Mail.cost} рублей.")
