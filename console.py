#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models.user import User
import shlex
"""console.py model"""


class HBNBCommand(cmd.Cmd):
    """Airbnb_clone program entry point"""
    models = {
                "BaseModel":    BaseModel(),
                "User":         User(),
                }
    classes = {"BaseModel", "User"}

    prompt = "(hbnb) "

    def do_create(self, line):
        """
        Function: create an instance of a class
        Use: create <classname>

        """
        if len(line) == 0:
            print("** class name missing **")
            return
        if line in self.classes:
            model = self.models[line]
            print(model.id)
            """
            other codes come here
            """
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """
        Function: prints the string representation of an
        instance based on class name and id.
        Use: show <classname.id>

        """
        tokens = shlex.split(line)
        if len(tokens) == 0:
            print("** class name missing **")
        elif tokens[0] in self.classes:
            if len(tokens) == 1:
                print("** instance id missing **")
            else:
                model = self.models[tokens[0]]
                """
                other code goes here
                """
        else:
            print("** class doesn't exist **")

    def do_all(self, line):
        """
        Function: prints all string representation of all instance
        based on class or all instance when used alone
        Use: all <classname>
             all

        """
        pass

    def do_update(self, line):
        """
        Function: Update an instance based on the class name and id
        by adding or updating attribute and then save the change
        to JSON file.
        Use: update <classname> <id> <attribute_name> <attribute_value>

        """
        tokens = shlex.split(line)
        if len(tokens) == 0:
            print("** class name missing **")
        elif tokens[0] in self.classes:
            if len(tokens) == 1:
                print("** instance id missing **")
            elif len(tokens) == 2:
                print("** attribute name missing **")
            elif len(tokens) == 3:
                print("** value missing **")
            else:
                model = self.models[tokens[0]]
                query = tokens[0] + "." + tokens[1]
        else:
            print("** class doesn't exist **")

    def do_destroy(self, line):
        """
        Function: destroy an instance base on class name and id
        and the save the changes to a JSON file
        Use: destroy <classname.id>

        """
        tokens = shlex.split(line)
        if len(tokens) == 0:
            print("** class name missing **")
        elif tokens[0] in self.classes:
            if len(tokens) == 1:
                print("** instance id missing **")
            else:
                model = self.models[tokens[0]]
                query = tokens[0] + "." + tokens[1]
                """
                other code goes here
                """
        else:
            print("** class doesn't exist **")

    def do_quit(self, line):
        """
        ommand

        """

        return True

    def do_EOF(self, line):
        """handling end of file imterrupt"""

        return True

    def emptyline(self):
        """updating default emptyline method"""

        HBNBCommand.prompt


if __name__ == "__main__":
    HBNBCommand().cmdloop()
