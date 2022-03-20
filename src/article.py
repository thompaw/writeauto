class Article:
    def __init__(self, title, number, author, date, link, reportedTo, severity, content):
        self.title = title
        self.number = number
        self.author = author
        self.date = date
        self.link = link
        self.reportedTo = reportedTo
        self.severity = severity
        self.content = content

    def makeDoc(self):
        pass