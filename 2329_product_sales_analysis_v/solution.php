<?php
// LeetCode 2329 - Product Sales Analysis V
// https://leetcode.com/problems/product-sales-analysis-v/

const QUERY = <<<'SQL'
SELECT user_id, SUM(quantity * price) AS spending
FROM
    Sales
    JOIN Product USING (product_id)
GROUP BY 1
ORDER BY 2 DESC, 1
SQL;
