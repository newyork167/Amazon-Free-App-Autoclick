Amazon-Free-App-Autoclick
=========================

A utility for automatically grabbing the free app of the day. Just fill in your username and password and run. You can set this up to automatically run once a day and never worry about forgetting your free app of the day!

To Schedule with Windows:

  1. Open the windows task scheduler
  2. Click Action->Create Basic Task
  3. Give the task a name
  4. Choose daily for the trigger
  5. Choose a time for the script to run
  6. Choose Start a program
  7. For the Program/script browse for your python.exe
  8. For the arguments give the file path for the python script
  9. Finish adding the task and let it go!

To Schedule with Linux:
  1. Open a terminal
  2. Execute "crontab -e"
  3. Add an entry to the file: 29 0 * * * /path/to/this/pythonFile.py - This will exectute ate 12:30am everyday
  4. Save the file and watch it get you free stuff (or not if you go to bed :P)
