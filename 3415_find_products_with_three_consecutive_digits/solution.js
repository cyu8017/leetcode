// LeetCode 3415 - Find Products With Three Consecutive Digits
// https://leetcode.com/problems/find-products-with-three-consecutive-digits/

var QUERY = `SELECT product_id, name
FROM Products
WHERE name REGEXP '(^|[^0-9])[0-9]{3}([^0-9]|$)'
ORDER BY 1;`;

module.exports = { QUERY };
