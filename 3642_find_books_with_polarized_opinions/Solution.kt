// LeetCode 3642 - Find Books With Polarized Opinions
// https://leetcode.com/problems/find-books-with-polarized-opinions/

class Solution {
    companion object {
        const val QUERY = "SELECT\n" +
            "    book_id,\n" +
            "    title,\n" +
            "    author,\n" +
            "    genre,\n" +
            "    pages,\n" +
            "    (MAX(session_rating) - MIN(session_rating)) AS rating_spread,\n" +
            "    ROUND((SUM(session_rating <= 2) + SUM(session_rating >= 4)) / COUNT(1), 2) polarization_score\n" +
            "FROM\n" +
            "    books\n" +
            "    JOIN reading_sessions USING (book_id)\n" +
            "GROUP BY book_id\n" +
            "HAVING\n" +
            "    COUNT(1) >= 5\n" +
            "    AND MAX(session_rating) >= 4\n" +
            "    AND MIN(session_rating) <= 2\n" +
            "    AND polarization_score >= 0.6\n" +
            "ORDER BY polarization_score DESC, title DESC;"
    }
}
