// LeetCode 1821 - Find Customers With Positive Revenue this Year
// https://leetcode.com/problems/find-customers-with-positive-revenue-this-year/

class Solution {
    public static final String QUERY = """
SELECT customer_id
FROM Customers
WHERE year = 2021 AND revenue > 0
""";
}
