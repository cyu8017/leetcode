# LeetCode 3293 - Calculate Product Final Price
# https:# leetcode.com/problems/calculate-product-final-price/

# Write your MySQL query statement below
QUERY = """
SELECT
    product_id,
    price * (100 - IFNULL(discount, 0)) / 100 final_price,
    category
FROM
    Products
    LEFT JOIN Discounts USING (category)
ORDER BY 1;
"""
