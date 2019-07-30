# LogAnalyzer
LogAnalyzer is a reporting tool that prints out reports based on the data in the database.

##Prerequisites
- python3
- psycopg2 library
- article_view_counts view
##article_view_counts
`create view article_view_counts as (select split_part(path, '/', 3) as article_slug, count(*) from log where path like '/article%' and status = '200 OK' group by path order by count(*) desc)`
