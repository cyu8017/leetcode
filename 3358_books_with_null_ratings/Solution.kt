// LeetCode 3358 - Books With Null Ratings
// https://leetcode.com/problems/books-with-null-ratings/

class Solution {
    companion object {
        const val QUERY = "SELECT book_id, title, author, published_year\n" +
            "FROM books\n" +
            "WHERE rating IS NULL\n" +
            "ORDER BY 1;"
    }
}
