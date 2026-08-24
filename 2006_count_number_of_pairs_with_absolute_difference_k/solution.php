<?php
// LeetCode 2006 - Count Number of Pairs With Absolute Difference K
// https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/

class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer
     */
    function countKDifference($nums, $k) {
        $freq = [];
        $ans = 0;
        foreach ($nums as $x) {
            $ans += $freq[$x - $k] ?? 0;
            $ans += $freq[$x + $k] ?? 0;
            $freq[$x] = ($freq[$x] ?? 0) + 1;
        }
        return $ans;
    }
}
