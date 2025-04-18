# Week-5-Python-Assignment
Object Orientated Programming

class Superhero:
    def __init__(self, name, alias, power_level):
        self.name = name
        self.alias = alias
        self._power_level = power_level  # Encapsulated attribute

    def introduce(self):
        return f"I am {self.alias}, also known as {self.name}!"

    def get_power_level(self):
        return self._power_level

    def boost_power(self, amount):
        self._power_level += amount
        print(f"{self.alias}'s power increased to {self._power_level}!")

class Speedster(Superhero):
    def __init__(self, name, alias, power_level, top_speed):
        super().__init__(name, alias, power_level)
        self.top_speed = top_speed

    def use_power(self):
        return f"{self.alias} runs at lightning speed of {self.top_speed} km/h! ⚡"

class Telepath(Superhero):
    def __init__(self, name, alias, power_level, mind_control_range):
        super().__init__(name, alias, power_level)
        self.mind_control_range = mind_control_range

    def use_power(self):
        return f"{self.alias} can control minds within {self.mind_control_range} meters! 🧠"

flash = Speedster("Barry Allen", "The Flash", 95, 1200)
prof_x = Telepath("Charles Xavier", "Professor X", 98, 300)

print(flash.introduce())
print(flash.use_power())
flash.boost_power(5)

print(prof_x.introduce())
print(prof_x.use_power())
