<?php
// LeetCode 1742 - Maximum Number of Balls in a Box
// https://leetcode.com/problems/maximum-number-of-balls-in-a-box/

class Solution {
    /**
     * @param Integer $lowLimit
     * @param Integer $highLimit
     * @return Integer
     */
    function countBalls($lowLimit, $highLimit) {
        $counts = [];
        for ($value = $lowLimit; $value <= $highLimit; $value++) {
            $box = array_sum(str_split((string)$value));
            $counts[$box] = ($counts[$box] ?? 0) + 1;
        }
        return max($counts);
    }
}
