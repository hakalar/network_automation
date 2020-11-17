from pyparsing import col,Word,Optional,alphas,nums,ParseException

table = """\
12345678901234567890
COLOR      S   M   L
RED       10   2   2
BLUE           5  10
GREEN      3       5
PURPLE     8"""

# function to create column-specific parse actions
def mustMatchCols(startloc,endloc):
    def pa(s,l,t):
        if not startloc <= col(l,s) <= endloc:
            raise ParseException(s,l,"text not in expected columns")
    return pa

# helper to define values in a space-delimited table
def tableValue(expr, colstart, colend):
    return Optional(expr.copy().addParseAction(mustMatchCols(colstart,colend)))


# define the grammar for this simple table
colorname = Word(alphas)
integer = Word(nums).setParseAction(lambda t: int(t[0])).setName("integer")
row = (colorname("name") +
        tableValue(integer, 11, 12)("S") +
        tableValue(integer, 15, 16)("M") +
        tableValue(integer, 19, 20)("L"))

# parse the sample text - skip over the header and counter lines
for line in table.splitlines()[2:]:
    print
    print (line)
    print (row.parseString(line).dump())