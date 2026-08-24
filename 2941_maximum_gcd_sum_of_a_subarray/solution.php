<?php
// LeetCode 2941 - Maximum GCD-Sum of a Subarray
// https://leetcode.com/problems/maximum-gcd-sum-of-a-subarray/

class Solution {
    function maxGcdSum($nums, $k) {
        $gcd = function($a, $b) {
            while ($b !== 0) { $t = $a % $b; $a = $b; $b = $t; }
            return $a;
        };
        $n = count($nums);
        $pref = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; $i++) $pref[$i + 1] = $pref[$i] + $nums[$i];
        $ans = 0;
        $st = [];
        for ($i = 0; $i < $n; $i++) {
            $nst = [[$nums[$i], $i]];
            foreach ($st as $p) {
                $g = $gcd($p[0], $nums[$i]);
                if ($nst[count($nst) - 1][0] === $g) continue;
                $nst[] = [$g, $p[1]];
            }
            $st = $nst;
            foreach ($st as $p) {
                $g = $p[0];
                $idx = $p[1];
                if ($i - $idx + 1 >= $k) {
                    $cand = ($pref[$i + 1] - $pref[$idx]) * $g;
                    if ($cand > $ans) $ans = $cand;
                }
            }
        }
        return $ans;
    }
}
