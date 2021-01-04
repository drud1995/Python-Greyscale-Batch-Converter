How to setup Python batch file:

1. Download the latest version of Python from the official website: https://www.python.org/downloads/

2. Open command prompt ("cmd" in the Windows search bar) 

3. Check to make sure "pip" is installed by typing "pip" in command prompt.
	- You should get a large options list if everything is setup properly.
	
4. Install the "Pillow" module for Python
	-Enter the following command in command prompt "pip install pillow"
	- Also enter the following command in command prompt "pip3 install pillow"
	
5. Prepare batch file for easy use:
	- Open "greyscale.bat" in a text editor - Notepad included in Windows works fine.
	- Contents of file looks like this:
	
		"C:\Users\drud1\AppData\Local\Programs\Python\Python39\python.exe" "C:\Users\drud1\Desktop\RGB to Greyscale\IMG_converter.py"
		pause
		
	- The file path for python.exe will be similar, just click on your HDD on my computer until you find this path containing "python.exe"
		+Replace my initial path with your new path
		+Do the same thing with the second path above in parenthesis containing "IMG_converter.py" depending on path where it's stored on your PC
		
6. Save the batch file in your text editor, and you can now just double click the batch file to automatically run the Python script.
	-Store images to convert in the folder labeled "RGB" and greyscale images will appear in the folder labeled "Greyscale" after running the batch file
	
7. Hope this helps!