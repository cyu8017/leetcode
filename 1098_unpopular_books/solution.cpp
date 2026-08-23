// LeetCode 1098 - Unpopular Books
// https://leetcode.com/problems/unpopular-books/

const char* QUERY = R"SQL(
SELECT b.book_id, b.name
FROM Books b
LEFT JOIN Orders o
    ON b.book_id = o.book_id
   AND o.dispatch_date >= '2018-06-23'
WHERE b.available_from <= '2019-05-23'
GROUP BY b.book_id, b.name
HAVING COALESCE(SUM(o.quantity), 0) < 10
)SQL";
