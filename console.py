#!/usr/bin/python3
"""
Module Console
"""
import cmd
import shlex
import sys
import models
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """HBNB Class """
    prompt = '(hbnb) '

    classes = {
                'BaseModel': BaseModel,
                'Amenity': Amenity,
                'State': State,
                'Place': Place,
                'Review': Review,
                'User': User,
                'City': City
                            }

    def do_quit(self, args):
        """ Defines quit option"""
        return True

    def do_EOF(self, args):
        """ Defines EOF option"""
        print()
        return True

    def emptyline(self):
        """ Defines Empty option"""
        self.prompt

    def do_create(self, args):
        """Creates an instance of BaseModel"""
        if args:
            if args in self.classes:
                model = getattr(sys.modules[__name__], args)
                instance = model()
                print(instance.id)
                models.storage.save()
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")
        return

    def do_show(self, args):
        """prints string representation based on the class name and id"""
        tokens = shlex.split(args)
        if len(tokens) == 0:
            print("** class name missing **")
        else:
            if tokens[0] not in self.classes:
                print("** class doesn't exist **")
            elif len(tokens) == 1:
                print("** instance id missing **")
            else:
                instance_id = tokens[0] + "." + tokens[1]
                all_instance_dict = models.storage.all()
                if instance_id in all_instance_dict:
                    print(all_instance_dict[instance_id])
                else:
                    print("** instance does'nt exist **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""
        tokens = shlex.split(args)
        if len(tokens) == 0:
            print("** class name missing **")
        else:
            if tokens[0] not in self.classes:
                print("** class doesn't exist **")
            elif len(tokens) == 1:
                print("** instance id missing **")
            else:
                instance_id = tokens[0] + "." + tokens[1]
                all_instance_dict = models.storage.all()
                if instance_id in all_instance_dict:
                    del all_instance_dict[instance_id]
                else:
                    print("** instance does'nt exist **")

    def do_all(self, args):
        """all string representation of all instances"""
        tokens = shlex.split(args)
        instance_dict = []
        all_instance_dict = models.storage.all()
        if len(tokens) == 0:
            for key in all_instance_dict:
                str_obj = str(all_instance_dict[key])
                instance_dict.append(str_obj)
            print(instance_dict)
        else:
            if len(tokens) == 1:
                if tokens[0] not in self.classes:
                    print("** class doesn't exist **")
                else:
                    for key in all_instance_dict:
                        query = key.split(".")
                        if query[0] == tokens[0]:
                            str_obj = str(all_instance_dict[key])
                            instance_dict.append(str_obj)
                    print(instance_dict)

    def do_update(self, args):
        """Updates an instance based on the class name and id """

        tokens = shlex.split(args)
        if len(tokens) == 0:
            print("** class name missing **")
        else:

            if tokens[0] not in self.classes:
                print("** class doesn't exist **")
            elif len(tokens) == 1:
                print("** instance id missing **")
            elif len(tokens) == 2:
                print("** attribute name missing **")
            elif len(tokens) == 3:
                print("** value missing **")
            else:
                instance_id = tokens[0] + "." + tokens[1]
                if tokens[2] == "created_at" or tokens[2] == "updated_at":
                    return
                all_instances_dict = models.storage.all()
                try:
                    instance = all_instances_dict[instance_id]
                except KeyError:
                    print("** no instance found **")
                try:
                    attr_type = type(getattr(instance, tokens[2]))
                    tokens[3] = attr_type(tokens[3])
                except AttributeError:
                    pass
                setattr(instance, tokens[2], tokens[3])
                models.storage.save()

    def do_count(self, argument):
        """  retrieve the number of instances of a class """
        tokensA = shlex.split(argument)
        dic = models.storage.all()
        num_instances = 0
        if tokensA[0] not in self.classes:
            print("** class doesn't exist **")
            return
        else:
            for key in dic:
                className = key.split('.')
                if className[0] == tokensA[0]:
                    num_instances += 1
                print(num_instances)

    def precmd(self, argument):
        """ executed just before the command line line is interpreted """
        args = argument.split('.', 1)
        if len(args) == 2:
            _class = args[0]
            args = args[1].split('(', 1)
            command = args[0]
            if len(args) == 2:
                args = args[1].split(')', 1)
                if len(args) == 2:
                    _id = args[0]
                    other_arguments = args[1]
            line = command + " " + _class + " " + _id + " " + other_arguments
            return line
        else:
            return argument


if __name__ == '__main__':
    """infinite loop"""
    HBNBCommand().cmdloop()
