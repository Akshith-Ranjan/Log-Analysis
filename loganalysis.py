#!/usr/bin/env python3
#
# Log analysis program for udacity.

import psycopg2

DBNAME = "news"

QUESTION1 = "The 3 most popular articles of all time"
QUERY1 = (
    "SELECT title, COUNT(title) AS views " +
    "FROM log, articles " +
    "WHERE path LIKE concat('%',slug,'%') " +
    "AND status = '200 OK' AND method = 'GET' " +
    "GROUP BY title ORDER BY views DESC LIMIT 3")

QUESTION2 = "The most popular article authors of all time"
QUERY2 = (
    "SELECT name, COUNT(name) AS views FROM log, articles, authors " +
    "WHERE authors.id = articles.author AND path like concat('%',slug,'%') " +
    "AND status='200 OK' AND method='GET' GROUP BY name ORDER BY views DESC ")

QUESTION3 = "Days with more than 1% of request that lead to an error"
QUERY3 = (
    "select a.date as date, trunc(error*100/correct::numeric,2) as errate " +
    "from (select time::date as date, count(*) as error " +
    "from log where status like '404%' group by time::date) as a, " +
    "(select time::date as date, count(*) as correct  "
    "from log where status like '200%' group by time::date) as b " +
    "where a.date = b.date and  error*100/correct::numeric >1")


def get_result(cursor, query_string):
    cursor.execute(query_string)
    return cursor.fetchall()


def print_result(question, data):
    print("\n" + question + " are:\n")
    for a, b in data:
        print('\t"' + str(a) + '" -- ' + str(b) + " views")


def print_error_result(question, data):
    print("\n" + question + " are:\n")
    for a, b in data:
        print('\t' + str(a) + ' -- ' + str(b) + "% errors")

if __name__ == '__main__':
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()

    result1 = get_result(c, QUERY1)
    result2 = get_result(c, QUERY2)
    result3 = get_result(c, QUERY3)

    print_result(QUESTION1, result1)
    print_result(QUESTION2, result2)
    print_error_result(QUESTION3, result3)

    db.close()
