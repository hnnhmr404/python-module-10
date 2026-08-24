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


def main():
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
