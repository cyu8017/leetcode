<?php
// LeetCode 1121 - Divide Array Into Increasing Sequences
// https://leetcode.com/problems/divide-array-into-increasing-sequences/

class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Boolean
     */
    function canDivideIntoSubsequences($nums, $k) {
        $n = count($nums);
        $freq = [];
        $maxFreq = 0;
        foreach ($nums as $x) {
            $freq[$x] = ($freq[$x] ?? 0) + 1;
            $maxFreq = max($maxFreq, $freq[$x]);
        }
        return $maxFreq * $k <= $n;
    }
}
