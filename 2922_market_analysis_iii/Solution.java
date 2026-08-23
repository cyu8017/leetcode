// LeetCode 2922 - Market Analysis III
// https://leetcode.com/problems/market-analysis-iii/

class Solution {
    public static final String QUERY = """
WITH
    T AS (
        SELECT seller_id, COUNT(DISTINCT item_id) AS num_items
        FROM
            Orders
            JOIN Users USING (seller_id)
            JOIN Items USING (item_id)
        WHERE item_brand != favorite_brand
        GROUP BY 1
    )
SELECT seller_id, num_items
FROM T
WHERE num_items = (SELECT MAX(num_items) FROM T)
ORDER BY 1
""";
}
