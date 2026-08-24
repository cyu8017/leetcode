<?php
// LeetCode 2615 - Sum of Distances
// https://leetcode.com/problems/sum-of-distances/

class Solution {
    function distance($nums) {
        $n = count($nums);
        $ans = array_fill(0, $n, 0);
        $pos = [];
        for ($i = 0; $i < $n; $i++) {
            if (!isset($pos[$nums[$i]])) $pos[$nums[$i]] = [];
            $pos[$nums[$i]][] = $i;
        }
        foreach ($pos as $idxs) {
            $m = count($idxs);
            $pref = array_fill(0, $m + 1, 0);
            for ($i = 0; $i < $m; $i++) $pref[$i + 1] = $pref[$i] + $idxs[$i];
            for ($j = 0; $j < $m; $j++) {
                $idx = $idxs[$j];
                $left = $j * $idx - $pref[$j];
                $right = $pref[$m] - $pref[$j + 1] - ($m - 1 - $j) * $idx;
                $ans[$idx] = $left + $right;
            }
        }
        return $ans;
    }
}
