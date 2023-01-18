from evennia import CmdSet
from commands.command import Command
from world import combat_system

class CmdAttack(Command):
    key = "attack"
    aliases = ["a","kill","k","murder","maim","m","hurt","h"]

    def parse(self):
        self.target = self.args

    def func(self):
        caller = self.caller
        target = self.target

        if not target:
            caller.msg("What are you attacking?")
            return
        
        target = caller.search(self.target)
        if not target:
            return
        
        string = combat_system.attack(caller, target)

        caller.location.msg_contents(string)

class ColonyCmdSet(CmdSet):
    def at_cmdset_creation(self):
        self.add(CmdAttack)