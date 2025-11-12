# 🧠🤖 Robots Only


Robots Only is a turn-based combat RPG where players choose from four powerful races — Fleshen, Osseins, Darkmon, or Bloodlings — and embark on a journey to conquer rival nations through strategy, magic, and brute strength.

The game features:

Character creation with race-specific abilities.

Dice-based combat for dynamic battles.

20 levels per nation and boss fights that test strategy and luck.

Unique endings depending on your chosen race.

What problem does this solve?
It offers a creative and strategic fantasy experience that blends storytelling, combat mechanics, and branching choices — all within a Python-based game that challenges the player to plan and adapt.

## Requirements

To run Robots Only, you’ll need the following:

Python 3.8+

A terminal or IDE that supports input() and print() (VS Code, PyCharm, etc.)

Optional: time and random libraries (already included with Python)

## Installation

Follow these steps to install and run the game:

Clone the repository
git clone https://github.com/yourusername/robots-only.git

Navigate to the directory
cd robots-only

Run the game
python robots_only.py


If you are using a virtual environment:

python -m venv myenv
source myenv/bin/activate  # macOS/Linux
myenv\Scripts\activate     # Windows
python robots_only.py

## Usage Examples
Start the Game

When you run the program, you’ll be greeted with the game introduction and prompted to choose your race:

Welcome to Robots Only RPG!
Choose your race:
1. Fleshen
2. Osseins
3. Darkmon
4. Bloodlings

Gameplay Example

The game progresses in levels and turns:

--- Bloodtopia Level 1 ---
Your Health: 120 | Enemy Health: 100
Actions: 1. Attack 2. Defend 3. Magic 4. Item


Each turn, you can:

Attack for physical damage.

Defend to restore small health.

Use Magic for elemental damage.

Use Items from your inventory.

Example Combat Turn
You attack and deal 15 damage!
Enemy casts magic and deals 10 damage!
You used a Health Potion! +50 health

Boss Battle Example

At level 20 of each nation, you’ll face the boss:

BOSS FIGHT: High Bloodlord!
The High Bloodlord summons fire rings!
You defend and survive the spell!
You deal a final strike and defeat the High Bloodlord!

## Game Features

🎭 Four Races with Distinct Styles:

Fleshen: Weapon and machinery masters.

Osseins: Skilled in armor and defense.

Darkmon: Physically dominant but emotionally unstable.

Bloodlings: Magical beings wielding powerful spells.

⚔️ Dynamic Combat System:

Dice-based outcomes (1–20 roll) for realistic chance-based combat.

Defend, attack, and magic actions with variable effects.

Race-specific enemies with weaknesses and special skills.

🏰 World Progression:

Conquer three rival nations (20 levels each).

Boss battles at every nation’s end.

Unlock rewards and items as you progress.

🧩 Branching Endings:

Each race has a unique ending that reveals their fate after conquering the world.

## Example Race Abilities

Race	Specialty	Example Power	Weakness
Fleshen	Machinery & Weapons	Cannon, Catapult, Battering Ram	Weak against magic
Osseins	Armor & Healing	Thorn Armor, Major Protection	Low strength
Darkmon	Physical Strength	Rage & Cry turns	Unstable emotions
Bloodlings	Magic Sorcery	Fire Ring, Decoy, Invulnerability	Low health

## Inventory & Rewards

After defeating each nation’s boss, players gain a unique item:

Nation	Reward
Bloodtopia	Magic Cast Spell
Osseinville	Enchanted Armor
Flaks Abyss	Strength & Health Boost
Talloo	Machinery Companion
8. Branching Endings

Your final ending depends on your chosen race:

Fleshen: Rule the world with machinery and dominance.

Osseins: Become the ultimate smiths of the land.

Darkmon: Find peace through strength.

Bloodlings: Spread magical reign across the world.

## Branching Endings

Your final ending depends on your chosen race:

Fleshen: Rule the world with machinery and dominance.

Osseins: Become the ultimate smiths of the land.

Darkmon: Find peace through strength.

Bloodlings: Spread magical reign across the world.

## Future Plans

Add voice narration for story progression.

Implement save/load system.

Expand with multiplayer combat mode.

Add cinematic boss animations and spell particle effects.

## Credits

Developed by: [ken-a-c]
Game Design, Story, and Code by: [ken-a-c]
