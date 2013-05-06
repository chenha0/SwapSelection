import sublime, sublime_plugin
from collections import deque

class SwapSelectionCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # self.view.insert(edit, 0, self.view.sel());
        self.sel_iter = self.view.sel()
        self.sel_str_list = deque(self.build_sel_str_list())

        self.edit = self.view.begin_edit('swap_sel')
        self.swap()
        self.view.end_edit(self.edit)

    def swap(self):
        self.sel_str_list.rotate(1)
        for idx, sel in enumerate(self.sel_iter):
            self.view.replace(self.edit,
                sel,
                self.sel_str_list[idx])

    def build_sel_str_list(self):
        str_list = []
        for s in self.sel_iter:
            str_list.append(self.view.substr(s))
        return str_list