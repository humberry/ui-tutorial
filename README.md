ui-tutorial
===========

As you surely noticed there are two ways of writing a ui-script. If you use only a few GUI elements you might write all 
the code in your script.py, but that's not what I want to show you here. I want to show you how to use the UI design tool
to speed up the process and write only some code. Please be patient, I'm starting with the basics.

1.) Create a "Script with UI"
2.) Push "+"
3.) Add a "Label"
4.) Push the Label until the menu apears and choose "Attributes..."
=> What's the difference between Name and Text?
=> Access the GUI Element via the name in your code. But the Text is what you see on the screen.
5.) Please change the text from label to "Hello World".
6.) Now change to your script with the button at the right of the "+" (it's looking like a script)
7.) You should see the following code:

  # coding: utf-8
  
  import ui

8.) Please add at the end:

  view = load_view('NameOfTheScript')  # e.g. load_view('Untitled 1')
  view.present('fullscreen')

9.) Run the script and admire your label.
