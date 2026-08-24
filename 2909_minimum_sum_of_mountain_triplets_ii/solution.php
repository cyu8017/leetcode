<?php
// LeetCode 2909 - Minimum Sum of Mountain Triplets II
// https://leetcode.com/problems/minimum-sum-of-mountain-triplets-ii/

class Solution {
    function minimumSum($nums) {
        $n = count($nums);
        $INF = 1 << 30;
        $left = array_fill(0, $n, 0);
        $right = array_fill(0, $n, 0);
        $mn = $INF;
        for ($i = 0; $i < $n; $i++) {
            $left[$i] = $mn;
            if ($nums[$i] < $mn) $mn = $nums[$i];
        }
        $mn = $INF;
        for ($i = $n - 1; $i >= 0; $i--) {
            $right[$i] = $mn;
            if ($nums[$i] < $mn) $mn = $nums[$i];
        }
        $ans = $INF;
        for ($j = 1; $j < $n - 1; $j++) {
            if ($left[$j] < $nums[$j] && $right[$j] < $nums[$j]) {
                $cand = $left[$j] + $nums[$j] + $right[$j];
                if ($cand < $ans) $ans = $cand;
            }
        }
        return $ans === $INF ? -1 : $ans;
    }
}
