data = { 
    "name" : "deep", 
    "course" : ["ml", "dl", "py", "stats", "cv"],
    "msg" : "This is my class" 
}

def get_course():
    return data["course"]


def msg():
    return data["msg"]