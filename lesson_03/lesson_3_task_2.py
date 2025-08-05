from smartphone import Smartphone
catalog = [
    Smartphone(mark_phone="Samsung", model_phone="Galaxy",
               phone_number="+79143251116"),
    Smartphone(mark_phone="LG", model_phone="AP",
               phone_number="+79256347129"),
    Smartphone(mark_phone="Sony", model_phone="Ericsson",
               phone_number="+79111189229"),
    Smartphone(mark_phone="Apple", model_phone="SE",
               phone_number="+79114445399"),
    Smartphone(mark_phone="Xiaomi", model_phone="Poco",
               phone_number="+79211178225")
]

for smartphone in catalog:
    print(f"{smartphone.mark} - {smartphone.model}. {smartphone.number}")
