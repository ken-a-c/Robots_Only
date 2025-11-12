import random
import time

# -------------------------
# --- GAME DATA & RACES ---
# -------------------------

races = {
    "Fleshen": {
        "health": 120, "strength": 12, "magic": 5, "special": "Machinery",
        "weapons": ["Axe", "Mace", "Scythe"], 
        "machinery": ["Cannon", "Catapult", "Battering Ram"]
    },
    "Osseins": {
        "health": 100, "strength": 8, "magic": 5, "special": "Armor",
        "armor": ["Thorns", "Major Protection", "Healing"]
    },
    "Darkmon": {
        "health": 150, "strength": 18, "magic": 3, "special": "Brute Strength"
    },
    "Bloodlings": {
        "health": 80, "strength": 5, "magic": 20, "special": "Magic Spells",
        "spells": ["Fire Ring", "Decoy", "Invulnerability"]
    }
}

nations = {
    "Bloodtopia": "Bloodlings",
    "Osseinville": "Osseins",
    "Flaks Abyss": "Darkmon",
    "Talloo": "Fleshen"
}

# --- Bosses with cinematic abilities ---
bosses = {
    "Bloodlings": {
        "name": "High Bloodlord", "health": 250, "magic": 30, "strength": 10,
        "abilities": ["Double Spell", "Fire Ring", "Decoy"]
    },
    "Osseins": {
        "name": "King Osseins", "health": 300, "strength": 15, "armor": "Ultimate Shield",
        "abilities": ["Reflect Damage", "Heal", "Crushing Strike"]
    },
    "Darkmon": {
        "name": "Darkmon Titan", "health": 350, "strength": 30,
        "abilities": ["Rage Attack", "Bow Volley", "Stun Slam"]
    },
    "Fleshen": {
        "name": "Warlord Fleshen", "health": 280, "strength": 20, 
        "machinery": "Mega Cannon",
        "abilities": ["Cannon Blast", "Battering Ram", "Trap"]
    }
}

actions = ["attack", "defend", "magic", "item"]

# -------------------------
# --- PLAYER CREATION ---
# -------------------------

def create_player():
    print("Welcome to Robots Only RPG!")
    print("\nChoose your race:")
    for i, race in enumerate(races.keys(), 1):
        print(f"{i}. {race}")
    choice = int(input("Enter number: ")) - 1
    player_race = list(races.keys())[choice]
    player_stats = races[player_race].copy()
    
    inventory = []
    
    print(f"\nYou chose {player_race}!")
    
    if player_race == "Fleshen":
        print("\nChoose your weapon:")
        for i, w in enumerate(player_stats["weapons"], 1):
            print(f"{i}. {w}")
        weapon_choice = int(input("Weapon: ")) - 1
        player_stats["weapon"] = player_stats["weapons"][weapon_choice]
        
        print("\nChoose your machinery:")
        for i, m in enumerate(player_stats["machinery"], 1):
            print(f"{i}. {m}")
        machinery_choice = int(input("Machinery: ")) - 1
        player_stats["machinery_choice"] = player_stats["machinery"][machinery_choice]
        
    elif player_race == "Osseins":
        print("\nChoose starting armor:")
        for i, a in enumerate(player_stats["armor"], 1):
            print(f"{i}. {a}")
        armor_choice = int(input("Armor: ")) - 1
        player_stats["armor_choice"] = player_stats["armor"][armor_choice]
        
    elif player_race == "Bloodlings":
        print("\nChoose your starting spell:")
        for i, s in enumerate(player_stats["spells"], 1):
            print(f"{i}. {s}")
        spell_choice = int(input("Spell: ")) - 1
        player_stats["spell_choice"] = player_stats["spells"][spell_choice]
    
    return player_race, player_stats, inventory

# -------------------------
# --- DICE & DAMAGE ---
# -------------------------

def dice_roll():
    return random.randint(1, 20)

def calculate_damage(attacker, action):
    roll = dice_roll()
    if action == "attack":
        return attacker["strength"] + roll
    elif action == "magic":
        return attacker.get("magic", 0) + roll
    return 0

# -------------------------
# --- STATUS EFFECTS ---
# -------------------------

def darkmon_emotion():
    return random.random() < 0.2

def bloodling_decoy():
    return random.random() < 0.25

# -------------------------
# --- INVENTORY SYSTEM ---
# -------------------------

def use_item(player_stats, inventory):
    if not inventory:
        print("No items in inventory!")
        return
    print("\nInventory:")
    for i, item in enumerate(inventory, 1):
        print(f"{i}. {item}")
    choice = int(input("Choose item to use: ")) - 1
    item = inventory.pop(choice)
    if item == "Health Potion":
        player_stats["health"] += 50
        print("You used a Health Potion! +50 health")
    elif item == "Strength Boost":
        player_stats["strength"] += 5
        print("You used a Strength Boost! +5 strength")
    elif item == "Magic Boost":
        player_stats["magic"] += 5
        print("You used a Magic Boost! +5 magic")

# -------------------------
# --- BOSS ABILITY SYSTEM ---
# -------------------------

