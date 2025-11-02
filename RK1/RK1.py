
# Рубежный контроль №1 (Вариант В)
# Предметная область: "Деталь" и "Производитель"
# Связи: один-ко-многим (Производитель -> Деталь) и многие-ко-многим (Производитель <-> Деталь)
# Требования запросов (В):
# 1) (1:M) Вывести список всех деталей, у которых название начинается с буквы "А", и названия их производителей.
# 2) (1:M) Вывести список производителей с минимальной ценой детали у каждого, отсортированный по минимальной цене.
# 3) (M:N) Вывести список всех связанных деталей и производителей, отсортированный по деталям (производители внутри — произвольно).
#
# При реализации используем функциональный стиль: list/dict comprehensions, map, filter, sorted, lambda.

from dataclasses import dataclass
from typing import List, Tuple, Dict


# ---------- Классы данных ----------

@dataclass
class Manufacturer:
    id: int
    name: str


@dataclass
class Part:
    id: int
    name: str
    price: int          # количественный признак на стороне "много"
    manufacturer_id: int  # для связи один-ко-многим


@dataclass
class PartManufacturer:
    part_id: int
    manufacturer_id: int  # для связи многие-ко-многим


# ---------- Тестовые данные (3-5+ записей) ----------

manufacturers: List[Manufacturer] = [
    Manufacturer(1, "АЛЬФА-Мех"),
    Manufacturer(2, "БетаПром"),
    Manufacturer(3, "Гамма-Сталь"),
    Manufacturer(4, "АвтоДеталь"),
    Manufacturer(5, "Аксис"),
]

parts: List[Part] = [
    Part(1, "Амортизатор", 5200, 4),
    Part(2, "Антенна", 900, 2),
    Part(3, "Болт", 30, 1),
    Part(4, "Адаптер", 700, 5),
    Part(5, "Клапан", 1350, 3),
    Part(6, "Фильтр", 850, 4),
]

# Многие-ко-многим: часть может выпускаться разными производителями (например, по лицензии)
part_manufacturer_links: List[PartManufacturer] = [
    PartManufacturer(1, 4),  # Амортизатор — АвтоДеталь
    PartManufacturer(1, 1),  # Амортизатор — АЛЬФА-Мех
    PartManufacturer(2, 2),  # Антенна — БетаПром
    PartManufacturer(2, 5),  # Антенна — Аксис
    PartManufacturer(3, 1),  # Болт — АЛЬФА-Мех
    PartManufacturer(3, 3),  # Болт — Гамма-Сталь
    PartManufacturer(4, 5),  # Адаптер — Аксис
    PartManufacturer(5, 3),  # Клапан — Гамма-Сталь
    PartManufacturer(6, 4),  # Фильтр — АвтоДеталь
]


# ---------- Вспомогательные индексы ----------

# Для 1:M — индекс производителя по id (O(1) доступ)
id_to_manufacturer: Dict[int, Manufacturer] = {m.id: m for m in manufacturers}

# Для M:N — создадим "словарь смежности" деталь -> список производителей
# (группировка через dict comprehension + заполнение)
from collections import defaultdict
part_to_manufs: Dict[int, List[int]] = defaultdict(list)
for link in part_manufacturer_links:
    part_to_manufs[link.part_id].append(link.manufacturer_id)


# ---------- Запрос 1 (В.1) ----------
# (1:M) Детали, название которых начинается на "А", и их производители.
# Используем list comprehension + фильтрацию по первой букве (кириллица "А").

def query_v1(parts: List[Part]) -> List[Tuple[str, str]]:
    # (имя детали, имя производителя) — по связи 1:M
    return sorted(
        [
            (p.name, id_to_manufacturer[p.manufacturer_id].name)
            for p in parts
            if p.name.startswith("А")
        ],
        key=lambda t: (t[0].lower(), t[1].lower()),
    )


# ---------- Запрос 2 (В.2) ----------
# (1:M) Производители с минимальной ценой детали у каждого, отсортированные по этой минимальной цене.
# Используем группировку компрехеншеном + min с generator expression + sorted.

def query_v2(parts: List[Part]) -> List[Tuple[str, int]]:
    # Сначала сгруппируем цены по производителю
    man_id_to_prices: Dict[int, List[int]] = defaultdict(list)
    for p in parts:
        man_id_to_prices[p.manufacturer_id].append(p.price)

    # Затем найдём минимум по каждому производителю (если у производителя нет деталей — пропускаем)
    tuples = [
        (id_to_manufacturer[mid].name, min(prices))
        for mid, prices in man_id_to_prices.items()
        if prices  # защита от пустых
    ]

    # Отсортируем по минимальной цене, затем по названию производителя
    return sorted(tuples, key=lambda t: (t[1], t[0].lower()))


# ---------- Запрос 3 (В.3) ----------
# (M:N) Все связанные детали и производители, отсортировано по деталям.
# Сформируем список (имя детали, [имена производителей]) с сортировкой по имени детали.

def query_v3(parts: List[Part]) -> List[Tuple[str, List[str]]]:
    # Словарь id детали -> имя детали
    id_to_part_name = {p.id: p.name for p in parts}

    # Построим (имя детали -> отсортированный список имён производителей)
    name_to_manuf_names: Dict[str, List[str]] = {
        id_to_part_name[pid]: sorted(
            [id_to_manufacturer[mid].name for mid in mids],
            key=str.lower,
        )
        for pid, mids in part_to_manufs.items()
    }

    # Вернём как отсортированный по имени детали список кортежей
    return sorted(name_to_manuf_names.items(), key=lambda t: t[0].lower())


# ---------- Запуск и вывод ----------

if __name__ == "__main__":
    print("=== В.1: Детали, начинающиеся на 'А', и их производители (1:M) ===")
    for part_name, manuf_name in query_v1(parts):
        print(f"{part_name} — {manuf_name}")

    print("\n=== В.2: Минимальная цена детали по каждому производителю (1:M) ===")
    for manuf_name, min_price in query_v2(parts):
        print(f"{manuf_name}: {min_price} ₽")

    print("\n=== В.3: Все связи Деталь—Производитель (M:N), отсортировано по деталям ===")
    for part_name, manuf_names in query_v3(parts):
        mans_str = ", ".join(manuf_names)
        print(f"{part_name}: {mans_str}")
