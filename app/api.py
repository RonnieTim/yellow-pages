from flask import request
from flask_restful import Resource


class PhoneNumbers(Resource):
    """Manages phone number pages api."""

    DATA_FILE = "data/contacts_list.txt"

    def get(self):
        phone_numbers = dict()
        contacts_list = open(self.DATA_FILE, "r")

        for line in contacts_list:
            if ":" in line:
                key = line.split(":")[0]
                value = line.split(":")[1]
                value = value.strip(" ").rstrip("\n\r")
                phone_numbers.update({key: value})

        return phone_numbers

    def post(self):
        json_data = request.json
        name = json_data["name"]
        number = json_data["number"]
        self.add_file(name, number)

        return {"success": True}, 201

    def put(self):
        json_data = request.json
        name = json_data["name"]
        number = json_data["number"]
        self.del_file(name)
        self.add_file(name, number, start_sep="", end_sep="\n")

        return {"success": True}, 200

    def delete(self):
        json_data = request.json
        name = json_data["name"]
        self.del_file(name)

        return {"success": True}, 200

    def add_file(self, name, number, start_sep="\n", end_sep=""):
        contacts_list = open(self.DATA_FILE, "a")
        data = start_sep + "{name}: {number}".format(
            name=name,
            number=number,
        )
        data += end_sep

        contacts_list.write(data)

    def del_file(self, name):
        with open(self.DATA_FILE, "r") as f:
            lines = f.readlines()
        with open(self.DATA_FILE, "w") as f:
            for line in lines:
                if name != line.split(":")[0]:
                    print("line: {}".format(line))
                    f.write(line)