def boss_action(boss, player_stats):
    ability = random.choice(boss.get("abilities", []))
    
    if ability == "Double Spell":
        damage = boss["magic"] * 2 + dice_roll()
        print(f"{boss['name']} casts DOUBLE SPELL! Deals {damage} magic damage!")
        player_stats["health"] -= damage
    elif ability == "Fire Ring":
        damage = boss["magic"] + dice_roll()
        print(f"{boss['name']} uses FIRE RING! Deals {damage} magic damage!")
        player_stats["health"] -= damage
    elif ability == "Decoy":
        print(f"{boss['name']} uses DECOY! Avoids your next attack!")
    elif ability == "Reflect Damage":
        print(f"{boss['name']}'s armor reflects 50% of your next damage!")
    elif ability == "Heal":
        heal = 50 + dice_roll()
        boss["health"] += heal
        print(f"{boss['name']} heals for {heal} health!")
    elif ability == "Crushing Strike":
        damage = boss["strength"] * 2 + dice_roll()
        print(f"{boss['name']} uses CRUSHING STRIKE! Deals {damage} damage!")
        player_stats["health"] -= damage
    elif ability == "Rage Attack":
        damage = boss["strength"] * 2 + dice_roll()
        print(f"{boss['name']} enters RAGE ATTACK! Deals {damage} damage!")
        player_stats["health"] -= damage
    elif ability == "Bow Volley":
        damage = boss["strength"] + dice_roll()
        print(f"{boss['name']} fires a BOW VOLLEY! Deals {damage} damage!")
        player_stats["health"] -= damage
    elif ability == "Stun Slam":
        print(f"{boss['name']} performs STUN SLAM! You may lose next turn!")
        return "stun"
    elif ability == "Cannon Blast":
        damage = boss["strength"] + dice_roll()
        print(f"{boss['name']} uses CANNON BLAST! Deals {damage} damage!")
        player_stats["health"] -= damage
    elif ability == "Battering Ram":
        damage = boss["strength"] + dice_roll()
        print(f"{boss['name']} charges with BATTERING RAM! Deals {damage} damage!")
        player_stats["health"] -= damage
    elif ability == "Trap":
        print(f"{boss['name']} sets a TRAP! Next attack may fail!")
    return None

# -------------------------
# --- COMBAT SYSTEM ---
# -------------------------

def combat(player_race, player_stats, inventory, enemy_race, level, is_boss=False):
    if is_boss:
        enemy = bosses[enemy_race].copy()
        enemy_name = enemy["name"]
        print(f"\nBOSS FIGHT: {enemy_name}!\n")
    else:
        enemy = races[enemy_race].copy()
        enemy_name = enemy_race
    
    time.sleep(1)
    stun_player = False
    
    while player_stats["health"] > 0 and enemy["health"] > 0:
        print(f"Your Health: {player_stats['health']} | Enemy Health: {enemy['health']}")
        print("Actions: 1. Attack 2. Defend 3. Magic 4. Item")
        
        if not stun_player:
            choice = int(input("Choose your action: "))
            action = actions[choice-1]
        else:
            print("You are stunned and lose this turn!")
            stun_player = False
            action = None
        
        # Player action
        if action == "attack":
            damage = calculate_damage(player_stats, "attack")
            enemy["health"] -= damage
            print(f"You attack and deal {damage} damage!")
        elif action == "magic":
            damage = calculate_damage(player_stats, "magic")
            enemy["health"] -= damage
            print(f"You cast magic and deal {damage} damage!")
        elif action == "defend":
            player_stats["health"] += 5
            print("You defend and gain temporary health!")
        elif action == "item":
            use_item(player_stats, inventory)
        
        time.sleep(1)
        
        # Enemy turn
        if enemy["health"] > 0:
            if is_boss:
                result = boss_action(enemy, player_stats)
                if result == "stun":
                    stun_player = True
            else:
                enemy_action = random.choice(actions[:3])
                
                if enemy_race == "Darkmon" and darkmon_emotion():
                    print("The Darkmon is emotional and loses its turn!")
                    continue
                
                damage = calculate_damage(enemy, enemy_action)
                
                if enemy_action == "attack":
                    print(f"{enemy_name} attacks and deals {damage} damage!")
                    player_stats["health"] -= damage
                elif enemy_action == "magic":
                    print(f"{enemy_name} casts magic and deals {damage} damage!")
                    player_stats["health"] -= damage
                elif enemy_action == "defend":
                    print(f"{enemy_name} defends this turn.")
        
        time.sleep(1)
    
    if player_stats["health"] <= 0:
        print("You have been defeated! Game Over.")
        return False
    else:
        print(f"You defeated the {enemy_name}!\n")
        if is_boss:
            reward = random.choice(["Health Potion", "Strength Boost", "Magic Boost"])
            print(f"You obtained {reward}!")
            inventory.append(reward)
        return True

# -------------------------
# --- MAIN GAME LOOP ---
# -------------------------

def main_game():
    player_race, player_stats, inventory = create_player()
    
    for nation, enemy_race in nations.items():
        if enemy_race == player_race:
            continue  # skip own nation
        
        # Levels 1-19
        for level in range(1, 20):
            print(f"\n--- {nation} Level {level} ---")
            success = combat(player_race, player_stats, inventory, enemy_race, level)
            if not success:
                return
            player_stats["health"] += 10
            player_stats["strength"] += 2
            player_stats["magic"] += 2
        
        # Level 20: Boss Fight
        print(f"\n--- {nation} Level 20: BOSS FIGHT! ---")
        success = combat(player_race, player_stats, inventory, enemy_race, 20, is_boss=True)
        if not success:
            return
        
        print(f"\nYou conquered {nation}!\n")
    
    print(f"\n--- Congratulations! You, a {player_race}, conquered all opposing nations! ---\n")
    if player_race == "Fleshen":
        print("Fleshens now rule the world with machinery and strategy.")
    elif player_race == "Osseins":
        print("Osseins' mastery of armor dominates the lands.")
    elif player_race == "Darkmon":
        print("Darkmons become the strongest and eventually peaceful rulers.")
    elif player_race == "Bloodlings":
        print("Bloodlings spread magical influence across the world.")

# -------------------------
# --- RUN GAME ---
# -------------------------

if __name__ == "__main__":
    main_game()

