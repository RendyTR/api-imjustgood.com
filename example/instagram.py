from justgood import imjustgood

api     = imjustgood("YOUR_APIKEY_HERE")
data    = api.instagram("the.autobots_corp")
print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES
result  = "ID : {}".format(data["result"]["id"])
result += "\nUsername : {}".format(data["result"]["username"])
result += "\nFullname : {}".format(data["result"]["fullname"])
result += "\nBiography : {}".format(data["result"]["biography"])
result += "\nWebsite : {}".format(data["result"]["website"])
result += "\nPrivate : {}".format(data["result"]["private"])
result += "\nVerified : {}".format(data["result"]["verified"])
result += "\nBusiness : {}".format(data["result"]["business"]["status"])
result += "\nCategory : {}".format(data["result"]["business"]["category"])
result += "\nFollower : {}".format(data["result"]["follower"])
result += "\nFollowing : {}".format(data["result"]["following"])
result += "\nPost : {}".format(data["result"]["post"])
result += "\nHighlights : {}".format(len(data["result"]["highlights"]))
result += "\n\nPicture :\n{}".format(data["result"]["picture"])
result += "\n\nProfile :\n{}".format(data["result"]["profile"])
if data["result"]["lastpost"] != []:
    number  = 0
    result += "\n\nLastpost"
    for a in data["result"]["lastpost"]:
        number += 1
        result += "\n{}. {}".format(number, a["caption"])
        result += "\n{}".format(a["url"])
        result += "\n   Like : {}".format(number, a["like"])
        result += "\n   Comment : {}".format(number, a["comment"])
        result += "\n   Created : {}".format(a["created"])
        result += "\n   PageUrl : {}".format(a["page"])
print(result)
