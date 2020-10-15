
import sys

def getTokens( inf ) :
    # word up!
    for lt in [ line.split() for line in inf ] :
        if not lt :
            continue
        for t in lt :
            yield t

c_i = 0.
i   = 0
a_i, s_i, d_i = 0., 0., 0.
d_sum, w_sum, s_sum = 0., 0., 0.

data = open( sys.argv[1] if len(sys.argv) > 1 else "/dev/null" )
tokens = iter(getTokens(data))

try :
    while True :
        a_i, s_i = float(next(tokens)), float(next(tokens))
        i += 1

        if  a_i < c_i :
            d_i = c_i - a_i
            d_sum += d_i
        else :
            d_i = 0

        c_i = a_i + d_i + s_i

        s_sum += s_i
        w_sum += d_i + s_i
except StopIteration :
    pass
except :
    raise

if i :
    print( "jobs                 ", i )
    print( "average interarrival ", a_i/i )
    print( "average delay        ", d_sum/i )
    print( "average wait         ", w_sum/i )
    print( "average service      ", s_sum/i )

data.close()
sys.exit(0)
