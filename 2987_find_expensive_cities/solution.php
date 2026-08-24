<?php
// LeetCode 2987 - Find Expensive Cities
// https://leetcode.com/problems/find-expensive-cities/

const QUERY = <<<'SQL'
SELECT city
FROM Listings
GROUP BY city
HAVING AVG(price) > (SELECT AVG(price) FROM Listings)
ORDER BY 1
SQL;
