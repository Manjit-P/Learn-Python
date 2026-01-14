import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste() # Access clipboard for location. 

# Open the web browser.
webbrowser.open('https://www.openstreetmap.org/search?query=' + address)