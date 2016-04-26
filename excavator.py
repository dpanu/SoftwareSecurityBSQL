#!/usr/bin/env python

######################################################
#Project: Blind SQL Injection Exploit Automation
#Authors: Shruti Sonawane, Devanshi Panu
######################################################

import os
import sys
import string

def main():
     print "Starting excavator.............."

     #reading possible column values from file into HashMap
     columnMap ={}
     try:
	os.chdir("/home/ssonawane/Desktop/SoftwareSecurityBSQL")
	columnFile = open("PossibleColumnNames")
	for x, line in enumerate(columnFile):
		possibleColumns = line.split(':')
		columnMap[possibleColumns[0]] = possibleColumns[1]
	#        print possibleColumns[0], ": ",columnMap[possibleColumns[0]]
     	#for keys,values in columnMap.items():
       # 	print(keys),":",(values)
     except Exception as ex:
		print ex,"feefifofum"

     #reading possible query templates from file
     try:
	queryFile = open("PossibleQueries")
     except Exception as e:
	print e

     #reading possible table values from file
     try:
	tableFile = open("PossibleTables")
	for x, possibleTable in enumerate(tableFile):
		tables = possibleTable.split()
		columns = columnMap[tables[0]]
                columnList = columns.split(',')
		for col in columnList:
		        for y, line in enumerate(queryFile):
				query = line.split('\n')
				q1 = ""
				if "column" in query[0]:
					print "yay1"					
					q1 = query[0].replace("column","{bla1}")      
				if "table" in query[0]:
					print "yay2"
					if "column" in query[0]:
						print "yay3"
						q2 = q1.replace("table","{bla2}") 
						print q2.format(bla1=col, bla2=possibleTable)    
					else:
						q2 = query[0].replace("table","{bla2}")
						print q2.format(bla2 = possibleTable)
                                        
				if (not("column" in query[0]) and not("table" in query[0])):
					print query[0]
				else:
					print q1.format(bla1=col)
				
     except Exception as e:
	print e,"blabla"





if __name__ == '__main__':
    main()
		
