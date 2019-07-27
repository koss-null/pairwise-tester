class Candidate:
    def __init__(self, label, properties):
        self.label = label
        if type(properties == list) and len(properties) != 0:
            self.properties = properties
        else:
            self.properties = [0]
