import sys
import csv

csvfile_path = "/Users/NightBaron/Desktop/py/find-emails-test/user_emails.csv"


def populate_dictionary(filename):
    """Populate a dictionary with name/number pairs for easy lookup."""
    phonedict = {}
    with open(filename) as csvfile:
        lines = csv.reader(csvfile, delimiter=',')
        for row in lines:
            name = row[0].lower()
            phonedict[name] = row[2]
    return phonedict


def find_phone_number(argv):

    try:
        fullname = argv[1] + " " + argv[2]
        phonedict = populate_dictionary(csvfile_path)
        if phonedict.get(fullname.lower()):
            return phonedict.get(fullname.lower())
        else:
            return "No phone number found"
    except IndexError:
        return "Missing parameters"


def main():
    print(find_phone_number(sys.argv))


if __name__ == "__main__":
    main()
