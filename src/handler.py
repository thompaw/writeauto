class fileToData:
    def __init__(self, filepath):
        self.filepath = filepath

    def get_sites(self):
        list_o_links = []
        # function needs to:
        # 1. read the file and get a list of all of the links listed
        with open(self.filepath, 'r') as f:
            lines = f.readlines()
            for line in lines:
                line = line.replace("\n","")  # remove newline escape
                list_o_links.append(line)
        # 2. return a list of links to be used in get_data function
        return list_o_links