import sys
import os
from phgl_imp import *
from zqh_full_chip_common.zqh_full_chip_common_main import zqh_full_chip_common
from zqh_system_e1.zqh_system_e1_main import zqh_system_e1

class zqh_full_chip_e1(zqh_full_chip_common):
    def instance_system(self):
        return zqh_system_e1('system', imp_mode = self.p.imp_mode)
