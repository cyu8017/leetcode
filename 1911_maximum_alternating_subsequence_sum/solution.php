<?php
// LeetCode 1911 - Maximum Alternating Subsequence Sum
// https://leetcode.com/problems/maximum-alternating-subsequence-sum/

class Solution {
    function maxAlternatingSum($nums) {
        $even = 0;
        $odd = 0;
        foreach ($nums as $x) {
            $newEven = max($even, $odd + $x);
            $newOdd = max($odd, $even - $x);
            $even = $newEven;
            $odd = $newOdd;
        }
        return $even;
    }
}
