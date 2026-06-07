# Journal desciption:
# This journal will close windows (undisplay / close tabs) of all of the open parts
# that have variable "mask" in their name
# If all of the open parts are fit to criteria, it will close everything.
#
# Written in Python
# Tested on Siemens NX 2412

import NXOpen
import NXOpen.Features


def main():

    theSession = NXOpen.Session.GetSession()
    mask = "GEO"

    for myPart in theSession.Parts.GetDisplayedParts():
        if mask in str(myPart.Name):
            myPart.Undisplay()


if __name__ == "__main__":
    main()
