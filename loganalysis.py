#!/usr/bin/env python3
#
# Log analysis program for udacity.

import psycopg2

DBNAME = "news"

# The 3 most popular articles of all time
QUESTION1 = "The 3 most popular articles of all time"
QUERY1 = (
    "SELECT title, COUNT(title) AS views " +
    "FROM log, articles " +
    "WHERE path LIKE concat('/article/',slug) " +
    "AND status = '200 OK' AND method = 'GET' " +
    "GROUP BY title ORDER BY views DESC LIMIT 3")

# The most popular article authors of all time
QUESTION2 = "The most popular article authors of all time"
QUERY2 = (
    "SELECT name, COUNT(name) AS views FROM log, articles, authors " +
    "WHERE authors.id = articles.author AND path like concat('%',slug,'%') " +
    "AND status='200 OK' AND method='GET' GROUP BY name ORDER BY views DESC ")

# Days with more than 1% of request that lead to an error
QUESTION3 = "Days with more than 1% of request that lead to an error"
QUERY3 = (
    "SELECT a.date AS date, ROUND(error*100/correct::numeric,2) as errate " +
    "FROM (SELECT time::date as date, count(*) as error " +
    "FROM log WHERE status LIKE '404%' GROUP BY time::date) AS a, " +
    "(SELECT time::date AS date, COUNT(*) AS correct  "
    "FROM log GROUP BY time::date) AS b " +
    "WHERE a.date = b.date AND  error*100/correct::numeric >1")


# executes query
def get_result(cursor, query_string):
    cursor.execute(query_string)
    return cursor.fetchall()


# print result
def print_result(question, data):
    print("\n" + question + " are:\n")
    for a, b in data:
        print('\t"' + str(a) + '" -- ' + str(b) + " views")


# print result
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
