此为sublime text 3 的插件，功能是把多行文本拼接成源码中可用的字符串内容，支持Java/C#、C/C++、PHP/Perl、Delphi、Obj-C。

插件源码说明：
    Context.sublime-menu:鼠标右键上下文菜单。

    Default (Windows).sublime-keymap：键盘映射。

    CopyWithQuotes.py：插件源代码

    Default.sublime-commands：命令定义

    Main.sublime-menu：功能菜单（可以不要）

    package-metadata.json：不确定是否必须

    packages.json：仓库必须

插件示例：

    普通文本：
    select *, "xx" from  bo_msg t
    where t.msg_id = "2" and z=1

    Java/C#:
    "select *, \"xx\" from  bo_msg t\n" +
    "where t.msg_id = \"2\" and z=1"

    C/C++:
    "select *, \"xx\" from  bo_msg t\n"
    "where t.msg_id = \"2\" and z=1"

    PHP/Perl:
    "select *, \"xx\" from  bo_msg t\n" .
    "where t.msg_id = \"2\" and z=1"

    Delphi:
    'select *, "xx" from  bo_msg t' + #13#10 +
    'where t.msg_id = "2" and z=1'

    Obj-C:
    @"select *, \"xx\" from  bo_msg t\n\
    where t.msg_id = \"2\" and z=1"

使用方法：
    选中文本，右键进入Copy with quotes的菜单，选择语言。