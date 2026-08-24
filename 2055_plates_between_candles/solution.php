<?php
// LeetCode 2055 - Plates Between Candles
// https://leetcode.com/problems/plates-between-candles/

class Solution {
    /**
     * @param String $s
     * @param Integer[][] $queries
     * @return Integer[]
     */
    function platesBetweenCandles($s, $queries) {
        $n = strlen($s);
        $pref = array_fill(0, $n + 1, 0);
        $left = array_fill(0, $n, -1);
        $right = array_fill(0, $n, -1);
        $last = -1;
        for ($i = 0; $i < $n; $i++) {
            $pref[$i + 1] = $pref[$i] + ($s[$i] === '*' ? 1 : 0);
            if ($s[$i] === '|') $last = $i;
            $left[$i] = $last;
        }
        $last = -1;
        for ($i = $n - 1; $i >= 0; $i--) {
            if ($s[$i] === '|') $last = $i;
            $right[$i] = $last;
        }
        $ans = [];
        foreach ($queries as $i => $q) {
            $l = $right[$q[0]];
            $r = $left[$q[1]];
            if ($l !== -1 && $r !== -1 && $l < $r) $ans[$i] = $pref[$r] - $pref[$l];
            else $ans[$i] = 0;
        }
        return $ans;
    }
}
