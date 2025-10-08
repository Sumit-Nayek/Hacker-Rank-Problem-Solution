'''
Given a time in -hour AM/PM format, convert it to military (24-hour) time.
Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.
Example

Return '12:01:00'.

Return '00:01:00'.
Function Description
Complete the  function with the following parameter(s):
: a time in  hour format
Returns
: the time in  hour format
Input Format
A single string  that represents a time in -hour clock format (i.e.:  or ).
Constraints
All input times are valid
'''
def timeConversion(s):
    # Extract AM/PM part
    period = s[-2:]
    # Extract hour, minute, and second parts
    hh, mm, ss = s[:-2].split(':')

    hh = int(hh)

    # Convert hours based on AM/PM
    if period == 'AM':
        if hh == 12:
            hh = 0
    else:  # PM
        if hh != 12:
            hh += 12

    # Format hour to 2 digits and return the final string
    return '{:02d}:{}:{}'.format(hh, mm, ss)


# Input reading
s = input().strip()
# Function call and print result
print(timeConversion(s))
