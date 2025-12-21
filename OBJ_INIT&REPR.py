

class Millimeter:
    #Базовый класс для представления единиц измерения длины.
    label = "mm"
    ratio = 1.0  # Коэффициент пересчета в миллиметры

    def __init__(self, value):            #Инициализирует объект, обрабатывая различные типы входных данных.
        if isinstance(value, (int, float)):
            # Если передано число, сохраняем его как float
            self._value = float(value)
        elif isinstance(value, Millimeter):
            # Если передан объект другого класса-единицы измерения
            # Конвертируем его значение в миллиметры, затем делим на ratio текущего класса
            millimeters_value = value.as_millimeters()
            self._value = millimeters_value / self.ratio
        else:
            raise TypeError(f"Неподдерживаемый тип значения: {type(value)}")

    def as_millimeters(self):       #Возвращает значение объекта в миллиметрах

        return self._value * self.ratio

    def __repr__(self):   #Возвращает строковое представление объекта, например 'Centimeter(10)
    # Используем имя класса и значение атрибута _value
        return f"{self.__class__.__name__}({self._value})"

# Определение дочерних классов с заданными коэффициентами пересчета
class Centimeter(Millimeter):
    label = "cm"
    ratio = 10.0

class Meter(Millimeter):
    label = "m"
    ratio = 1000.0

class Inch(Millimeter):
    label = "in"
    ratio = 25.4

# --- Примеры использования ---

# 1. Создание объектов из числовых значений
mm_val = Millimeter(500.43)
cm_val = Centimeter(10.6)
m_val = Meter(1.551)
inch_val = Inch(2.567)

print(f"Представление объектов: {mm_val!r}, {cm_val!r}, {m_val!r}, {inch_val!r}")

# 2. Использование метода as_millimeters()
print('-'*80)
print(f"{mm_val} в мм: {mm_val.as_millimeters()} мм")
print(f"{cm_val} в мм: {cm_val.as_millimeters()} мм")
print(f"{m_val} в мм: {m_val.as_millimeters()} мм")
print(f"{inch_val} в мм: {inch_val.as_millimeters()} мм")











