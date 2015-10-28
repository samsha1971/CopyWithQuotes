this plugin is used for sublime text 3 ，add quotes for multiline text for Java/C#、C/C++、PHP/Perl、Delphi、Obj-C source code string.


sample：

    common text：
	
    select *, "xx" from  bo_msg t
    where t.msg_id = "2" and z=1
	
	
	after add quotes:

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

how to use：
    select text in sublime text，click mouse right key , find context menu "Copy with quotes"，click submenu for target language。