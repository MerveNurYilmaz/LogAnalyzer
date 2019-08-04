# LogAnalyzer
LogAnalyzer is a reporting tool that prints out reports based on the data in the database.

## Prerequisites
- Python 3
- PostgreSQL
- psycopg2 library

## Create news database
Data for news database can be found in the link:
[Download newsdata](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

Create news database from shell
`sudo -u postgres createdb news`

To import the data from newsdata.sql to the news database, run the command below in shell
`psql -d news -f newsdata.sql`


## Create article_view_counts view
In order to create the view first connect to the news database, from shell
`psql news`

Create the article_view_counts view
`create view article_view_counts as (select split_part(path, '/', 3) as article_slug, count(*) from log where path like '/article%' and status = '200 OK' group by path order by count(*) desc)`
