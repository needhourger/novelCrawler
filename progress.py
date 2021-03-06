import progressbar

from crawlers.settings import DEBUG

class Progress:
    __widths = [
        (126, 1),
        (159, 0),
        (687, 1),
        (710, 0),
        (711, 1),
        (727, 0),
        (733, 1),
        (879, 0),
        (1154, 1),
        (1161, 0),
        (4347, 1),
        (4447, 2),
        (7467, 1),
        (7521, 0),
        (8369, 1),
        (8426, 0),
        (9000, 1),
        (9002, 2),
        (11021, 1),
        (12350, 2),
        (12351, 1),
        (12438, 2),
        (12442, 0),
        (19893, 2),
        (19967, 1),
        (55203, 2),
        (63743, 1),
        (64106, 2),
        (65039, 1),
        (65059, 0),
        (65131, 2),
        (65279, 1),
        (65376, 2),
        (65500, 1),
        (65510, 2),
        (120831, 1),
        (262141, 2),
        (1114109, 1),
    ]

    # ACCESSOR FUNCTIONS
    def get_width(self,o):
        """Return the screen column width for unicode ordinal o."""
        if o == 0xe or o == 0xf:
            return 0
        for num, wid in self.__widths:
            if o <= num:
                return wid
        return 1

    def custom_len(self,value):
        total = 0
        for c in value:
            total += self.get_width(ord(c))
        return total


    def __init__(self,max_values,bname,author):
        if DEBUG:
            self.__bar = None
            return
        
        self.__bar = progressbar.ProgressBar(
            max_value=max_values, 
            widgets=[
                "<{}-{}>".format(bname,author),
                progressbar.Percentage(),
                progressbar.Bar(marker='>'),
                progressbar.Counter(format=' [Chapters:%(value)d/%(max_value)d]')
            ], 
            custom_len=self.custom_len
        )
    
    def start(self):
        if self.__bar:
            self.__bar.start()

    def update(self,value):
        if self.__bar:
            self.__bar.update(value)

    def finish(self):
        if self.__bar:
            self.__bar.finish()