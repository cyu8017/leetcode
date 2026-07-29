<?php
// LeetCode 1322 - Ads Performance
// https://leetcode.com/problems/ads-performance/

const QUERY = <<<'SQL'
SELECT ad_id,
       ROUND(IFNULL(100 * SUM(action = 'Clicked') /
                    NULLIF(SUM(action IN ('Clicked', 'Viewed')), 0), 0), 2) AS ctr
FROM Ads
GROUP BY ad_id
ORDER BY ctr DESC, ad_id
SQL;
