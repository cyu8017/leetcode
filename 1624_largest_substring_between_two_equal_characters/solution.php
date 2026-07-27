<?php
// LeetCode 1624 - Largest Substring Between Two Equal Characters
// https://leetcode.com/problems/largest-substring-between-two-equal-characters/

class Solution {
    /**
     * @param String $s
     * @return Integer
     */
    function maxLengthBetweenEqualCharacters($s) {
        $first = [];
        $ans = -1;
        $len = strlen($s);
        for ($i = 0; $i < $len; $i++) {
            $ch = $s[$i];
            if (isset($first[$ch])) {
                $ans = max($ans, $i - $first[$ch] - 1);
            } else {
                $first[$ch] = $i;
            }
        }
        return $ans;
    }
}
