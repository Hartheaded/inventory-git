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

        with open("logs/inventory.log", 'r+')as infile:
            data = infile.readlines()
            count = -1
            for i in data:
                count += 1
                if (cable and length) in i:
                    infile.close()
                    infile = open("logs/inventory.log", 'w')
                    data[count] = f"{cable},{length},{change + int(i.split(',')[2][:-1])}\n"
                    infile.writelines(data)






        if change >= 0:
            posneg = "added"
        else:
            posneg = "took"


        content = self.history.read()
        self.history.seek(0, 0)
        self.history.write((f"[{datetime.datetime.now()}]: {user} {posneg} {abs(change)} {length}' {cable} cable").rstrip('\r\n') + '\n' + content)




