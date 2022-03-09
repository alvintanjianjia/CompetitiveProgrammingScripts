def failTable(pattern):
    # Create the resulting table, which for length zero is None.
    result = [None]

    # Iterate across the rest of the characters, filling in the values for the
    # rest of the table.
    for i in range(0, len(pattern)):
        # Keep track of the size of the subproblem we're dealing with, which
        # starts off using the first i characters of the string.
        j = i

        while True:
            # If j hits zero, the recursion says that the resulting value is
            # zero since we're looking for the LPB of a single-character
            # string.
            if j == 0:
                result.append(0)
                break

            # Otherwise, if the character one step after the LPB matches the
            # next character in the sequence, then we can extend the LPB by one
            # character to get an LPB for the whole sequence.
            if pattern[result[j]] == pattern[i]:
                result.append(result[j] + 1)
                break

            # Finally, if neither of these hold, then we need to reduce the
            # subproblem to the LPB of the LPB.
            j = result[j]
    
    return result

# Function: kmpMatch(needle, haystack)
# Usage: print kmpMatch("0101", "0011001011") # Prints 5
# -----------------------------------------------------------------------------
# Uses the KMP algorithm to find an occurrence of the specified needle string
# in the haystack string.  To do this, we compute the failure table, which
# is done above.  Next, we iterate across the string, keeping track of a
# candidate start point and length matched so far.  Whenever a match occurs, we
# update the length of the match we've made.  On a failure, we update these
# values by trying to preserve the maximum proper border of the string we were
# able to manage by that point.
def kmpMatch(needle, haystack):
    # Compute the failure table for the needle we're looking up.
    fail = failTable(needle)

    # Keep track of the start index and next match position, both of which
    # start at zero since our candidate match is at the beginning and is trying
    # to match the first character.
    index = 0
    match = 0

    # Loop until we fall off the string or match.
    while index + match < len(haystack):
        print (index, match)

        # If the current character matches the expected character, then bump up
        # the match index.
        if haystack[index + match] == needle[match]:
            match = match + 1

            # If we completely matched everything, we're done.
            if match == len(needle):
                return index

        # Otherwise, we need to look at the fail table to determine what to do
        # next.
        else:
            # If we couldn't match the first character, then just advance the
            # start index.  We need to try again.
            if match == 0:
                index = index + 1

            # Otherwise, see how much we need to skip forward before we have
            # another feasible match.
            else:
                index = index + match - fail[match]
                match = fail[match]
    return None


def solution(s):
    
    failArr = failTable(s)
    
    length = len(s) - failArr[-1]
    
    ans = len(s) // length


    if len(s) % ans == 0:
        return ans
    else:
        1


test = solution('abcabcabcabc')
print(test)

test = solution('abccbaabccba')
print(test)
test = solution('abcabcabcabc')
print(test)
test = solution('abccbaabccba')
print(test)