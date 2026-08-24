<?php
// LeetCode 2505 - Bitwise OR of All Subsequence Sums
// https://leetcode.com/problems/bitwise-or-of-all-subsequence-sums/

class Solution {
    function subsequenceSumOr($nums) {
        $ans = 0;
        $prefix = 0;
        foreach ($nums as $x) {
            $prefix += $x;
            $ans |= $x | $prefix;
        }
        return $ans;
    }
}
