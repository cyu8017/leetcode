// LeetCode 3358 - Books with NULL Ratings
// https://leetcode.com/problems/books-with-null-ratings/

const char* QUERY =
    "\n"
    "SELECT book_id, title, author, published_year\n"
    "FROM books\n"
    "WHERE rating IS NULL\n"
    "ORDER BY 1;\n";
