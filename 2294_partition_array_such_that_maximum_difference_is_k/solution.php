<?php
// LeetCode 2294 - Partition Array Such That Maximum Difference Is K
// https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/

class Solution {
    function partitionArray($nums, $k) {
        sort($nums);
        $ans = 1;
        $start = $nums[0];
        for ($i = 1; $i < count($nums); $i++) {
            if ($nums[$i] - $start > $k) { $ans++; $start = $nums[$i]; }
        }
        return $ans;
    }
}
