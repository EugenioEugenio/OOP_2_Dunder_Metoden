

class Millimeter:
    """
    Базовый класс для представления единиц измерения длины
    с возможностью конвертации в миллиметры.
    """
    def __init__(self, value):
        # Базовые атрибуты, которые будут переопределены или использованы дочерними классами
        self.label = 'mm'
        self.ratio = 1.0
        self.value = value

    def as_millimeters(self):
        """
        Возвращает значение объекта, преобразованное в миллиметры.
        """
        return self.value * self.ratio

    def __repr__(self):
        """
        Удобное строковое представление объекта.
        """
        return f"{self.value} {self.label}"

# --- Дочерние классы ---

class Centimeter(Millimeter):
    """Представляет значение в сантиметрах."""
    def __init__(self, value):
        super().__init__(value)
        self.label = 'cm'
        self.ratio = 10

class Meter(Millimeter):
    """Представляет значение в метрах."""
    def __init__(self, value):
        super().__init__(value)
        self.label = 'm'
        self.ratio = 1000

class Inch(Millimeter):
    """Представляет значение в дюймах."""
    def __init__(self, value):
        super().__init__(value)
        self.label = 'in'
        self.ratio = 25.4

# --- Пример использования ---

# Создаем экземпляры разных классов
m_val = Millimeter(100)
cm_val = Centimeter(15)
m_val_big = Meter(2.5)
in_val = Inch(12)

print(f"{m_val} в мм: {m_val.as_millimeters()} мм")
print(f"{cm_val} в мм: {cm_val.as_millimeters()} мм")
print(f"{m_val_big} в мм: {m_val_big.as_millimeters()} мм")
print(f"{in_val} в мм: {in_val.as_millimeters()} мм")

