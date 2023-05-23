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
,
    "https://www.google.com/search?q=site:"+ search_string +"+ext:sql+|+ext:dbf+|+ext:mdb"
,
    "https://www.google.com/search?q=site:"+ search_string +"+intext:%22sql+syntax+near%22+|+intext:%22syntax+error+has+occurred%22+|+intext:%22incorrect+syntax+near%22+|+intext:%22unexpected+end+of+SQL+command%22+|+intext:%22Warning:+mysql_connect()%22+|+intext:%22Warning:+mysql_query()%22+|+intext:%22Warning:+pg_connect()%22",
    "https://www.google.com/search?q=site:"+ search_string +"+ext:log",
    "https://www.google.com/search?q=site:"+ search_string +"+ext:doc+|+ext:docx+|+ext:odt+|+ext:pdf+|+ext:rtf+|+ext:sxw+|+ext:psw+|+ext:ppt+|+ext:pptx+|+ext:pps+|+ext:csv",
    "https://www.google.com/search?q=site:"+ search_string +"+ext:php+intitle:phpinfo+%22published+by+the+PHP+Group%22",
    "https://www.google.com/search?q=site:"+ search_string +"+inurl:redir+|+inurl:url+|+inurl:redirect+|+inurl:return+|+inurl:src=http+|+inurl:r=http",
    "https://www.google.com/search?q=site:"+ search_string +"+inurl:shell+|+inurl:backdoor+|+inurl:wso+|+inurl:cmd+|+shadow+|+passwd+|+boot.ini+|+inurl:backdoor",
    "https://www.google.com/search?q=site:pastebin.com+"+ search_string,
    "https://www.google.com/search?q=site:"+ search_string +"+inurl:readme+|+inurl:license+|+inurl:install+|+inurl:setup+|+inurl:config",
    "https://www.google.com/search?q=site:"+ search_string +"+inurl:%22/phpinfo.php%22+|+inurl:%22.htaccess%22+|+inurl:%22/.git%22+string%20-github",
    "https://www.google.com/search?q=site:*."+ search_string,
    "https://www.google.com/search?q=site:*.*."+ search_string,
    "https://crt.sh/?q=%25."+ search_string,
    "https://google.com/search?q=site:" + search_string +"+inurl%3A%22.php%3Fcmd%3D%22+%7C+inurl%3A%22.php%3Fz%3D%22+%7C+inurl%3A%22.php%3Fq%3D%22+%7C+inurl%3A%22.php%3Fsearch%3D%22+%7C+inurl%3A%22.php%3Fquery%3D%22+%7C+inurl%3A%22.php%3Fsearchst%C2%ADring%3D%22+%7C+inurl%3A%22.php%3Fkeyword%3D%C2%AD%22+%7C+inurl%3A%22.php%3Ffile%3D%22+%7C+inurl%3A%22.php%3Fyears%3D%22+%7C+inurl%3A%22.php%3Ftxt%3D%22+%7C+inurl%3A%22.php%3Ftag%3D%22+%7C+inurl%3A%22.php%3Fmax%3D%22+%7C+inurl%3A%22.php%3Ffrom%3D%22+%7C+inurl%3A%22.php%3Fauthor%3D%22+%7C+inurl%3A%22.php%3Fpass%3D%22+%7C+inurl%3A%22.php%3Ffeedback%C2%AD%3D%22+%7C+inurl%3A%22.php%3Fmail%3D%22+%7C+inurl%3A%22.php%3Fcat%3D%22+%7C+inurl%3A%22.php%3Fvote%3D%22+%7C+inurl%3Asearch.php%3Fq%3D+%7C+inurl%3Acom_feedpostol%C2%ADd%2Ffeedpost.php%3Furl%3D+%7C+inurl%3Ascrapbook.php%3F%C2%ADid%3D+%7C+inurl%3Aheadersearch.p%C2%ADhp%3Fsid%3D+%7C+inurl%3A%2Fpoll%2F%C2%ADdefault.asp%3Fcatid%3D+%7C+inurl%3A%2F%C2%ADsearch_results.php%3Fse%C2%ADarch%3D+%7C+inurl%3AcategoryId+%7C+inurl%3AstoreId++%7C+inurl%3AresultCatEntryType+%7C+inurl%3AsearchTermScope+%7C+inurl%3A%E2%80%9Dwebapp%2Fwcs%E2%80%9D+%7C+inurl%3A%E2%80%9DProductListingView%E2%80%9D+%7C+inurl%3A%E2%80%9DAdvancedSearchDisplay%E2%80%9D+%7C+inurl%3A%E2%80%9DCompareProductsDisplayView%E2%80%9D+%7C+inurl%3Aparent_category_rn",
    "https://www.shodan.io/search?query="+ search_string, "", ""
]
while True:
    # Prompt the user to select a search to use
    printy("Which search do you want to use?", 'y')
    print("1. Directory Listing Vulnerabilities")
    print("2. Exposed Configuration Files")
    print("3. Exposed Database Files")
    print("4. Search SQL Errors")
    print("5. Exposed Log Files")
    print("6. Publicly Exposed Documents")
    print("7. phpinfo()")
    print("8. Open Redirects")
    print("9. Finding Backdoors")
    print("10. Find Pastebin Entries")
    print("11. Install / Setup Files")
    print("12. .htaccess Files")
    print("13. Subdomains")
    print("14. Sub-Subdomains")
    print("15. check crt.sh")
    print("16. XSS Hunter")
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

