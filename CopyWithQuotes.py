import sublime
import sublime_plugin
import re


class CwqJavaCsharpCommand(sublime_plugin.TextCommand):
    # Convert Tabs To Spaces
    def run(self, edit):
        for sel_region in self.view.sel():
            if not sel_region.empty():
                sel_text = self.view.substr(sel_region)
                q_text = quotes_java_csharp(sel_text)
                sublime.set_clipboard(q_text)
                sublime.status_message("quotes for Java/C# !")
            else:
                sublime.status_message("quotes error !")
        return


class CwqCppCommand(sublime_plugin.TextCommand):
    # Convert Tabs To Spaces
    def run(self, edit):
        sublime.status_message("not support C/C++ !")
        return


class CwqPhpPerlCommand(sublime_plugin.TextCommand):
    # Convert Tabs To Spaces
    def run(self, edit):
        sublime.status_message("not support PHP/Perl !")
        return


class CwqDelphiCommand(sublime_plugin.TextCommand):
    # Convert Tabs To Spaces
    def run(self, edit):
        sublime.status_message("not support Delphi !")
        return


class CwqObjcCommand(sublime_plugin.TextCommand):
    # Convert Tabs To Spaces
    def run(self, edit):
        sublime.status_message("not support Obj-c !")
        return


def quotes_java_csharp(str):
    sep = "\n"
    m1 = re.search("\r\n", str)
    if m1:
        sep = "\r\n"
    lines = re.split("\r\n|\n", str)
    content = ""
    count = 0
    for line in lines:
        line = line.replace('"', '\\"')
        if (count < len(lines) - 1):
            content += '"' + line + '" + ' + sep
        else:
            content += '"' + line + '";'
        count += 1
    return content
