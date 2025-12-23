
class Millimeter:
    """Базовый класс для представления измерений в миллиметрах."""
    ratio = 1.0  # Коэффициент преобразования в миллиметры (1 мм = 1 мм)

    def __init__(self, value):
        # Храним значение в единицах данного класса
        self.value = value

    def as_millimeters(self):
        """Конвертирует текущее значение в миллиметры."""
        return self.value * self.ratio

    @classmethod
    def from_millimeters(cls, millimeters):
        """Создает объект данного класса из значения в миллиметрах."""
        # Обратное преобразование: мм / ratio
        return cls(millimeters / cls.ratio)

    # --- Арифметические методы ---

    def __add__(self, other):         #Сложение двух объектов измерения
        # 1. Конвертируем оба операнда в миллиметры
        mm_self = self.as_millimeters()
        if isinstance(other, (Millimeter, int, float)):
            # Если other тоже является классом измерения или числом,
            # конвертируем other в миллиметры (если это число, считаем, что оно в мм, или просто число)
            mm_other = other.as_millimeters() if isinstance(other, Millimeter) else other
        else:
            # Если other несовместимый тип, Python вызовет TypeError
            return NotImplemented

        # 2. Выполняем сложение в миллиметрах
        result_mm = mm_self + mm_other

        # 3. Преобразуем результат обратно в тип левого операнда (type(self))
        return type(self).from_millimeters(result_mm)

    def __sub__(self, other):
        """Вычитание одного объекта из другого."""
        # Логика аналогична сложению
        mm_self = self.as_millimeters()

        if isinstance(other, (Millimeter, int, float)):
            mm_other = other.as_millimeters() if isinstance(other, Millimeter) else other
        else:
            return NotImplemented

        result_mm = mm_self - mm_other

        return type(self).from_millimeters(result_mm)

    def __mul__(self, factor):
        """Умножение объекта на число (коэффициент)."""
        if not isinstance(factor, (int, float)):
            raise TypeError(f"Коэффициент должен быть числом, а не {type(factor).__name__}")

        # Умножаем значение объекта (в его родных единицах) на коэффициент
        # или можно работать через мм:
        # result_mm = self.as_millimeters() * factor
        # return type(self).from_millimeters(result_mm)

        # Умножаем текущее хранимое значение, это проще
        new_value = self.value * factor
        return type(self)(new_value)


    def __truediv__(self, factor):
        """Деление объекта на число (коэффициент)."""
        if not isinstance(factor, (int, float)):
            raise TypeError(f"Коэффициент должен быть числом, а не {type(factor).__name__}")
        if factor == 0:
            raise ZeroDivisionError("Деление на ноль невозможно.")

        # Делим текущее хранимое значение
        new_value = self.value / factor
        return type(self)(new_value)

    def __str__(self):
        """Представление объекта в виде строки для удобства чтения."""
        # Можно переопределить в дочерних классах для добавления единиц измерения
        return f"{self.value:.2f}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.value})"


class Centimeter(Millimeter):
    ratio = 10  # 1 см = 10 мм

    def __str__(self):
        return f"{self.value:.2f} cm"

class Meter(Millimeter):
    ratio = 1000  # 1 м = 1000 мм

    def __str__(self):
        return f"{self.value:.2f} m"

class Inch(Millimeter):
    ratio = 25.4

    def __str__(self):
        return f"{self.value:.2f} in"


# Создание объектов
m1 = Meter(1.5)
cm1 = Centimeter(50.6)
inch1 = Inch(10.9)
mm1 = Millimeter(100.7)

print(f"Объекты для теста:")
print(f"  m1: {m1!r} -> {m1.as_millimeters()} мм")
print(f"  cm1: {cm1!r} -> {cm1.as_millimeters()} мм")
print(f"  inch1: {inch1!r} -> {inch1.as_millimeters()} мм")
print(f"  mm1: {mm1!r} -> {mm1.as_millimeters()} мм")
print("-" * 80)


# --- 1. Сложение и вычитание (Результат в типе левого операнда) ---

# Сложение: Meter + Centimeter = Meter
res_add_m_cm = m1 + cm1

print(f"Сложение (Meter + Centimeter): {m1} + {cm1} = {res_add_m_cm!r} -> {res_add_m_cm}")

# Вычитание: Centimeter - Inch = Centimeter
res_sub_cm_in = cm1 - inch1
print(f"Вычитание (Centimeter - Inch): {cm1} - {inch1} = {res_sub_cm_in!r} -> {res_sub_cm_in}")

# Сложение: Inch + Millimeter = Inch
res_add_in_mm = inch1 + mm1
print(f"Сложение (Inch + Millimeter): {inch1} + {mm1} = {res_add_in_mm!r} -> {res_add_in_mm}")

print("-" * 80)

# --- 2. Умножение и деление (Результат в типе операнда) ---
res_mul = m1 * 2.5
print(f"Умножение (Meter * 2.5): {m1} * 2.5 = {res_mul!r} -> {res_mul}")

# Деление: Centimeter / 4 = Centimeter
res_div = cm1 / 4
print(f"Деление (Centimeter / 4): {cm1} / 4 = {res_div!r} -> {res_div}")

# Деление: Inch / 2 = Inch
res_div_in = inch1 / 2
print(f"Деление (Inch / 2): {inch1} / 2 = {res_div_in!r} -> {res_div_in}")

