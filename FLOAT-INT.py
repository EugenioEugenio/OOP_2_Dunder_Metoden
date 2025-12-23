


class Millimeter:
    """
    Класс для представления измерения.
    Предполагается, что внутреннее значение хранится в миллиметрах.
    """
    def __init__(self, value_millimeters):
        self.value_millimeters = value_millimeters

    def __int__(self):
        """
        Возвращает значение объекта в миллиметрах как целое число.
        """
        # 1 метр = 1000 миллиметров
        value_mm = self.value_millimeters # * 1000
        return int(value_mm)

    def __float__(self):
        """
        Возвращает значение объекта в метрах как число с плавающей точкой.
        """
        # 1 метр = 1000 миллиметров
        value_m = self.value_millimeters / 1000
        return float(value_m)

    def __str__(self):
        """
        Дополнительный метод для удобного отображения объекта при печати.
        """
        return f"{self.value_millimeters} мм"

# --- Использование класса ---

# Создаем объект со значением 123.456 мм
obj = Millimeter(123.456)

print(f"Объект: {obj}")

# Преобразование в целое число (миллиметры)
int_value = int(obj)
print(f"int(obj) -> {int_value} мм (целое число)")

# Преобразование в число с плавающей точкой (миллиметры)
float_value = float(obj)
print(f"float(obj) -> {float_value} м (число с плавающей точкой)")

# Пример с другим значением
obj_small = Millimeter(5.1)

print(f"\nОбъект: {obj_small}")
print(f"int(obj_small) -> {int(obj_small)} мм")
print(f"float(obj_small) -> {float(obj_small)} м")
