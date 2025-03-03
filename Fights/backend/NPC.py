import random     # For dice throws
import json       # For criticals

import os
current_dir = os.path.dirname(__file__)
resources_path = os.path.join(current_dir, "resources/")

# Dices
def throw_dice100():
    return random.randint(1,100)

def throw_dice20():
    return random.randint(1,20)

def throw_dice10():
    return random.randint(1,10)

def throw_dice6():
    return random.randint(1,6)

def throw_dice4():
    return random.randint(1,4)

# Read critical hits json
crit_tables = [
    "critical_hits_bladed",
    "critical_hits_blunt",
    "critical_hits_projectile",
    "critical_hits_hand2hand",
    "critical_hits_block",
    "clumsy_hits_standard",
    "clumsy_hits_spells",
    "clumsy_hits_projectile",
    "clumsy_hits_hand2hand"
]
myCrits = vars()
for table in crit_tables:
    with open(resources_path+table+'.json', 'r') as openfile:
        myCrits[table] = json.load(openfile)

class enemy:
    """
    Naheulbeuk is in French, so a translation to English is included in documentation/comments.
    
    NAME: Nom (Name), str
    AT : Attaque (Attack Score), unsigned int
    PRD: Parade (Block Score), unsigned int
    EV: Energie Vitale (Health Points, HP), int
    PR: Protection (Armour), int
    WEAPON: Arme (Weapon), str
    DMG_DICE_N: Number of dices thrown for damage calculation
    DMG_BONUS: Bonus to damage calculation (can be negative), int
    COU: Courage (Courage score), unsigned int
    EXP: Experience Points gained if enemy is defeated
    """
    
    def __init__(self,NAME,AT,PRD,EV,PR,WEAPON,DMG_DICE_N,DMG_BONUS,COU,EXP):
        self.NAME = NAME;
        self.AT = AT;
        self.PRD = PRD;
        self.EV = EV;
        self.PR = PR;
        self.WEAPON = WEAPON;
        self.DMG_DICE_N = DMG_DICE_N;
        self.DMG_BONUS = DMG_BONUS;
        self.COU = COU;
        self.EXP = EXP;
        
        self.state = "ALIVE"; # Alive by default #! State should be saved
        self.filename = "../saved-state/save_file/saved_state_" + str(self.NAME)
        
    def info(self):
        information = str(self.NAME) + " a "                                # NAME has
        information += str(self.AT) + " en attaque, "                       # AT in attack,
        information += str(self.PRD) + " en parade, "                       # PRD in blocking score,
        information += str(self.EV) + " en EV, "                            # EV in HP,
        information += "et une protection de " +str(self.PR) + ".\n"        # an armour of PR
        
        information += "Armé de " + str(self.WEAPON) + ", "                 # armed with WEAPON
        information += "qui fait des dégâts "                               # Their weapon does damage
        information += str(self.DMG_DICE_N) + "D6+" + str(self.DMG_BONUS)   # (DICE_N)D6+(BONUS)
        information += ".\n"
        information += "Ils ont un courage de " + str(self.COU) + ".\n"     # They have a courage of COURAGE.
        information += "Ils donnent " + str(self.EXP) + " XP en mourant."   # They give EXP EXP upon death.
        
        return information
    
    def get_state(self):
        if self.state == "ALIVE":
            print(self.NAME + " est en vie avec " + str(self.EV) + " EV.")
        elif self.state == "DEAD":
            print(self.NAME + " est mort.")
        elif self.state == "FAINTED":
            print(self.NAME + " est evanoui avec " + str(self.EV) + " EV.")
        elif self.state == "PANIC":
            print(self.NAME + " panique avec " + str(self.EV) + " EV.")
        elif self.state == "RUNNING":
            print(self.NAME + " est en train de s'enfuire avec " + str(self.EV) + " EV.")
        elif self.state == "FLED":
            print(self.NAME + " s'est enfuit.")
        return None
    
    def update_state(self):
        if self.state == "RUNNING" and self.EV > 0:
            self.state = "FLED";
        elif self.EV <= 0:
            self.state = "DEAD";
            self.EV = 0;
        elif self.EV <= 3:
            self.state = "FAINTED";
        elif self.EV < 6 and self.state=="ALIVE":
            dice = throw_dice20();
            if dice < 4: # 15% chance
                self.state = "PANIC";
            elif dice > 17 and self.COU < 19: # 15% chance, Enemies with high COURAGE stat do not run away
                self.state = "RUNNING";
        return None
    
    def save_state(self):
        """
        To save current state of fight to file (in case restart is needed).
        """
        with open(self.filename, 'w') as file:
            current_state = str(self.NAME) + " " + \
                            str(self.AT) + " " + \
                            str(self.PRD) + " " + \
                            str(self.EV) + " " + \
                            str(self.PR) + " " + \
                            str(self.WEAPON) + " " + \
                            str(self.DMG_DICE_N) + " " + \
                            str(self.DMG_BONUS) + " " + \
                            str(self.COU) + " " + \
                            str(self.EXP)
            file.write(current_state)
        return None
    
    def next_phase(self):
        self.update_state()
        self.get_state()
        self.save_state()
        return None
    
    def take_damage(self, DMG):
        """
        PRD is not taken into account here as critical attacks ignore armour.
        """
        self.EV -= DMG
        print(self.NAME, "a pris", DMG, "en dégats.")     # NAME took DMG damage.
        return None
    
    def gain_health(self, HEAL):
        # TO-DO: Is capped heal to max health needed?
        if self.state != "DEAD":
            self.EV += HEAL
            print(self.NAME, "a récupéré", HEAL, "en EV.")    # NAME healed HEAL health.
        self.next_phase()
        return None
    
    def critical_attack(self):
        # Attaque critique
        dice20 = throw_dice20();
        print("Attaque Critique:")
        print("Blade:", critical_hits_bladed[str(dice20)])
        print("Blunt:", critical_hits_blunt[str(dice20)])
        print("Hand_to_Hand:", critical_hits_hand2hand[str(dice20)])
        print("Projectile:", critical_hits_projectile[str(dice20)])
        # For choices
        dice4 = throw_dice4();
        dice6 = throw_dice6();
        dice10 = throw_dice10();
        dice20 = throw_dice20();
        print("Dice 4:",dice4,"Dice 6:",dice6,"Dice 10:",dice10,"Dice 20:",dice20,"\n")
    
    def attack_mishap(self):
        # Maladresse attaque
        dice20 = throw_dice20();
        print("Maladresse Attaque:")
        print("Standard:", clumsy_hits_standard[str(dice20)])
        print("Spells:", clumsy_hits_spells[str(dice20)])
        print("Hand_to_Hand:", clumsy_hits_hand2hand[str(dice20)])
        print("Projectile:", critical_hits_projectile[str(dice20)])
        # For choices
        dice4 = throw_dice4();
        dice6 = throw_dice6();
        dice10 = throw_dice10();
        dice20 = throw_dice20();
        print("Dice 4:",dice4,"Dice 6:",dice6,"Dice 10:",dice10,"Dice 20:",dice20,"\n")
    
    def critical_block(self):
        # Parade critique
        dice20 = throw_dice20();
        print("Parade Critique:")
        print("Parade:", critical_hits_block[str(dice20)])
        # For choices
        dice4 = throw_dice4();
        dice6 = throw_dice6();
        dice10 = throw_dice10();
        dice20 = throw_dice20();
        print("Dice 4:",dice4,"Dice 6:",dice6,"Dice 10:",dice10,"Dice 20:",dice20,"\n")
    
    def block_mishap(self):
        # Maladresse parade
        dice20 = throw_dice20();
        print("Maladresse Parade:")
        print("Standard:", clumsy_hits_standard[str(dice20)])
        print("Hand_to_Hand:", clumsy_hits_hand2hand[str(dice20)])
        # For choices
        dice4 = throw_dice4();
        dice6 = throw_dice6();
        dice10 = throw_dice10();
        dice20 = throw_dice20();
        print("Dice 4:",dice4,"Dice 6:",dice6,"Dice 10:",dice10,"Dice 20:",dice20,"\n")
    
    def attack(self):
        if self.state == "ALIVE":
            # Attack
            dice20 = throw_dice20();
            #dice20=1; # debug, critical
            #dice20=20; # debug, maladresse
            if dice20 == 1:
                print(self.NAME,": Attaque Critique!")
                self.critical_attack()
                return None
            if dice20 == 20:
                print(self.NAME,": Maladresse Attaque!")
                self.attack_mishap()
                return None
            if dice20 <= self.AT:
                dice6 = [throw_dice6() for i in range(self.DMG_DICE_N)];
                DAMAGE = sum(dice6) + self.DMG_BONUS;
                print(self.NAME, "fait", DAMAGE, "de dégâts en EV à son ennemi.") # NAME does DAMAGE damage to their enemy.
            else:
                print(self.NAME, "rate son attaque.") # NAME misses their attack.
        return None
    
    def counter(self):
        if self.state == "ALIVE":
            dice20 = throw_dice20();
            if dice20 <= self.PRD:
                print(self.NAME, "arrive à parer l'attaque!") # NAME manages to block the attack.
            else:
                print(self.NAME,"n'arrives pas à parer. Dégats à calculer.") # NAME does not manage to block. Damage calculation is needed.
        return None
    
    def defend(self, hit):
        if hit == None or hit == 0:
            return None
        if self.state == "ALIVE":
            dice20 = throw_dice20();
            #dice20=1; # debug, critical
            #dice20=20; # debug, maladresse
            if dice20 == 1:
                print(self.NAME,": Parade Critique!")
                self.critical_block()
                return None
            if dice20 == 20:
                print(self.NAME,": Maladresse Parade!")
                self.block_mishap()
                return None
            if dice20 <= self.PRD:
                print(self.NAME,"arrive à parer l'attaque!")
                print(self.NAME,"contre-attaque.")
                self.attack()
            else:
                print(self.NAME,"n'arrives pas à parer l'attaque...")
                actual_damage = hit - self.PR;
                if actual_damage > 0:
                    self.take_damage(actual_damage)
                else:
                    print(self.NAME,"ne prends pas de dégats.") # NAME does not take any damage.
        
        self.next_phase()
        return None
