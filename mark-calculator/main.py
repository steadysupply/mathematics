import pprint
import pyquery
import re
import requests

fmt = 'http://www.bbk.ac.uk/study/modules/{0}/{1}'
regexp = re.compile(r'(Level..)')

class Course(object):
    __slots__ = ('code', 'level', 'mark', 'name')
    def __init__(self, code, mark):
        self.code = code
        self.mark = mark
        response = requests.get(fmt.format(code[:4].lower(), code))
        content = pyquery.PyQuery(response.content)('#content')
        self.name = content[0][1].text_content()
        text = content[0][2][0][0].text_content()
        self.level = int(re.search(regexp, text).group(0)[-1])

    def __repr__(self):
        desc = [
            "{0}: {1}".format(name, getattr(self, name))
            for name in self.__slots__
        ]
        return "<Course {0}>".format(', '.join(desc))

weighting = {
    4: 0,
    5: 1,
    6: 2,
}

code_mark = (
    ('EMMS097S4', 69),
    ('EMMS096S4', 56),
    ('EMMS095S5', 63),
    ('BUEM001S5', 43),
    ('BUEM002S5', 58),
    ('EMMS098S5', 60),
    ('EMMS094S6', None),
    ('BUEM021S6', None),
    ('BUEM022S6', None),
)

courses = [Course(code, mark) for code, mark in code_mark]

pprint.pprint(courses)
