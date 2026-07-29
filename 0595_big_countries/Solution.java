// LeetCode 0595 - Big Countries
// https://leetcode.com/problems/big-countries/

class Solution {
    public static final String QUERY = """
SELECT name, population, area
FROM World
WHERE area >= 3000000 OR population >= 25000000
""";
}
