<?php
// LeetCode 2967 - Minimum Cost to Make Array Equalindromic
// https://leetcode.com/problems/minimum-cost-to-make-array-equalindromic/

class Solution {
    private function makePal($x) {
        $ch = str_split((string)$x);
        for ($i = 0, $j = count($ch) - 1; $i < $j; $i++, $j--) $ch[$j] = $ch[$i];
        return (int)implode('', $ch);
    }

    private function costOf($nums, $p) {
        $c = 0;
        foreach ($nums as $v) $c += abs($v - $p);
        return $c;
    }

    function minimumCost($nums) {
        sort($nums);
        $n = count($nums);
        $median = $nums[intdiv($n, 2)];
        $candidates = [$this->makePal($median)];
        $s = (string)$median;
        $half = (int)substr($s, 0, intdiv(strlen($s) + 1, 2));
        for ($d = -2; $d <= 2; $d++) {
            $h = $half + $d;
            if ($h <= 0) continue;
            $hs = (string)$h;
            if (strlen($s) % 2 === 0) {
                $pal = $hs . strrev($hs);
            } else {
                $prefix = substr($hs, 0, strlen($hs) - 1);
                $pal = $hs . strrev($prefix);
            }
            $parsed = (int)$pal;
            $candidates[] = $parsed;
        }
        foreach ([1, 9, 11, 99, 101] as $v) $candidates[] = $v;
        $ans = PHP_INT_MAX / 4;
        foreach ($candidates as $p) {
            if ($p <= 0) continue;
            $ans = min($ans, $this->costOf($nums, $p));
        }
        return $ans;
    }
}
