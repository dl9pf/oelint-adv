from oelint_adv.cls_rule import Rule
from oelint_adv.cls_item import *

class VarHomepagePrefix(Rule):
    def __init__(self):
        super().__init__(id = "oelint.vars.dependsappend", 
                         severity="error",
                         message="DEPENDS should only be appended, not overwritten")

    def check(self, _file, stash):
        res = []
        items = stash.GetItemsFor(filename=_file, classifier=Variable.CLASSIFIER, attribute=Variable.ATTR_VAR, attributeValue="DEPENDS")
        for i in items:
            if not i.IsAppend():
                res += self.finding(i.Origin, i.InFileLine)
        return res