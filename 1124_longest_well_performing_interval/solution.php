<?php
// LeetCode 1124 - Longest Well-Performing Interval
// https://leetcode.com/problems/longest-well-performing-interval/

class Solution {
    /**
     * @param Integer[] $hours
     * @return Integer
     */
    function longestWPI($hours) {
        $score = 0;
        $ans = 0;
        $seen = [];
        foreach ($hours as $i => $h) {
            $score += $h > 8 ? 1 : -1;
            if ($score > 0) {
                $ans = $i + 1;
            } else {
                if (!isset($seen[$score])) $seen[$score] = $i;
                if (isset($seen[$score - 1])) {
                    $ans = max($ans, $i - $seen[$score - 1]);
                }
            }
        }
        return $ans;
    }
}
