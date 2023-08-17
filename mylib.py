"""
solution HW7.1.py: creates Class Config
Author: Katelyn Pease
Date: 8-17-23
"""
import csv
class Config:
    """class for producing config instances. These config instances
    construct an object that can read and write configuration values
    (ke/value pairs) from/to a file """

    def __init__(self, filename):
        """constructor. Takes in a file that has key/value pairs
        that we can read and write o"""
        self.filename = filename
        x = filename.split(".")
        if len(x) < 2:
            raise ValueError(f'not enough values to unpack')
        self.format = x[-1]
        self.params = self.read_csv_file()

    def read_csv_file(self):
        """reads in the file and
        stores it as a dictionary"""
        mydict = {}
        fh = open(self.filename)
        fr = csv.reader(fh)
        for line in fr:
            mydict[line[0]] = line[1]
        return mydict

    def get(self, key):
        """reads value from the
        dictionary and returns it"""
        try:
            x = self.params[key]
        except KeyError:
            raise KeyError(f'"{key}" is not in config')
        return x

    def set(self, key, value, overwrite=False):
        """add key value pairs to the dictionary
        and write to the file"""
        if key in self.params.keys() and overwrite is False:
            raise KeyError(f'key "{key}" is already in config!')
        self.params[key] = value
        self.write_csv_file()

    def write_csv_file(self):
        """opens the file for writing and
        writes to it using the dictionary"""
        wfh = open(self.filename, 'w')
        dwriter = csv.writer(wfh)
        for item in self.params:
            dwriter.writerow([item] + [self.params[item]])
        wfh.close()

    def __str__(self):
        """returns a string that indicates
        how the file was constructed"""
        x = f"Config {str(self.filename)}"
        return x

























