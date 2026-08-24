<?php
// LeetCode 2908 - Minimum Sum of Mountain Triplets I
// https://leetcode.com/problems/minimum-sum-of-mountain-triplets-i/

class Solution {
    function minimumSum($nums) {
        $n = count($nums);
        $INF = 1 << 30;
        $ans = $INF;
        for ($j = 1; $j < $n - 1; $j++) {
            $left = $INF;
            $right = $INF;
            for ($i = 0; $i < $j; $i++)
                if ($nums[$i] < $nums[$j] && $nums[$i] < $left) $left = $nums[$i];
            for ($k = $j + 1; $k < $n; $k++)
                if ($nums[$k] < $nums[$j] && $nums[$k] < $right) $right = $nums[$k];
            if ($left < $INF && $right < $INF) {
                $cand = $left + $nums[$j] + $right;
                if ($cand < $ans) $ans = $cand;
            }
        }
        return $ans === $INF ? -1 : $ans;
    }
}
