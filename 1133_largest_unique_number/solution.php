<?php
// LeetCode 1133 - Largest Unique Number
// https://leetcode.com/problems/largest-unique-number/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function largestUniqueNumber($nums) {
        $cnt = array_count_values($nums);
        $ans = -1;
        foreach ($cnt as $num => $c) {
            if ($c === 1) $ans = max($ans, $num);
        }
        return $ans;
    }
}
