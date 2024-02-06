import datetime
class LogFunctions():

    def __init__(self):
        self.search = ''
        self.entries = []
        self.inventory = []
        self.history = open('logs/history.log', 'r+')

        with open("logs/inventory.log", 'r') as data:
            for line in data:
                self.inventory.append(line.strip().split(','))
            data.close()


    def newEntry(self):
        pass

    def modEntry(self,cable,length,change,user):
        x = ''
        with open("logs/history.log", 'a+') as file:
            for entry in file:
                if cable in entry[0] and length in entry[1]:
                    x = int(entry[2]) + change

        with open("logs/inventory.log", 'a+') as file:
            for line in file:
                if f'{cable},{length},' in line:
                    pass





        if change >= 0:
            posneg = "added"
        else:
            posneg = "took"


        content = self.history.read()
        self.history.seek(0, 0)
        self.history.write((f"[{datetime.datetime.now()}]: {user} {posneg} {abs(change)} {length}' {cable} cable").rstrip('\r\n') + '\n' + content)




