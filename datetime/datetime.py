from datetime import datetime

now = datetime.now()

-----------

from datetime import datetime

now = datetime.now()
print now
print now.year
print now.month
print now.day

-----------

from datetime import datetime
now = datetime.now()

print '%s/%s/%s' % (now.month, now.day, now.year)


-----------

rom datetime import datetime
now = datetime.now()

print '%s-%s-%s' % (now.year, now.month, now.day)

print '%s:%s:%s' % (now.hour, now.minute, now.second)


-----------

from datetime import datetime
now = datetime.now()

print '%s-%s-%s' % (now.year, now.month, now.day)

print '%s:%s:%s' % (now.hour, now.minute, now.second)

print '%s/%s/%s %s:%s:%s' % (now.month, now.day, now.year, now.hour, now.minute, now.second)
