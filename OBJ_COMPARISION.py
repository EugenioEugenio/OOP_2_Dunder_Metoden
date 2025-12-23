


import functools

@functools.total_ordering
class Millimeter:
    """Базовый класс для представления измерений в миллиметрах."""
    label = "mm"
    # Коэффициенты пересчета в миллиметры для дочерних классов
    ratio = 1.0

    def __init__(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Значение должно быть числом (int или float).")
        self.value = value

    def as_millimeters(self):
        """Возвращает значение в миллиметрах."""
        return self.value * self.ratio

    def __eq__(self, other):
        """Проверяет равенство объектов через их хэш."""
        if not isinstance(other, Millimeter):
            return NotImplemented
        # Сравнение через хэш, как указано в задании
        return hash(self) == hash(other)

    def __le__(self, other):
        """Проверяет, меньше или равно ли значение в миллиметрах."""
        if not isinstance(other, Millimeter):
            return NotImplemented
        # Сравнение значений в миллиметрах
        return self.as_millimeters() <= other.as_millimeters()

    def __hash__(self):
        """Возвращает хэш объекта на основе значения в миллиметрах."""
        # Хэш рассчитывается на основе значения в миллиметрах
        return hash(self.as_millimeters())

    def __repr__(self):
        """Строковое представление объекта для отладки."""
        return f"{self.__class__.__name__}({self.value})"

# --- Дочерние классы ---

class Centimeter(Millimeter):
    """Класс для представления измерений в сантиметрах."""
    ratio = 10.0 # 1 см = 10 мм
    label = "cm"
class Meter(Millimeter):
    """Класс для представления измерений в метрах."""
    ratio = 1000.0 # 1 м = 1000 мм
    label = "m"
class Inch(Millimeter):
    """Класс для представления измерений в дюймах."""
    ratio = 25.4 # 1 дюйм = 25.4 мм (приблизительно)
    label = "inc"
# Создание объектов различных классов
mm = Millimeter(10)        # 10 мм
cm = Centimeter(100)  # 100 сантиметров
inc = Inch(40)      # 40 дюймов (примерно 1016 мм)
m = Meter(1) # 1 метр

print(f"mm: {mm!r} ({mm.as_millimeters()} мм)")
print(f"cm: {cm!r} ({cm.as_millimeters()} мм)")
print(f"inc: {inc!r} ({inc.as_millimeters()} мм)")
print(f"m: {m!r} ({m.as_millimeters()} мм)")
print("-" * 30)

# Демонстрация __eq__ (равенство через хэш)
# 1 метр == 100 сантиметров
print(f"m == cm : {m == cm}")  # True

# Демонстрация методов сравнения, реализованных через @total_ordering и __le__
print(f"mm <= inc : {mm <= inc}")
print(f"m <= cm : {m <= cm}")
print(f"m <= m : {m <= m}")
print(f"inc <= m : {inc <= m}")

# Демонстрация хэширования
print(f"hash(m) == hash(cm): {hash(m) == hash(cm)}") # True
