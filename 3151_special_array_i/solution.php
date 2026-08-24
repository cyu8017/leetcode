<?php
// LeetCode 3151 - Special Array I
// https://leetcode.com/problems/special-array-i/

class Solution {
    function isArraySpecial($nums) {
        $n = count($nums);
        for ($i = 1; $i < $n; $i++) {
            if ($nums[$i] % 2 === $nums[$i - 1] % 2) return false;
        }
        return true;
    }
}
