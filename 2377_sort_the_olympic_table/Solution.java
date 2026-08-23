// LeetCode 2377 - Sort the Olympic Table
// https://leetcode.com/problems/sort-the-olympic-table/

class Solution {
    public static final String QUERY = """
SELECT *
FROM Olympic
ORDER BY 2 DESC, 3 DESC, 4 DESC, 1
""";
}
