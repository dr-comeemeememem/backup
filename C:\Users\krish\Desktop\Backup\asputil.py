# Date created: Thu Oct 21 15:34:26 2021
# Last date modified: Sat Jul 24 17:17:04 2021
"""A utility module for ASP (Active Server Pages on MS Internet Info Server.

Contains:
	iif -- A utility function to avoid using "if" statements in ASP <% tags

"""

def iif(cond, t, f):
	if cond:
		return t
	else:
		return f
