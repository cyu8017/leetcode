<?php
// LeetCode 1149 - Article Views Ii
// https://leetcode.com/problems/article-views-ii/

const QUERY = <<<'SQL'
SELECT DISTINCT viewer_id AS id
FROM Views
GROUP BY viewer_id, view_date
HAVING COUNT(DISTINCT article_id) > 1
ORDER BY id
SQL;
