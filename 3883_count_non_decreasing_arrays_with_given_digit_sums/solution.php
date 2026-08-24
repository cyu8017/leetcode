<?php
// LeetCode 3883 - Count Non Decreasing Arrays With Given Digit Sums
// https://leetcode.com/problems/count-non-decreasing-arrays-with-given-digit-sums/

class Solution {
    function countNonDecreasingArrays($digitSum) {
        $mod = 1000000007;
        $groups = [];
        for ($i = 0; $i <= 50; $i++) $groups[$i] = [];
        for ($x = 0; $x <= 5000; $x++) {
            $s = 0;
            for ($y = $x; $y > 0; $y = intdiv($y, 10)) $s += $y % 10;
            $groups[$s][] = $x;
        }
        $prevVals = $groups[$digitSum[0]];
        $dp = array_fill(0, count($prevVals), 1);
        $len = count($digitSum);
        for ($pos = 1; $pos < $len; $pos++) {
            $curVals = $groups[$digitSum[$pos]];
            $next = array_fill(0, count($curVals), 0);
            $j = 0;
            $prefix = 0;
            $cn = count($curVals);
            $pn = count($prevVals);
            for ($i = 0; $i < $cn; $i++) {
                $x = $curVals[$i];
                while ($j < $pn && $prevVals[$j] <= $x) {
                    $prefix += $dp[$j];
                    if ($prefix >= $mod) $prefix -= $mod;
                    $j++;
                }
                $next[$i] = $prefix;
            }
            $prevVals = $curVals;
            $dp = $next;
        }
        $ans = 0;
        foreach ($dp as $x) {
            $ans += $x;
            if ($ans >= $mod) $ans -= $mod;
        }
        return $ans;
    }
}
