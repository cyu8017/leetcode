<?php
// LeetCode 1503 - Last Moment Before All Ants Fall Out of a Plank
// https://leetcode.com/problems/last-moment-before-all-ants-fall-out-of-a-plank/

class Solution {
    /**
     * @param Integer $n
     * @param Integer[] $left
     * @param Integer[] $right
     * @return Integer
     */
    function getLastMoment($n, $left, $right) {
        $leftMax = empty($left) ? 0 : max($left);
        $rightMin = empty($right) ? $n : min($right);
        return max($leftMax, $n - $rightMin);
    }
}
