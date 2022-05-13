class ScriptReader() :
    def __init__(self, script_path):

        #Read script file and avoid comments
        with open(script_path) as f:
            lines_raw = f.readlines()
            #Clean list
            lines = []
            for line in lines_raw :

                if line[0:2] != "//" :
                    lines.append(line[0:-1])
        position_line = 0
        #Get first line infos (values)
        first_line_val = [x.split("=") for x in lines[position_line].split(",")]
        for val in first_line_val :
            if val[0] == "edit_type" :
                self.type_of_edit = int(val[1])
            if val[0] == "fps" :
                self.fps = int(val[1])

        #Skip to next part
        position_line = self.__skip_next_part(position_line,lines)

        #Get Actors :
        self.persos = []
        while lines[position_line][0] != "-" and lines[position_line][0] != " ":
            perso_temp = []
            #Get path to perso folder
            perso_line = lines[position_line].split(" ")
            perso_temp.append(perso_line[0])
            #Add files to load
            files_names = []
            for i in range(1, len(perso_line)):
                files_names.append(perso_line[i])
            perso_temp.append(files_names)
            #Add perso to persos list
            self.persos.append(perso_temp)
            position_line+=1


        # Skip to next part
        position_line = self.__skip_next_part(position_line, lines)

        #Get Background
        self.background = lines[position_line]

        # Skip to next part
        position_line = self.__skip_next_part(position_line, lines)

        #Get music
        self.song = lines[position_line]

        # Skip to next part
        position_line = self.__skip_next_part(position_line, lines)

        self.title = lines[position_line].split(" ")
        position_line += 1
        position_line = self.__skip_next_part(position_line, lines)


        #Get comparisons :
        self.comparisons = []
        while lines[position_line][0] != " " and lines[position_line][0] != "-" :
            self.comparisons.append(lines[position_line].split(" "))
            position_line+=1

    def __skip_next_part(self, position_line, lines):
        while lines[position_line][0] != "-" :
            position_line+=1
        return position_line+1
