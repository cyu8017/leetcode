<?php
// LeetCode 2028 - Find Missing Observations
// https://leetcode.com/problems/find-missing-observations/

class Solution {
    /**
     * @param Integer[] $rolls
     * @param Integer $mean
     * @param Integer $n
     * @return Integer[]
     */
    function missingRolls($rolls, $mean, $n) {
        $sum = 0;
        foreach ($rolls as $r) $sum += $r;
        $remain = $mean * (count($rolls) + $n) - $sum;
        if ($remain < $n || $remain > 6 * $n) return [];
        $ans = [];
        $baseVal = intdiv($remain, $n);
        $extra = $remain % $n;
        for ($i = 0; $i < $n; $i++) $ans[$i] = $baseVal + ($i < $extra ? 1 : 0);
        return $ans;
    }
}
