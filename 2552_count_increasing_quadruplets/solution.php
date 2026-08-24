<?php
// LeetCode 2552 - Count Increasing Quadruplets
// https://leetcode.com/problems/count-increasing-quadruplets/

class Solution {
    function countQuadruplets($nums) {
        $n = count($nums);
        $ans = 0;
        $great = array_fill(0, $n, 0);
        for ($j = 0; $j < $n; $j++) {
            for ($i = 0; $i < $j; $i++) {
                if ($nums[$i] < $nums[$j]) $ans += $great[$i];
                else if ($nums[$i] > $nums[$j]) $great[$i]++;
            }
        }
        return $ans;
    }
}
