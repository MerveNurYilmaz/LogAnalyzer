#!/usr/bin/env python3
import psycopg2

db = psycopg2.connect("dbname=news")
cursor = db.cursor()

# 1. find the three most popular articles
cursor.execute("select articles.title, article_view_counts.count "
               "from article_view_counts, articles "
               "where articles.slug = article_view_counts.article_slug "
               "order by article_view_counts.count desc limit 3")
articles = cursor.fetchall()

print("1. The three most popular articles of all time are:")
for article in articles:
    print("\t" + str(article[0]) + " - " + str(article[1]) + " views")


# 2. find the most popular article authors
cursor.execute("select authors.name, sum(article_view_counts.count) "
               "from article_view_counts, articles, authors "
               "where article_view_counts.article_slug = articles.slug "
               "and articles.author = authors.id "
               "group by authors.name "
               "order by sum(article_view_counts.count) desc")
articles = cursor.fetchall()

print("\n2. The most popular article authors are:")
for article in articles:
    print("\t" + str(article[0]) + " - " + str(article[1]) + " views")

# 3. find the days with more than 1% errors
cursor.execute("select to_char(cast(time as date), 'FMMonth DD,yyyy') "
               "as log_date, round((count(case when status = '404 NOT FOUND' "
               "then log.id end) * 100)::numeric / count(*), 1) "
               "as error_rate from log group by log_date "
               "having round((count(case when status = '404 NOT FOUND' "
               "then log.id end) * 100)::numeric / count(*), 1) > 1 ")
articles = cursor.fetchall()

print("\n3. Days on which more than 1% of requests lead to errors:")
for article in articles:
    print("\t" + str(article[0]) + " - " + str(article[1]) + "% errors")
