<?php
// LeetCode 3818 - Minimum Prefix Removal to Make Array Strictly Increasing
// https://leetcode.com/problems/minimum-prefix-removal-to-make-array-strictly-increasing/

class Solution {
    function minimumPrefixLength($nums) {
        for ($i = count($nums) - 1; $i > 0; $i--) {
            if ($nums[$i - 1] >= $nums[$i]) return $i;
        }
        return 0;
    }
}
