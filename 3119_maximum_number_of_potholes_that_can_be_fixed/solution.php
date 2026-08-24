<?php
// LeetCode 3119 - Maximum Number of Potholes That Can Be Fixed
// https://leetcode.com/problems/maximum-number-of-potholes-that-can-be-fixed/

class Solution {
    function maxPotholes($road, $budget) {
        $road = $road . ".";
        $n = strlen($road);
        $cnt = array_fill(0, $n, 0);
        $k = 0;
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            $c = $road[$i];
            if ($c === "x") $k++;
            else if ($k > 0) { $cnt[$k]++; $k = 0; }
        }
        for ($k = $n - 1; $k > 0 && $budget > 0; $k--) {
            $t = min(intdiv($budget, $k + 1), $cnt[$k]);
            $ans += $t * $k;
            $budget -= $t * ($k + 1);
            $cnt[$k - 1] += $cnt[$k] - $t;
        }
        return $ans;
    }
}
