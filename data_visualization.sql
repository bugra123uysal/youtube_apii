
select * from youtubeapii
select DISTINCT country from youtubeapii 
select DISTINCT catogori from youtubeapii
select "Title","Comment" from youtubeapii order by "Comment"  desc

select "Title","Comment" from youtubeapii order by "Comment" asc

select "Title","Like","View" from youtubeapii order by "Like" asc
select "Title","Like","View" from youtubeapii order by "Like" desc

select "Title","country","View" from youtubeapii order by "View" asc
select "Title","country","View" from youtubeapii order by "View" desc


select * from youtubeapii
where country IN ('TR','IN', 'GB', 'DE', 'US')
order by country, "View" asc


select * from youtubeapii
where country IN ('TR','IN', 'GB', 'DE', 'US')
order by country, "View" desc
