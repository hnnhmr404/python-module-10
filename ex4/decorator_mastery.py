import time
from functools import wraps
from typing import Callable


def spell_timer(func: Callable) -> Callable:
    """Measure and display the execution time of a function."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")

        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        elapsed = end_time - start_time
        print(f"Spell completed in {elapsed:.3f} seconds")

        return result

    return wrapper


def power_validator(min_power: int) -> Callable:
    """Create a decorator that checks spell power."""

    def decorator(func: Callable) -> Callable:

        @wraps(func)
        def wrapper(*args, **kwargs):
            # Get power from the function arguments
            if "power" in kwargs:
                power = kwargs["power"]
            else:
                # For methods, args[0] is self
                # args[1] is spell_name
                # args[2] is power
                power = args[-1]

            if power >= min_power:
                return func(*args, **kwargs)

            return "Insufficient power for this spell"

        return wrapper

    return decorator


def retry_spell(max_attempts: int) -> Callable:
    """Retry a spell if it raises an exception."""

    def decorator(func: Callable) -> Callable:

        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(
                            f"Spell failed, retrying... "
                            f"(attempt {attempt}/{max_attempts})"
                        )

            return (
                f"Spell casting failed after "
                f"{max_attempts} attempts"
            )

        return wrapper

    return decorator


class MageGuild:

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        """Check whether a mage name is valid."""

        if len(name) < 3:
            return False

        return all(char.isalpha() or char == " " for char in name)

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        """Cast a spell if the mage has enough power."""

        return f"Successfully cast {spell_name} with {power} power"


@spell_timer
def fireball() -> str:
    """Cast a fireball."""

    time.sleep(0.1)
    return "Fireball cast!"


@retry_spell(3)
def unreliable_spell() -> str:
    """A spell that always fails."""

    raise Exception("Spell failed")


"""
def test_data() -> None:
    test_powers = [16, 18, 26, 28]
    spell_names = ["heal", "earthquake", "freeze", "shield"]
    mage_names = ["Ash", "River", "Sage", "Alex", "Storm", "Luna"]
    invalid_names = ["Jo", "A", "Alex123", "Test@Name"]

    print("Testing spell timer...")
    result = fireball()
    print(f"Result: {result}")

    print("\nTesting standalone power validator...")

    @power_validator(20)
    def cast_arcane(power: int) -> str:
        return f"Arcane explosion with power {power}"

    print(cast_arcane(power=test_powers[2]))
    print(cast_arcane(power=test_powers[0]))

    print("\nTesting retrying spell...")
    # Test retry on permanent failure
    result = unreliable_spell()
    print(result)

    # Test retry on temporary failure (succeeds on attempt 2)
    attempts = 0

    @retry_spell(3)
    def temporary_failing_spell() -> str:
        nonlocal attempts
        attempts += 1
        if attempts < 2:
            raise Exception("Temporary disruption")
        return "Spell cast successfully on attempt 2!"

    print(temporary_failing_spell())

    print("Waaaaaaagh spelled !")

    print("\nTesting MageGuild staticmethod...")
    print(
          f"Valid name '{mage_names[0]}':",
          MageGuild.validate_mage_name(mage_names[0])
         )
    print(
          f"Invalid name '{invalid_names[3]}':",
          MageGuild.validate_mage_name(invalid_names[3])
         )

    print("\nTesting MageGuild cast_spell...")
    guild = MageGuild()
    print(guild.cast_spell(spell_names[0], test_powers[0]))
    print(guild.cast_spell(spell_names[1], 5))
"""


def main() -> None:
    print("Testing spell timer...")
    result = fireball()
    print(f"Result: {result}")

    print("\nTesting retrying spell...")
    result = unreliable_spell()
    print(result)

    print("Waaaaaaagh spelled !")

    print("\nTesting MageGuild...")
    print(MageGuild.validate_mage_name("Gandalf"))
    print(MageGuild.validate_mage_name("G@ndalf"))

    guild = MageGuild()

    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Lightning", 5))


if __name__ == "__main__":
    main()
#   test_data()
