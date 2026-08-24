<?php
// LeetCode 2740 - Find the Value of the Partition
// https://leetcode.com/problems/find-the-value-of-the-partition/

class Solution {
    function findValueOfPartition($nums) {
        sort($nums);
        $ans = PHP_INT_MAX;
        for ($i = 1; $i < count($nums); $i++) $ans = min($ans, $nums[$i] - $nums[$i - 1]);
        return $ans;
    }
}
