from __future__ import (
    unicode_literals,
    absolute_import,
    print_function,
    division,
    )

from uuid import UUID

from . import core
from .utils import register_class
from . import mobs

@register_class
class ContentStorage(core.AAFObject):
    class_id = UUID("0d010101-0101-1800-060e-2b3402060101")

    def mobs(self):
        for key, mob in self["Mobs"].items():
            yield mob
    def add_mob(self, mob):
        self['Mobs'].append(mob)

    def lookup_mob(self, mob_id):
        # should replace this
        for key, mob in self["Mobs"].items():
            if key == mob_id:
                return mob

    def toplevel(self):
        for mob in self.mobs():
            if mob.usage == 'Usage_TopLevel':
                yield mob

    def mastermobs(self):
        for mob in self.mobs():
            if isinstance(mob, mobs.MasterMob):
                yield mob

    def compositionmobs(self):
        for mob in self.mobs():
            if isinstance(mob, mobs.CompositionMob):
                yield mob

    def sourcemobs(self):
        for mob in self.mobs():
            if isinstance(mob, mobs.SourceMob):
                yield mob

    def essencedata(self):
        for key, essencedata in self["EssenceData"].items():
            yield essencedata

    def add_essencedata(self, essencedata):
        self["EssenceData"].append(essencedata)
