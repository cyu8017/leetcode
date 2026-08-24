<?php
// LeetCode 3218 - Minimum Cost for Cutting Cake I
// https://leetcode.com/problems/minimum-cost-for-cutting-cake-i/

class Solution {
    function minimumCost($m, $n, $horizontalCut, $verticalCut) {
        rsort($horizontalCut);
        rsort($verticalCut);
        $i = 0;
        $j = 0;
        $h = 1;
        $v = 1;
        $ans = 0;
        while ($i < $m - 1 || $j < $n - 1) {
            if ($j === $n - 1 || ($i < $m - 1 && $horizontalCut[$i] > $verticalCut[$j])) {
                $ans += $horizontalCut[$i] * $v;
                $h++;
                $i++;
            } else {
                $ans += $verticalCut[$j] * $h;
                $v++;
                $j++;
            }
        }
        return $ans;
    }
}
