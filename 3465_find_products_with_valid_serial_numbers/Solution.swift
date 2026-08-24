// LeetCode 3465 - Find Products With Valid Serial Numbers
// https://leetcode.com/problems/find-products-with-valid-serial-numbers/

let QUERY = """
SELECT product_id, product_name, description
FROM products
WHERE description REGEXP '(?-i)\\bSN[0-9]{4}-[0-9]{4}\\b'
ORDER BY 1;
"""
