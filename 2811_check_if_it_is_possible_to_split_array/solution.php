<?php
// LeetCode 2811 - Check if it is Possible to Split Array
// https://leetcode.com/problems/check-if-it-is-possible-to-split-array/

class Solution {
    function canSplitArray($nums, $m) {
        $n = count($nums);
        if ($n <= 2) return true;
        for ($i = 0; $i + 1 < $n; $i++) {
            if ($nums[$i] + $nums[$i + 1] >= $m) return true;
        }
        return false;
    }
}
