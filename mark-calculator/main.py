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
    name = content('.page-title')[0].text_content()
    text = content('#content')[0][2][1][0][0].text_content()
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

    def __gt__(self, other):
        if self.mark is None:
            return False
        if other.mark is None:
            return False
        return self.mark > other.mark


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
    ('EMMS094S6', 71),
    ('BUEM021S6', 75),
    ('BUEM022S6', 54),
    ('BUEM008S6', None),
    ('BUEM009S6', None),
    ('EMMS093S6', None),
)

modules = [Module(code, mark) for code, mark in code_mark]
# pop weakest non-zero-weighted result
modules.pop(modules.index(min(mod for mod in modules if mod.level > 4)))
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


for prospective_mark in range(100):
    level_mark = []
    for module in modules:
        if module.mark is None:
            mark = prospective_mark
        else:
            mark = module.mark
        level_mark.append((module.level, mark))
    lowest_mark = min(mark for level, mark in level_mark if level > 4)
    final = weighted_average(level_mark)
    if final > 69:
        print("Average mark required: {0}".format(mark))
        break
