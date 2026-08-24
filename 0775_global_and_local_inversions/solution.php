<?php
// LeetCode 0775 - Global and Local Inversions
// https://leetcode.com/problems/global-and-local-inversions/

class Solution {
    function isIdealPermutation($nums) {
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            if (abs($nums[$i] - $i) > 1) return false;
        }
        return true;
    }
}
