from flask import Flask
app = Flask(__name__)

@dj.route("/Intro")

def hello():
    return "Hello. My name is Inigo Montoya. You killed my father. Prepare to die" 


@dj.route("/Quote")

def favQuote():
    return "Ever loved someone so much, you would do anything for them? Yeah, well make that someone yourself and do whatever the hell you want."

@dj.route("/MyCollegeList")


def collegeList():
    return "Columbia\nSORRY TO DEPRESSED TO CONTINUE"

if __name__=='__main__':
    dj.run()
else:
    print("welp sucks to suck")


