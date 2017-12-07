import pprint
import pyquery
import re
import redis
import requests

fmt = 'http://www.bbk.ac.uk/study/modules/{0}/{1}'
regexp = re.compile(r'(Level..)')

response_cache = redis.StrictRedis('redis', db=0)


def cache(code):
    response_body = response_cache.get(code)
    if response_body is None:
        response = requests.get(fmt.format(code[:4].lower(), code))
        response_body = response.content
        response_cache.set(code, response_body)
    content = pyquery.PyQuery(response_body)('#content')
    name = content[0][1].text_content()
    text = content[0][2][0][0].text_content()
    level = int(re.search(regexp, text).group(0)[-1])
    return name, level


class Module(object):
    __slots__ = ('code', 'level', 'mark', 'name')

    def __init__(self, code, mark):
        self.code = code
        self.mark = mark
        self.name, self.level = cache(code)

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
    ('BUEM008S6', None),
    ('BUEM009S6', None),
    ('BUEM003S6', None),
)

modules = [Module(code, mark) for code, mark in code_mark]
marked_modules = tuple(filter(lambda module: module.mark is not None, modules))

pprint.pprint(modules)


def weighted_average(level_mark):
    numerator = 0
    denominator = 0

    for level, mark in level_mark:
        weight = weighting[level]
        numerator = numerator + (mark * weight)
        denominator = denominator + weight

    return numerator / denominator


for prospective_mark in range(70, 80):
    level_mark = []
    for module in modules:
        if module.mark is None:
            mark = prospective_mark
        else:
            mark = module.mark
        level_mark.append((module.level, mark))
    final = weighted_average(level_mark)
    print("With average {0}, final {1}".format(mark, final))
    if final > 70:
        print("Average mark required: {0}".format(mark))
        break
