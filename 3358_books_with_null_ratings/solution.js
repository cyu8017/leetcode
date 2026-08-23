// LeetCode 3358 - Books With Null Ratings
// https://leetcode.com/problems/books-with-null-ratings/

var QUERY = `SELECT book_id, title, author, published_year
FROM books
WHERE rating IS NULL
ORDER BY 1;`;

module.exports = { QUERY };
