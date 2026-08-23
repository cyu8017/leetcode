// LeetCode 1757 - Recyclable and Low Fat Products
// https://leetcode.com/problems/recyclable-and-low-fat-products/

public class Solution {
    public static final String QUERY = "SELECT product_id\n" +
        "FROM Products\n" +
        "WHERE low_fats = 'Y' AND recyclable = 'Y';\n";
}
