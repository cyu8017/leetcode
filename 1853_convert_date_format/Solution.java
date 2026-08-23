// LeetCode 1853 - Convert Date Format
// https://leetcode.com/problems/convert-date-format/

class Solution {
    public static final String QUERY = "SELECT DATE_FORMAT(day, '%W, %M %e, %Y') AS day\n" +
        "FROM Days\n";
}
