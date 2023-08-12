
"""
    A score contains all of the information necessary to create a piece of sheet music.
    By default, the Staff is empty.
"""

from xml.dom import minidom # use minidom to create an xml file
from staff import Staff, Voice

class VBox:
    def __init__(self, title, composer, subtitle=None, lyricist=None, height=20):
        # for now, these attributes are public
        self.title = title
        self.subtitle = subtitle
        self.composer = composer
        self.lyricist = lyricist
        self.height = height

class Score:
    def __init__(self, vbox: VBox=None, staff: Staff=None) -> None:
        self.vbox = vbox
        self.staff = staff

    def add_staff(self, staff: Staff) -> None:
        if self.staff != None:
            print("WARNING: Attempting to add a staff to a score that already has a staff")
        else:
            self.staff = staff
    
    def create_xml(self) -> minidom.Document:
        doc = minidom.Document()
        # ----- create xml doc here -----
        return doc
    

# driver code
my_score = Score(
    VBox(
        "Cool title here",
        "Andrew",
        height=50
    )
)
