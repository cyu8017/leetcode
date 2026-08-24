<?php
// LeetCode 0945 - Minimum Increment to Make Array Unique
// https://leetcode.com/problems/minimum-increment-to-make-array-unique/

class Solution {
    function minIncrementForUnique($nums) {
        sort($nums);
        $ans = 0;
        $n = count($nums);
        for ($i = 1; $i < $n; $i++) {
            if ($nums[$i] <= $nums[$i - 1]) {
                $need = $nums[$i - 1] + 1;
                $ans += $need - $nums[$i];
                $nums[$i] = $need;
            }
        }
        return $ans;
    }
}
