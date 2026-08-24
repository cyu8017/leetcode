<?php
// LeetCode 3261 - Count Substrings That Satisfy K-Constraint II
// https://leetcode.com/problems/count-substrings-that-satisfy-k-constraint-ii/

class Solution {
    function countKConstraintSubstrings($s, $k, $queries) {
        $n = strlen($s);
        $leftMost = array_fill(0, $n, 0);
        $z = 0;
        $o = 0;
        $L = 0;
        for ($R = 0; $R < $n; $R++) {
            if ($s[$R] === '0') $z++; else $o++;
            while ($z > $k && $o > $k) {
                if ($s[$L] === '0') $z--; else $o--;
                $L++;
            }
            $leftMost[$R] = $L;
        }
        $pref = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; $i++) $pref[$i + 1] = $pref[$i] + ($i - $leftMost[$i] + 1);
        $ans = array_fill(0, count($queries), 0);
        for ($qi = 0; $qi < count($queries); $qi++) {
            $l = $queries[$qi][0];
            $r = $queries[$qi][1];
            $lo = $l;
            $hi = $r + 1;
            while ($lo < $hi) {
                $mid = ($lo + $hi) >> 1;
                if ($leftMost[$mid] < $l) $lo = $mid + 1;
                else $hi = $mid;
            }
            $res = 0;
            if ($lo > $l) {
                $m = $lo - $l;
                $res += intdiv($m * ($m + 1), 2);
            }
            if ($lo <= $r) $res += $pref[$r + 1] - $pref[$lo];
            $ans[$qi] = $res;
        }
        return $ans;
    }
}
