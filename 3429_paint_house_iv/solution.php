<?php
// LeetCode 3429 - Paint House IV
// https://leetcode.com/problems/paint-house-iv/

class Solution {
    function minCost($n, $cost) {
        $inf = intdiv(PHP_INT_MAX, 4);
        $m = intdiv($n, 2);
        $dp = [];
        for ($a = 0; $a < 3; $a++) {
            $dp[$a] = [];
            for ($b = 0; $b < 3; $b++) {
                $dp[$a][$b] = ($a === $b) ? $inf : $cost[0][$a] + $cost[$n - 1][$b];
            }
        }
        for ($i = 1; $i < $m; $i++) {
            $ndp = [];
            for ($a = 0; $a < 3; $a++) $ndp[$a] = array_fill(0, 3, $inf);
            for ($pa = 0; $pa < 3; $pa++) {
                for ($pb = 0; $pb < 3; $pb++) {
                    if ($dp[$pa][$pb] >= $inf) continue;
                    for ($a = 0; $a < 3; $a++) {
                        if ($a === $pa) continue;
                        for ($b = 0; $b < 3; $b++) {
                            if ($b === $pb || $a === $b) continue;
                            $v = $dp[$pa][$pb] + $cost[$i][$a] + $cost[$n - 1 - $i][$b];
                            if ($v < $ndp[$a][$b]) $ndp[$a][$b] = $v;
                        }
                    }
                }
            }
            $dp = $ndp;
        }
        $ans = $inf;
        for ($a = 0; $a < 3; $a++)
            for ($b = 0; $b < 3; $b++)
                if ($dp[$a][$b] < $ans) $ans = $dp[$a][$b];
        return $ans;
    }
}
