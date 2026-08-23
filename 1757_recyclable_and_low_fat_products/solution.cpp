// LeetCode 1757 - Recyclable and Low Fat Products
// https://leetcode.com/problems/recyclable-and-low-fat-products/

const char* QUERY = R"SQL(
SELECT product_id
FROM Products
WHERE low_fats = 'Y' AND recyclable = 'Y';
)SQL";
