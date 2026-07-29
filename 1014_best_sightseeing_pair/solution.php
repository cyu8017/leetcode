<?php
// LeetCode 1014 - Best Sightseeing Pair
// https://leetcode.com/problems/best-sightseeing-pair/

class Solution {
    /**
     * @param Integer[] $values
     * @return Integer
     */
    function maxScoreSightseeingPair($values) {
        $best = $values[0];
        $ans = 0;
        $n = count($values);
        for ($j = 1; $j < $n; $j++) {
            $ans = max($ans, $best + $values[$j] - $j);
            $best = max($best, $values[$j] + $j);
        }
        return $ans;
    }
}
