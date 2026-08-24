<?php
// LeetCode 3810 - Minimum Operations to Reach Target Array
// https://leetcode.com/problems/minimum-operations-to-reach-target-array/

class Solution {
    function minOperations($nums, $target) {
        $s = [];
        for ($i = 0; $i < count($nums); $i++) {
            if ($nums[$i] !== $target[$i]) $s[$nums[$i]] = true;
        }
        return count($s);
    }
}
