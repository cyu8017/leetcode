<?php
// LeetCode 3191 - Minimum Operations to Make Binary Array Elements Equal to One I
// https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i/

class Solution {
    function minOperations($nums) {
        $ans = 0;
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            if ($nums[$i] === 0) {
                if ($i + 2 >= $n) return -1;
                $nums[$i + 1] ^= 1;
                $nums[$i + 2] ^= 1;
                $ans++;
            }
        }
        return $ans;
    }
}
