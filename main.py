from art import *
import sys

tprint("Custom  Installer  v2")
print("""
[1] Make an installer
[2] Exit
""")


def install(name, link, download):
  write = f"""REM an installer for {name}
 GUI R
 DELAY 600
 STRING chrome
 DELAY 1000
 STRING {link}
 DELAY 400
 CTRL N
 DELAY 700
 STRING {download}
 DELAY 800
 CTRL N
 DELAY 600
 STRING Thank you for installing {name}"""

  f = open('payload.dd', 'w')
  f.write(write)
  f.close()
  print(f"Your installer for {name} has been built")


option = input("[?]: ")

if option == '1':
  name = input("Enter your app name: ")
  link = input("Enter link to homepage: ")
  download = input('Enter link to download page: ')
  install(name, link, download)

if option == '2':
  sys.exit()
