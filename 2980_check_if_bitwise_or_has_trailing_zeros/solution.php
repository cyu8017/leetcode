<?php
// LeetCode 2980 - Check if Bitwise OR Has Trailing Zeros
// https://leetcode.com/problems/check-if-bitwise-or-has-trailing-zeros/

class Solution {
    function hasTrailingZeros($nums) {
        $even = 0;
        foreach ($nums as $v) {
            if ($v % 2 === 0) {
                $even++;
                if ($even >= 2) return true;
            }
        }
        return false;
    }
}
