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
