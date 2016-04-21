# with open("poems.txt") as f:
#      for line in f:
#            print(line, end='')

#
# -> exceptions_finally.py
# -> TRY-TEDST.PY
#
# 21-4-2016 MK
#


import sys
import time

f = None
try:
    # f = open("poem.txt")
    # Our usual file-reading idiom
    # while True:
#        line = f.readline()
#        if len(line) == 0:
#            break
#        print(line, end='')

        with open("poem.txt") as f:
              for line in f:
                    print(line, end='')


        sys.stdout.flush()
        print("Press ctrl+c now")
        # To make sure it runs for a while
        time.sleep(4)
except IOError:
    print("Could not find file poem.txt")
except KeyboardInterrupt:
    print("!! You cancelled the reading from the file.")
finally:
    if f:
        f.close()
    print("(Cleaning up: Closed the file)")
