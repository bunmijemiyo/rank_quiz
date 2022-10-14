"""
Given a time in -hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

Example
s='12:01:00PM'
Return '12:01:00'.

s='12:01:00AM'
Return '00:01:00'.

Sample Input
07:05:45PM

Sample Output
19:05:45
"""

def timeConversion(s):
    # Write your code here

    if s.endswith("PM"):
        if s[:2] == "12":
            return(s[:-2])
        else:
            return(str(int(s[:2]) + 12) + s[2:-2])
    elif s.endswith("AM"):
        if s[:2] == "12":
            return("00" + s[2:-2])
        else:
            return(s[:-2])
