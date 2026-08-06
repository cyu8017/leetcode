<?php
// LeetCode 1208 - Get Equal Substrings Within Budget
// https://leetcode.com/problems/get-equal-substrings-within-budget/

class Solution {
    /**
     * @param String $s
     * @param String $t
     * @param Integer $maxCost
     * @return Integer
     */
    function equalSubstring($s, $t, $maxCost) {
        $left = $cost = $answer = 0;
        $n = strlen($s);
        for ($right = 0; $right < $n; $right++) {
            $cost += abs(ord($s[$right]) - ord($t[$right]));
            while ($cost > $maxCost) {
                $cost -= abs(ord($s[$left]) - ord($t[$left]));
                $left++;
            }
            $answer = max($answer, $right - $left + 1);
        }
        return $answer;
    }
}
