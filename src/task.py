# Flowshutter
# Copyright (C) 2021  Hugo Chiang

# Flowshutter is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Flowshutter is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with flowshutter.  If not, see <https://www.gnu.org/licenses/>.
import protocols.common as common
import vram
import gui.logic as ui
import time, gc

class Task:
    def __init__(self):
        print(str(time.ticks_us()) + " [Create] Task scheduler")
        self.fc_link = common.CRSF()
        self.mem_opt_interval = 100 # gc per 100ms
        self.ui = ui.Logic()
        print(str(time.ticks_us()) + " [  OK  ] Task scheduler")

    def mem_opt(self):
        gc.enable()
        gc.collect()
        gc.disable()

    def scheduler(self, t):
        self.mem_opt_interval -= 5

        # task1 - FC RC packeet sender
        self.fc_link.send_packet(t)

        # task2 - OLED display or GC
        if vram.oled_tasklist != []:
            # print(vram.oled_tasklist)
            i = vram.oled_tasklist[0]
            self.ui.show_sub(i)
            del vram.oled_tasklist[0]
        elif self.mem_opt_interval < 0:
            self.mem_opt()
            self.mem_opt_interval = 100
