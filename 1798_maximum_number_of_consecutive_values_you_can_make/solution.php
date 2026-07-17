<?php
// LeetCode 1798 - Maximum Number of Consecutive Values You Can Make
// https://leetcode.com/problems/maximum-number-of-consecutive-values-you-can-make/

class Solution {
    /**
     * @param Integer[] $coins
     * @return Integer
     */
    function getMaximumConsecutive($coins) {
        sort($coins);
        $reach = 0;
        foreach ($coins as $coin) {
            if ($coin > $reach + 1) break;
            $reach += $coin;
        }
        return $reach + 1;
    }
}
