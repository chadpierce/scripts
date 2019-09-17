#defeats sleep

On Error Resume Next
Dim MyDate
Dim WshShell
Set WshShell = WScript.CreateObject("WScript.Shell")
Set Fso = Createobject("Scripting.FileSystemObject")

MyDate = (DateAdd("n",14400,Now()))

'Launch Popup window with time Presentation Mode will end. 
MsgBox ("Presentation Mode Enabled until " & MyDate), vbSystemModal + vbInformation

for i=1 To 14400
	'f1.writeline i
	WshShell.SendKeys("{F15}")
	WScript.Sleep(14400)
Next
