-- task_4.sql: Script to show full description of Books table

SELECT COLUMN_NAME, COLUMN_TYPE
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'alx_book_store'
AND TABLE_NAME = 'Books'
ORDER BY ORDINAL_POSITION;
