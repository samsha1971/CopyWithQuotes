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
        for sel_region in self.view.sel():
            if not sel_region.empty():
                sel_text = self.view.substr(sel_region)
                q_text = quotes_cpp(sel_text)
                sublime.set_clipboard(q_text)
                sublime.status_message("quotes for Java/C# !")
            else:
                sublime.status_message("quotes error !")
        return


class CwqPhpPerlCommand(sublime_plugin.TextCommand):
    # Convert Tabs To Spaces
    def run(self, edit):
        for sel_region in self.view.sel():
            if not sel_region.empty():
                sel_text = self.view.substr(sel_region)
                q_text = quotes_php_perl(sel_text)
                sublime.set_clipboard(q_text)
                sublime.status_message("quotes for Java/C# !")
            else:
                sublime.status_message("quotes error !")
        return


class CwqDelphiCommand(sublime_plugin.TextCommand):
    # Convert Tabs To Spaces
    def run(self, edit):
        for sel_region in self.view.sel():
            if not sel_region.empty():
                sel_text = self.view.substr(sel_region)
                q_text = quotes_delphi(sel_text)
                sublime.set_clipboard(q_text)
                sublime.status_message("quotes for Java/C# !")
            else:
                sublime.status_message("quotes error !")
        return


class CwqObjcCommand(sublime_plugin.TextCommand):
    # Convert Tabs To Spaces
    def run(self, edit):
        for sel_region in self.view.sel():
            if not sel_region.empty():
                sel_text = self.view.substr(sel_region)
                q_text = quotes_objc(sel_text)
                sublime.set_clipboard(q_text)
                sublime.status_message("quotes for Java/C# !")
            else:
                sublime.status_message("quotes error !")
        return


def quotes_java_csharp(str):
    sep = "\n"
    lines = str.splitlines()
    #lines = re.split(sep, str)
    #lines = [x for x in lines if x != '']
    content = ""
    count = 0
    for line in lines:
        line = line.replace('"', '\\"')
        if (count < len(lines) - 1):
            content += '"' + line + '\\n" + ' + sep
        else:
            content += '"' + line + '"'
        count += 1
    return content


def quotes_cpp(str):
    sep = "\n"
    lines = str.splitlines()
    #lines = re.split(sep, str)
    #lines = [x for x in lines if x != '']
    content = ""
    count = 0
    for line in lines:
        line = line.replace('"', '\\"')
        if (count < len(lines) - 1):
            content += '"' + line + '\\n"' + sep
        else:
            content += '"' + line + '"'
        count += 1
    return content


def quotes_php_perl(str):
    sep = "\n"
    lines = str.splitlines()
    #lines = re.split(sep, str)
    #lines = [x for x in lines if x != '']
    content = ""
    count = 0
    for line in lines:
        line = line.replace('"', '\\"')
        if (count < len(lines) - 1):
            content += '"' + line + '\\n" . ' + sep
        else:
            content += '"' + line + '"'
        count += 1
    return content


def quotes_delphi(str):
    sep = "\n"
    lines = str.splitlines()
    #lines = re.split(sep, str)
    #lines = [x for x in lines if x != '']
    content = ""
    count = 0
    for line in lines:
        line = line.replace("'", "''")
        if (count < len(lines) - 1):
            content += "'" + line + "\' + #13#10 + " + sep
        else:
            content += "'" + line + "'"
        count += 1
    return content


def quotes_objc(str):
    sep = "\n"
    lines = str.splitlines()
    #lines = re.split(sep, str)
    #lines = [x for x in lines if x != '']
    content = '@"'
    count = 0
    for line in lines:
        line = line.replace('"', '\\"')
        if (count < len(lines) - 1):
            content += line + "\\n\\" + sep
        else:
            content += line + '"'
        count += 1
    return content
