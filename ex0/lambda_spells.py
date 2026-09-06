from typing import Any
# from data_generator import FuncMageDataGenerator


def artifact_sorter(artifacts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(
        artifacts,
        key=lambda artifact: artifact["power"],
        reverse=True
    )


def power_filter(
    mages: list[dict[str, Any]], min_power: int
) -> list[dict[str, Any]]:
    return list(
        filter(
            lambda mage: mage["power"] >= min_power,
            mages
        )
    )


def spell_transformer(spells: list[str]) -> list[str]:
    return list(
        map(
            lambda spell: f"* {spell} *",
            spells
        )
    )


def mage_stats(mages: list[dict[str, Any]]) -> dict[str, Any]:
    max_mage = max(mages, key=lambda m: m["power"])
    min_mage = min(mages, key=lambda m: m["power"])
    total_power = sum(map(lambda m: m["power"], mages))
    avg_power = round(total_power / len(mages), 2)

    return {
        "max_power": max_mage["power"],
        "min_power": min_mage["power"],
        "avg_power": avg_power
    }


"""
def test_data() -> None:
    artifacts = FuncMageDataGenerator.generate_artifacts(3)
    print(f"\n\nArtifacts: {artifacts}")
    print("\nSorted Artifacts:")
    print(artifact_sorter(artifacts))
    mages = FuncMageDataGenerator.generate_mages(5)
    print(f"\nMages: {mages}")
    print("\nMages with Power >= 70:")
    print(power_filter(mages, 70))
    spells = FuncMageDataGenerator.generate_spells(3)
    print(f"\nSpells: {spells}")
    print("\nTransformed Spells:")
    print(spell_transformer(spells))
    print("\nMage Stats:")
    print(mage_stats(mages))
"""


def main() -> None:
    print("Testing artifact sorter...")
    artifacts = [
        {"name": "Crystal Orb", "power": 85},
        {"name": "Fire Staff", "power": 92},
    ]
    sorted_artifacts = artifact_sorter(artifacts)
    first = sorted_artifacts[0]
    second = sorted_artifacts[1]
    print(
        f"{first['name']} ({first['power']} power) comes before "
        f"{second['name']} ({second['power']} power)"
    )

    print("\nTesting spell transformer...")
    spells = ["fireball", "heal", "shield"]
    transformed = spell_transformer(spells)
    print(" ".join(transformed))


if __name__ == "__main__":
    main()
#   test_data()
