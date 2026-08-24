<?php
// LeetCode 2036 - Maximum Alternating Subarray Sum
// https://leetcode.com/problems/maximum-alternating-subarray-sum/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maximumAlternatingSubarraySum($nums) {
        $ans = PHP_INT_MIN;
        $even = 0;
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            $x = $nums[$i];
            if ($i % 2 === 0) $even += $x;
            else $even = max(0, $even - $x);
            $ans = max($ans, $even);
        }
        $odd = 0;
        for ($i = 1; $i < $n; $i++) {
            $x = $nums[$i];
            if ($i % 2 === 1) $odd += $x;
            else $odd = max(0, $odd - $x);
            $ans = max($ans, $odd);
        }
        return $ans;
    }
}
