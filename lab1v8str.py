class Population:
    # Коэффициенты вероятности для каждого типа пары (в порядке из задания)
    DOMINANT_PROBS = [1.0, 1.0, 1.0, 0.75, 0.5, 0.0]
    OFFSPRING_PER_PAIR = 2  # Потомков от одной пары

    def __init__(self, counts):
        self.counts = counts  # Количество пар каждого типа

    def calculate_expected_dominant(self):
        total = 0.0
        for i in range(6):
            total += self.counts[i] * self.DOMINANT_PROBS[i]
        return total * self.OFFSPRING_PER_PAIR

    @classmethod
    def from_input(cls):
        """Создает объект популяции из ввода пользователя"""
        counts = [
            int(input("AA-AA pairs: ")),
            int(input("AA-Aa pairs: ")),
            int(input("AA-aa pairs: ")),
            int(input("Aa-Aa pairs: ")),
            int(input("Aa-aa pairs: ")),
            int(input("aa-aa pairs: ")),
        ]
        return cls(counts)


if __name__ == "__main__":
    # Создаем объект популяции
    population = Population.from_input()

    # Вычисляем и выводим результат
    expected = population.calculate_expected_dominant()
    print(f"Expected dominant offspring: {expected:.5f}")


    # Пример использования функции без ввода с клавиатуры
    pop = Population([1, 0, 0, 1, 0, 1])
    # Расчет ожидаемого значения
    print(pop.calculate_expected_dominant())
