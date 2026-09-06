from typing import Callable


def mage_counter() -> Callable:
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> Callable:
    total = initial_power

    def add_power(amount: int):
        nonlocal total
        total += amount
        return total

    return add_power


def enchantment_factory(enchantment_type: str) -> Callable:

    def enchant(item_name: str):
        return f"{enchantment_type} {item_name}"

    return enchant


def memory_vault() -> dict[str, Callable]:

    memory = {}

    def store(key, value):
        memory[key] = value

    def recall(key):
        return memory.get(key, "Memory not found")

    return {
        "store": store,
        "recall": recall
    }


"""
def test_data() -> None:
    initial_powers = [45, 24, 61]
    power_additions = [16, 14, 8, 5, 14]
    enchantment_types = ["Frozen", "Windy", "Flowing"]
    items_to_enchant = ["Ring", "Amulet", "Wand", "Cloak"]

    print("\n\nTesting mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")

    print("\nTesting spell accumulator...")
    base_power = initial_powers[0]
    acc = spell_accumulator(base_power)
    pa0 = power_additions[0]
    pa1 = power_additions[1]
    print(f"Base {base_power}, add {pa0}: {acc(pa0)}")
    print(f"Base {base_power}, add {pa1}: {acc(pa1)}")

    print("\nTesting enchantment factory...")
    type0 = enchantment_factory(enchantment_types[0])
    type1 = enchantment_factory(enchantment_types[1])
    print(type0(items_to_enchant[0]))
    print(type1(items_to_enchant[1]))

    print("\nTesting memory vault...")
    vault = memory_vault()
    vault["store"]("secret", initial_powers[0])
    print(f"Store 'secret' = {initial_powers[0]}")
    print(f"Recall 'secret': {vault['recall']('secret')}")
    print(f"Recall 'unknown': {vault['recall']('unknown')}")
"""


def main() -> None:
    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()

    print("counter_a call 1:", counter_a())
    print("counter_a call 2:", counter_a())
    print("counter_b call 1:", counter_b())

    print("\nTesting spell accumulator...")
    accumulator = spell_accumulator(100)

    print("Base 100, add 20:", accumulator(20))
    print("Base 100, add 30:", accumulator(30))

    print("\nTesting enchantment factory...")
    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")

    print(flaming("Sword"))
    print(frozen("Shield"))

    print("\nTesting memory vault...")
    vault = memory_vault()

    vault["store"]("secret", 42)
    print("Store 'secret' = 42")

    print("Recall 'secret':", vault["recall"]("secret"))
    print("Recall 'unknown':", vault["recall"]("unknown"))


if __name__ == "__main__":
    main()
#   test_data()
