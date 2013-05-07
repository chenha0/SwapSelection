import sublime
import sublime_plugin
from collections import deque


class SwapSelectionCommand(sublime_plugin.TextCommand):
    def run(self, edit, manner):
        # self.view.insert(edit, 0, self.view.sel());
        self.sel_iter = self.view.sel()
        self.sel_str_list = deque(self.build_sel_str_list())

        self.edit = self.view.begin_edit('swap_sel')
        self.swap(manner)
        self.view.end_edit(self.edit)

    def swap(self, manner):
        if manner == 1:
            self.sel_str_list.rotate(1)
        elif manner == 2:
            self.sel_str_list.rotate(-1)
        elif manner == 3:
            # the python in sublime has no reverse() method for deque :(
            reversed_list = []
            while len(self.sel_str_list):
                reversed_list.append(self.sel_str_list.pop())
            self.sel_str_list = deque(reversed_list)

        for idx, sel in enumerate(self.sel_iter):
            self.view.replace(self.edit,
                sel,
                self.sel_str_list[idx])

    def build_sel_str_list(self):
        str_list = []
        for s in self.sel_iter:
            str_list.append(self.view.substr(s))
        return str_list
