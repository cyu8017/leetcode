<?php
// LeetCode 0561 - Array Partition
// https://leetcode.com/problems/array-partition/

class Solution {
    function arrayPairSum($nums) {
        sort($nums);
        $total = 0;
        for ($i = 0; $i < count($nums); $i += 2) $total += $nums[$i];
        return $total;
    }
}
