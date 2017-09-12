import datetime

now = datetime.datetime.now()

print
print "Current date adn time using str method of datetime object:"
print str(now)

print
print "Current date and time using instance attributes:"
print "Current year: %d" % now.year
print "Current month: %d" % now.month
print "Current day: %d" % now.day
print "Current hour: %d" % now.hour
print "Current minute: %d" % now.minute
print "Current second: %d" % now.second
print "Current microsecond: %d" % now.microsecond

print # Use this! it is much more convenient.
print "Current date and time using strftime:"
print now.strftime("%Y-%m-%d %H:%M")