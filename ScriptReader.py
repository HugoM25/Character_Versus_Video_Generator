class ScriptReader() :
    def __init__(self, script_path):

        with open(script_path) as f:
            lines = f.readlines()
        #Clean list
        lines = [x.replace("\n", "") for x in lines]

        #Add infos to
        self.typeOfEdit = int(lines[0])

        if self.typeOfEdit == 1 :

            self.perso1 = lines[1].split(" ")[0]
            self.perso2 = lines[1].split(" ")[2]
            self.song = lines[2]

            self.comparisons = []
            for i in range(3, len(lines)):
                self.comparisons.append(lines[i].split(" "))

        elif self.typeOfEdit == 2 :
            self.perso1 = lines[1].split(" ")[0]
            self.perso2 = lines[1].split(" ")[2].split(",")
            self.song = lines[2]
            self.background = lines[3]
            self.comparisons = []
            for i in range(4, len(lines)) :
                self.comparisons.append(lines[i].split(" "))

        else :
            print("[ERROR] NO TYPE OF EDIT CHOSEN")