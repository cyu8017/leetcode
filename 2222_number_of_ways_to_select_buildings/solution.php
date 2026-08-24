<?php
// LeetCode 2222 - Number of Ways to Select Buildings
// https://leetcode.com/problems/number-of-ways-to-select-buildings/

class Solution {
    function numberOfWays($s) {
        $total0 = 0;
        $total1 = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            if ($s[$i] === '0') $total0++;
            else $total1++;
        }
        $left0 = 0;
        $left1 = 0;
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            if ($s[$i] === '0') {
                $ans += $left1 * ($total1 - $left1);
                $left0++;
            } else {
                $ans += $left0 * ($total0 - $left0);
                $left1++;
            }
        }
        return $ans;
    }
}
