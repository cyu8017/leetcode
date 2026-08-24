// LeetCode 1341 - Movie Rating
// https://leetcode.com/problems/movie-rating/

class Solution {
    companion object {
        const val QUERY = "(SELECT u.name AS results\n" +
            " FROM MovieRating r JOIN Users u USING (user_id)\n" +
            " GROUP BY u.user_id, u.name\n" +
            " ORDER BY COUNT(*) DESC, u.name\n" +
            " LIMIT 1)\n" +
            "UNION ALL\n" +
            "(SELECT m.title AS results\n" +
            " FROM MovieRating r JOIN Movies m USING (movie_id)\n" +
            " WHERE r.created_at >= '2020-02-01' AND r.created_at < '2020-03-01'\n" +
            " GROUP BY m.movie_id, m.title\n" +
            " ORDER BY AVG(r.rating) DESC, m.title\n" +
            " LIMIT 1)"
    }
}
