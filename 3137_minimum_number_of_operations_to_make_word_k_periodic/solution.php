<?php
// LeetCode 3137 - Minimum Number of Operations to Make Word K-Periodic
// https://leetcode.com/problems/minimum-number-of-operations-to-make-word-k-periodic/

class Solution {
    function minimumOperationsToMakeKPeriodic($word, $k) {
        $cnt = [];
        $n = strlen($word);
        $mx = 0;
        for ($i = 0; $i < $n; $i += $k) {
            $s = substr($word, $i, $k);
            $v = ($cnt[$s] ?? 0) + 1;
            $cnt[$s] = $v;
            $mx = max($mx, $v);
        }
        return intdiv($n, $k) - $mx;
    }
}
