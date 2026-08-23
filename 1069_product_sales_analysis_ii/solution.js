// LeetCode 1069 - Product Sales Analysis Ii
// https://leetcode.com/problems/product-sales-analysis-ii/

var QUERY = `SELECT product_id, SUM(quantity) AS total_quantity
FROM Sales
GROUP BY product_id`;

module.exports = { QUERY };
