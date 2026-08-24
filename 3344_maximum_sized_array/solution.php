<?php
// LeetCode 3344 - Maximum Sized Array
// https://leetcode.com/problems/maximum-sized-array/

class Solution {
    function ok($n, $s) {
        $sum = 0;
        for ($i = 0; $i < $n; $i++) {
            for ($j = 0; $j < $n; $j++) {
                $ij = $i | $j;
                $sum += $ij * ($n - 1) * $n / 2;
                if ($sum > $s) return false;
            }
        }
        return $sum <= $s;
    }

    function maxSizedArray($s) {
        $lo = 1;
        $hi = 2000;
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi + 1, 2);
            if ($this->ok($mid, $s)) $lo = $mid;
            else $hi = $mid - 1;
        }
        return $lo;
    }
}
