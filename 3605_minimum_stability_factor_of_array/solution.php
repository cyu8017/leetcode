<?php
// LeetCode 3605 - Minimum Stability Factor of Array
// https://leetcode.com/problems/minimum-stability-factor-of-array/

class Solution {
    private function gcd($a, $b) {
        while ($b !== 0) { $t = $a % $b; $a = $b; $b = $t; }
        return $a;
    }

    private function ok($nums, $maxC, $x) {
        $n = count($nums);
        if ($x >= $n) return true;
        $changes = 0;
        $i = 0;
        while ($i + $x < $n) {
            $g = $nums[$i];
            for ($j = $i + 1; $j <= $i + $x; $j++) $g = $this->gcd($g, $nums[$j]);
            if ($g > 1) {
                $changes++;
                $i += $x + 1;
            } else {
                $i++;
            }
        }
        return $changes <= $maxC;
    }

    function minStable($nums, $maxC) {
        $n = count($nums);
        $lo = 0;
        $hi = $n;
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi, 2);
            if ($this->ok($nums, $maxC, $mid)) $hi = $mid;
            else $lo = $mid + 1;
        }
        return $lo;
    }
}
