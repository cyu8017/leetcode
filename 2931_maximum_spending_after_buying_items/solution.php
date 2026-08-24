<?php
// LeetCode 2931 - Maximum Spending After Buying Items
// https://leetcode.com/problems/maximum-spending-after-buying-items/

class Solution {
    function maxSpending($values) {
        $m = count($values);
        $n = count($values[0]);
        $idx = array_fill(0, $m, $n - 1);
        $ans = 0;
        $day = 1;
        $total = $m * $n;
        for ($t = 0; $t < $total; $t++) {
            $bestI = -1;
            $bestV = PHP_INT_MAX;
            for ($i = 0; $i < $m; $i++) {
                if ($idx[$i] >= 0 && $values[$i][$idx[$i]] < $bestV) {
                    $bestV = $values[$i][$idx[$i]];
                    $bestI = $i;
                }
            }
            $ans += $bestV * $day;
            $idx[$bestI]--;
            $day++;
        }
        return $ans;
    }
}
