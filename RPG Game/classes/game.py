import random


class bcolors:  # this class shows us the code for colors
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Person:
    def __init__(self, name, hp, mp, atk, df, magic, items):
        self.name = name
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.items = items
        self.action = ["Attack", "Magic", "Items"]

    def generat_damage(self) -> int:
        return random.randrange(self.atkl, self.atkh)

    def take_damage(self, dmg) -> int:
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def heal(self, dmg) -> int:
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp
        return self.hp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

    def choose_action(self):
        i = 1
        print("\n" + "    " + bcolors.BOLD + self.name + bcolors.ENDC)
        print(bcolors.OKBLUE + bcolors.BOLD + "    ACTION" + bcolors.ENDC)
        for item in self.action:
            print("         " + str(i) + ".", item)
            i += 1

    def choose_magic(self):
        i = 1
        print("\n" + bcolors.OKBLUE + bcolors.BOLD + "    MAGIC" + bcolors.ENDC)
        for spell in self.magic:
            print("         " + str(i) + ".", spell.name, "(cost:", str(spell.cost) + ")")
            i += 1

    def choose_item(self):
        i = 1
        print("\n" + bcolors.OKGREEN + bcolors.BOLD + "    ITEM" + bcolors.ENDC)
        for item in self.items:
            print("         " + str(i) + ".", item["item"].name, ":", item["item"].description, "(x" + str(item["quantity"])+ ")")
            i += 1

    def choose_target(self, enemies):
        i = 1

        print("\n" + bcolors.FAIL + bcolors.BOLD + "    TERGET" + bcolors.ENDC)
        for enemy in enemies:
            if enemy.get_hp() != 0:
                print("         " + str(i) + ".", enemy.name)
                i += 1
        choice= int(input("    Choose target: ")) - 1
        return  choice




    def get_enemy_stats(self):
        hp_bar = ""
        tick_bar = (self.hp / self.maxhp) * 100 / 2

        while tick_bar > 0:
            hp_bar += "█"
            tick_bar -= 1

        while len(hp_bar) < 50:
            hp_bar += " "

        hp_string = str(self.hp) + "/" + str(self.maxhp)
        current_hp = ""

        if len(hp_string) < 11:
            decrease = 11 - len(hp_string)

            while decrease > 0:
                current_hp += " "
                decrease -= 1
            current_hp += hp_string
        else:
            current_hp = hp_string



        print("                                 __________________________________________________")
        print(bcolors.BOLD + self.name + "          " +
              current_hp + "    |" + bcolors.FAIL + hp_bar + bcolors.ENDC + bcolors.BOLD + "|")

    def get_stats(self):

        hp_bar = ""
        tick_bar = (self.hp/self.maxhp) * 100 / 4

        mp_bar = ""
        mp_tick = (self.mp / self.maxmp) * 100 / 10

        while tick_bar > 0:
            hp_bar += "█"
            tick_bar -= 1

        while len(hp_bar) < 25:
            hp_bar += " "


        while mp_tick > 0:
            mp_bar += "█"
            mp_tick -= 1

        while len(mp_bar) < 10:
            mp_bar += " "

        hp_string = str(self.hp) + "/" + str(self.maxhp)
        current_hp = ""

        if len(hp_string) < 9:
            decrease = 9 - len(hp_string)

            while decrease > 0:
                current_hp += " "
                decrease -= 1
            current_hp += hp_string
        else:
            current_hp = hp_string


        mp_string = str(self.mp) + "/" + str(self.maxmp)
        current_mp = ""

        if len(mp_string) < 7:
            decrease_mp = 7 - len(mp_string)

            while decrease_mp > 0:
                current_mp += " "
                decrease_mp -= 1

            current_mp += mp_string
        else:
            current_mp = mp_string

        print("                                 _________________________             __________")
        print(bcolors.BOLD + self.name + "          " +
              current_hp + "      |" + bcolors.OKGREEN + hp_bar + bcolors.ENDC + bcolors.BOLD + "|   " +
              current_mp + " |" + bcolors.OKBLUE + mp_bar + bcolors.ENDC + "|")

    def choose_enemy_spell(self):
        magic_choice = random.randrange(0, len(self.magic))
        spell = self.magic[magic_choice]
        magic_dmg = spell.generate_damage()

        pct = self.get_hp() / self.maxhp * 100

        if self.mp < spell.cost or spell.type == "white" and pct > 50:
            return self.choose_enemy_spell()
        else:
            return spell, magic_dmg