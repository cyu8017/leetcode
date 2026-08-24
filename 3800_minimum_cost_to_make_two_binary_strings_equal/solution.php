<?php
// LeetCode 3800 - Minimum Cost to Make Two Binary Strings Equal
// https://leetcode.com/problems/minimum-cost-to-make-two-binary-strings-equal/

class Solution {
    function minimumCost($s, $t, $flipCost, $swapCost, $crossCost) {
        $diff = [0, 0];
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            if ($s[$i] !== $t[$i]) $diff[ord($s[$i]) - 48]++;
        }
        $ans = ($diff[0] + $diff[1]) * $flipCost;
        $mx = max($diff[0], $diff[1]);
        $mn = min($diff[0], $diff[1]);
        $ans = min($ans, $mn * $swapCost + ($mx - $mn) * $flipCost);
        $avg = intdiv($mx + $mn, 2);
        $ans = min($ans, ($avg - $mn) * $crossCost + $avg * $swapCost + ($mx + $mn - $avg * 2) * $flipCost);
        return $ans;
    }
}
