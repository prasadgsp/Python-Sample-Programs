import urllib

def read_text():
    file=open("D:\online courses\U.D.A.C.I.T.Y\Programming Foundations with Python\movie_quotes.txt")
    contents=file.read()
    print(contents)
    check_profanity(contents)
    file.close()

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+text_to_check)
    output=connection.read()
    print(output)
    connection.close()
    if "true" in output:
        print("Bad Word!!")
    elif "false" in output:
        print("No bad word!!")
    else:
        print("Could not scan document")

read_text()
