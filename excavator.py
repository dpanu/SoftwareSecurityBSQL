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
	os.chdir("/home/swetasinghal28/cse545/SoftwareSecurityBSQL")
	columnFile = open("PossibleColumnNames")
	for x, line in enumerate(columnFile):
		possibleColumns = line.split(':')
		columnMap[possibleColumns[0]] = possibleColumns[1]
	#        print possibleColumns[0], ": ",columnMap[possibleColumns[0]]
     	#for keys,values in columnMap.items():
       # 	print(keys),":",(values)
     
	
	
	#reading possible table values from file
	tableFile = open("PossibleTables")
	for x, possibleTable in enumerate(tableFile):
		tables = possibleTable.split()
		columns = columnMap[tables[0]]
                columnList = columns.split(',')
		for z,col in enumerate(columnList):
			#reading possible query templates from file
			queryFile = open("PossibleQueries")
		        for y, line in enumerate(queryFile):
				if "column" in line:
					q1 = line.replace("column",col)
				if "table" in line:
					if "column" in line:
						q2 = q1.replace("table",tables[0])
						print q2
					else:
						q2 = line.replace("table",tables[0])
						print q2
                                        
				if (not("column" in line) and not("table" in line)):
					print line
				
				continue
			continue
		continue
     except Exception as e:
	print e,"blabla"





if __name__ == '__main__':
    main()
		
