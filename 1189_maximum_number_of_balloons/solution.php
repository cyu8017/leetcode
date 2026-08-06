<?php
// LeetCode 1189 - Maximum Number of Balloons
// https://leetcode.com/problems/maximum-number-of-balloons/

class Solution {
    /**
     * @param String $text
     * @return Integer
     */
    function maxNumberOfBalloons($text) {
        $count = array_count_values(str_split($text));
        return min(
            $count['b'] ?? 0,
            $count['a'] ?? 0,
            intdiv($count['l'] ?? 0, 2),
            intdiv($count['o'] ?? 0, 2),
            $count['n'] ?? 0
        );
    }
}
