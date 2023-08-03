import os
import time
import urllib.parse
import pyfiglet
from printy import printy

# Prompt the user to enter a search string

asciiBanner = pyfiglet.figlet_format("gScan!")
printy(asciiBanner, 'y')
printy("[rI]This is a Google Dorking tool")
search_string = input("Enter a search string: ")

# Construct the Google search URLs
search_urls = [
    "https://www.google.com/search?q=site%3A" + urllib.parse.quote(search_string) + "+intitle:index.of",
    "https://www.google.com/search?q=site%3A" + search_string + "+ext%3Axml+OR+ext%3Aconf+OR+ext%3Acnf+OR+ext%3Areg+OR+ext%3Ainf+OR+ext%3Ardp+OR+ext%3Acfg+OR+ext%3Atxt+OR+ext%3Aora+OR+ext%3Aini"
,"https://www.google.com/search?q=inurl:q= | inurl:s= | inurl:search= | inurl:query= | inurl:keyword= | inurl:lang= inurl:%26 site:"+ search_string

,
    "https://www.google.com/search?q=site:inurl:id= | inurl:pid= | inurl:category= | inurl:cat= | inurl:action= | inurl:sid= | inurl:dir= inurl:%26 site:"+ search_string,
    "https://www.google.com/search?q=site:inurl:src=http | inurl:r=http  | inurl:url= | inurl:return= | inurl:next= | inurl:redirect= | inurl:redir= | inurl:ret= | inurl:r2= | inurl:page= inurl:%26 inurl:http site:"+ search_string
  ,
    "https://www.google.com/search?q=site:"+ search_string +"+ext:doc+|+ext:docx+|+ext:odt+|+ext:pdf+|+ext:rtf+|+ext:sxw+|+ext:psw+|+ext:ppt+|+ext:pptx+|+ext:pps+|+ext:csv",
    "https://www.google.com/search?q=site:"+ search_string +"+ext:php+intitle:phpinfo+%22published+by+the+PHP+Group%22",
      "https://www.google.com/search?q=site:"+ search_string +"+ext:log",
    "https://www.google.com/search?q=site:"+ search_string +"+inurl:shell+|+inurl:backdoor+|+inurl:wso+|+inurl:cmd+|+shadow+|+passwd+|+boot.ini+|+inurl:backdoor",
    "https://www.google.com/search?q=site:pastebin.com+"+ search_string,
    "https://www.google.com/search?q=site:"+ search_string +"+inurl:readme+|+inurl:license+|+inurl:install+|+inurl:setup+|+inurl:config",
    "https://www.google.com/search?q=site:"+ search_string +"+inurl:%22/phpinfo.php%22+|+inurl:%22.htaccess%22+|+inurl:%22/.git%22+string%20-github",
    "https://www.google.com/search?q=site:*."+ search_string,
    "https://www.google.com/search?q=site:*.*."+ search_string,
    "https://crt.sh/?q=%25."+ search_string,
        "https://www.google.com/search?q=site:"+ search_string +"+ext:sql+|+ext:dbf+|+ext:mdb",
    "https://www.shodan.io/search?query="+ search_string, "", ""
]
while True:
    # Prompt the user to select a search to use
    printy("Which search do you want to use?", 'y')
    print("1. Directory Listing Vulnerabilities")
    print("2. Exposed Configuration Files")
    print("3. XSS Hunter")
    print("4. SQL Prone Parameters")
    print("5. Open Redirects")
    print("6. Publicly Exposed Documents")
    print("7. phpinfo()")
    print("8. Exposed Log Files")
    print("9. Finding Backdoors")
    print("10. Find Pastebin Entries")
    print("11. Install / Setup Files")
    print("12. .htaccess Files")
    print("13. Subdomains")
    print("14. Sub-Subdomains")
    print("15. check crt.sh")
    print("16. Exposed Database Files")
    print("17. SHODAN")
    print("Type 'end' or 'exit' to exit.")
    choice = input("Enter the number of the search you want to use (1-17): ")
    if choice.lower() in ["end", "exit"]:
        exit(0)
    elif choice.isdigit() and int(choice) in range(1, 17):
        # Open the selected search URL in the default web browser
        os.system('xdg-open "' + search_urls[int(choice) - 1] + '"')
    else:
        print("Invalid choice. Please enter a number between 1 and 17.")
        continue
