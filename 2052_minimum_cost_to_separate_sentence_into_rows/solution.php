<?php
// LeetCode 2052 - Minimum Cost to Separate Sentence Into Rows
// https://leetcode.com/problems/minimum-cost-to-separate-sentence-into-rows/

class Solution {
    /**
     * @param String $sentence
     * @param Integer $k
     * @return Integer
     */
    function minimumCost($sentence, $k) {
        $words = preg_split('/\s+/', trim($sentence));
        $n = count($words);
        $INF = PHP_INT_MAX / 4;
        $dp = array_fill(0, $n + 1, $INF);
        $dp[$n] = 0;
        for ($i = $n - 1; $i >= 0; $i--) {
            $length = -1;
            for ($j = $i; $j < $n; $j++) {
                $length += 1 + strlen($words[$j]);
                if ($length > $k) break;
                $cost = 0;
                if ($j < $n - 1) {
                    $extra = $k - $length;
                    $cost = $extra * $extra;
                }
                $dp[$i] = min($dp[$i], $cost + $dp[$j + 1]);
            }
        }
        return $dp[0];
    }
}
