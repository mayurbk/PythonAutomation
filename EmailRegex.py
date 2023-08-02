#matching an email with regex
import re

# emailRegex = re.compile(r''''
# (
# [a-zA-Z0-9._%-+]+
# @
# [a-zA-Z0-9.-]+
# (\.[a-zA-Z]{2,4})
# )
# ''')
#
# emailObj = emailRegex.match("My email id is mayur2_3@gmail.com and it is not Mayur332@hotmail.com")
# print(emailObj)

regexEmail = re.compile(r'([A-Za-z0-9]+[._])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
def validemail(email):
    if re.fullmatch(regexEmail,email):
        print("Your email" +email+ "is valid")
    else:
        print("invalid email")

validemail("mayur.kotoky@gmail.com")

#validating Date in the format (date/month/year) (2010-2025)