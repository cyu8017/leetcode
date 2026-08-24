<?php
// LeetCode 0330 - Patching Array
// https://leetcode.com/problems/patching-array/

class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $n
     * @return Integer
     */
    function minPatches($nums, $n) {
        $patches = 0;
        $miss = 1;
        $index = 0;
        $count = count($nums);
        while ($miss <= $n) {
            if ($index < $count && $nums[$index] <= $miss) {
                $miss += $nums[$index];
                $index++;
            } else {
                $miss += $miss;
                $patches++;
            }
        }
        return $patches;
    }
}
