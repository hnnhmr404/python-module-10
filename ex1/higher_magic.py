from typing import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int):
        result1 = spell1(target, power)
        result2 = spell2(target, power)
        return (result1, result2)

    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(target: str, power: int):
        return base_spell(target, power * multiplier)

    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def conditional(target: str, power: int):
        if condition(target, power):
            return spell(target, power)

        return "Spell fizzled"

    return conditional


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(target: str, power: int):
        results = []

        for spell in spells:
            results.append(spell(target, power))

        return results

    return sequence


"""
def test_data() -> None:
    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target} for {power} damage"

    def heal(target: str, power: int) -> str:
        return f"Heals {target} for {power} HP"

    test_values = [5, 9, 12]
    test_targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']

    print("\n\n=== Testing spell_combiner ===")
    combined = spell_combiner(fireball, heal)(test_targets[0], test_values[0])
    print("Output:", combined)

    print("\n=== Testing power_amplifier ===")
    amplified = power_amplifier(fireball, multiplier=3)(test_targets[1], test_values[0])
    print("Output:", amplified)

    print("\n=== Testing conditional_caster ===")
    check = conditional_caster(lambda target, power: power >= test_values[1], fireball)
    print("Valid (Power 12 >= 9):", check(test_targets[2], test_values[2]))
    print("Invalid (Power 5 < 9):", check(test_targets[2], test_values[0]))

    print("\n=== Testing spell_sequence ===")
    sequence = spell_sequence([fireball, heal])(test_targets[3], test_values[2])
    print("Output:", sequence)
"""


def main() -> None:
    print("Testing spell combiner...")

    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target}"

    def heal(target: str, power: int) -> str:
        return f"Heals {target}"

    combined = spell_combiner(fireball, heal)
    result = combined("Dragon", 10)

    print("Combined spell result:", ", ".join(result))

    print("Testing power amplifier...")

    def measure_power(target: str, power: int) -> int:
        return power

    amplified = power_amplifier(measure_power, 3)

    original_power = 10
    amplified_result = amplified("Dragon", original_power)

    print(f"Original: {original_power}, Amplified: {amplified_result}")


if __name__ == "__main__":
    main()
#   test_data()
