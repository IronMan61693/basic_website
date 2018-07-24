import sqlite3

def connectMe():
	con = sqlite3.connect('wackyWebsitedb.sqlite3')
	c = con.cursor()

	return c,con