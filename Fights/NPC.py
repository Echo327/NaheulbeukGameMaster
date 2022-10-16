import random

def throw_dice100():
    return random.randint(1,100)

def throw_dice20():
    return random.randint(1,20)

def throw_dice6():
    return random.randint(1,6)

def throw_dice4():
    return random.randint(1,4)

class enemy:
    """
    Naheulbeuk is in French, so a translation to English is included in documentation, just in case.
    
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
        
        self.state = "ALIVE"; # Alive by default
        
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
        elif self.EV <= 3:
            self.state = "FAINTED";
        elif self.EV < 6 and self.state=="ALIVE":
            dice = throw_dice20();
            if dice < 4: # 15% chance
                self.state = "PANIC";
            elif dice > 17: # 15% chance
                self.state = "RUNNING";
        return None
    
    def save_fight(self):
        """
        To save current state of fight to file (in case restart is needed).
        """
        pass
    
    def next_phase(self):
        self.update_state()
        self.get_state()
        self.save_fight()
        return None
    
    def take_damage(self, DMG):
        """
        PRD is not taken into account here as critical attacks ignore armour.
        """
        self.EV -= DMG
        print(self.NAME, "a pris", DMG, "en dégats.")     # NAME took DMG damage.
        return None
    
    def gain_health(self, HEAL):
        self.EV += HEAL
        print(self.NAME, "a récupéré", HEAL, "en EV.")    # NAME healed HEAL health.
        return None
    
    def critical_attack(self):
        pass
    
    def critical_block(self):
        pass
    
    def attack(self):
        if self.state == "ALIVE":
            # Attack
            dice20 = throw_dice20();
            if dice20 <= self.AT:
                dice6 = [throw_dice6() for i in range(self.DMG_DICE_N)];
                DAMAGE = sum(dice6) + self.DMG_BONUS;
                print(self.NAME, "fait", DAMAGE, "de dégâts en EV à son ennemi.") # NAME does DAMAGE damage to their enemy.
            else:
                print(self.NAME, "rate son attaque.") # NAME misses their attack.

        self.next_phase()
        return None
    
    def countered(self,hit):
        if hit == None:
            return None
        if self.state == "ALIVE":
            dice20 = throw_dice20();
            if dice20 <= self.PRD:
                print(self.NAME, "arrive à parer l'attaque!") # NAME manages to block the attack.
            else:
                print(self.NAME,"n'arrives pas à parer. Dégats à calculer.") # NAME does not manage to block. Damage calculation is needed.

        #self.next_phase()
        return None
    
    def defend(self, hit):
        if hit == None:
            return None
        if self.state == "ALIVE":
            dice20 = throw_dice20();
            if dice20 <= self.PRD:
                print(self.NAME,"arrive à parer l'attaque!")
                print(self.NAME,"contre-attaque.")
                self.attack()
            else:
                actual_damage = hit - self.PR;
                if actual_damage > 0:
                    self.take_damage(actual_damage)
                else:
                    print(self.NAME,"ne prends pas de dégats.") # NAME does not take any damage.
        
        self.next_phase()
        return None
