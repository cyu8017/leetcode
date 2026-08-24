<?php
// LeetCode 2009 - Minimum Number of Operations to Make Array Continuous
// https://leetcode.com/problems/minimum-number-of-operations-to-make-array-continuous/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function minOperations($nums) {
        $n = count($nums);
        $uniq = array_values(array_unique($nums));
        sort($uniq);
        $ans = $n;
        $j = 0;
        $un = count($uniq);
        for ($i = 0; $i < $un; $i++) {
            while ($j < $un && $uniq[$j] - $uniq[$i] + 1 <= $n) $j++;
            $ans = min($ans, $n - ($j - $i));
        }
        return $ans;
    }
}
