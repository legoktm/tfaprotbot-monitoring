What are human readable timedeltas? 
===============================================

ago.py makes customizable human readable timedeltas, for example:

Testing past tense::

 Russell commented 1 year, 127 days, 16 hours ago
 You replied 1 year, 127 days ago

Testing future tense::

 Program will shutdown in 2 days, 3 hours, 27 minutes
 Job will run 2 days, 3 hours from now


How to install
===================

There are a number of ways to install this package::

 easy_install ago

 pip install ago

or specify *ago* under the *setup_requires* list within your
*setuptools*-compatible project's *setup.py* file.


How to use
==================

The ago module comes with two functions: 

#. human
#. delta2dict

You really only need to worry about *human*.

Here are all the available arguments and defaults::

 human(dt, precision=2, past_tense='{} ago', future_tense='in {}'):

dt
 either a datetime or timedelta object to become human readable, required

precision
 control how verbose the output should look, optional

past_tense
 format string used when dt is a past datetime, optional

future_tense
 format string used when dt is a future datetime, optional


Here is an example on how to use *human*::

 from ago import human
 from ago import delta2dict
 
 from datetime import datetime
 from datetime import timedelta

 # pretend this was stored in database
 db_date = datetime( 
   year = 2010, 
   month=5, 
   day=4, 
   hour=6, 
   minute=54, 
   second=33, 
   microsecond=4000
  )

 # to find out how long ago, use the human function
 print 'Created ' + human( db_date )
 
 # optionally pass a precision
 print 'Created ' + human( db_date, 3 )
 print 'Created ' + human( db_date, 6 )

We also support future dates and times::

 PRESENT = datetime.now()
 PAST = PRESENT - timedelta( 492, 58711, 45 ) # days, secs, ms
 FUTURE = PRESENT + timedelta( 2, 12447, 963 ) # days, secs, ms

 print human( FUTURE )

Example past_tense and future_tense keyword arguments::

 output1 = human( PAST,
   past_tense = 'titanic sunk {0} ago',
   future_tense = 'titanic will sink in {0} from now'
 )

 output2 = human( FUTURE,
   past_tense = 'titanic sunk {0} ago',
   future_tense = 'titanic will sink in {0} from now'
 )

 print output1
 # titanic sunk 1 year, 127 days ago
 print output2
 # titanic will sink in 2 days, 3 hours from now

Now we will document how to use delta2dict::

 # subtract two datetime objects for a timedelta object
 delta = PRESENT - db_date

 # create a dictionary of units out of the timedelta
 print delta2dict( delta )


Need more examples?
==========================

You should look at test_ago.py


How do I thank you?
==========================

You should follow me on twitter http://twitter.com/russellbal


License
=========================

Public Domain


Public Revision Control
==============================

https://bitbucket.org/russellballestrini/ago
