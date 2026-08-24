<?php
// LeetCode 3396 - Minimum Number of Operations to Make Elements in Array Distinct
// https://leetcode.com/problems/minimum-number-of-operations-to-make-elements-in-array-distinct/

class Solution {
    function minimumOperations($nums) {
        $list = $nums;
        $ops = 0;
        while (true) {
            $seen = [];
            $dup = false;
            foreach ($list as $x) {
                if (isset($seen[$x])) { $dup = true; break; }
                $seen[$x] = true;
            }
            if (!$dup) return $ops;
            if (count($list) <= 3) return $ops + 1;
            $list = array_slice($list, 3);
            $ops++;
        }
    }
}
