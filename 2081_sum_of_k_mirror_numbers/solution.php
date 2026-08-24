<?php
// LeetCode 2081 - Sum of k-Mirror Numbers
// https://leetcode.com/problems/sum-of-k-mirror-numbers/

class Solution {
    /**
     * @param Integer $k
     * @param Integer $n
     * @return Integer
     */
    function kMirror($k, $n) {
        $isPalBase = function ($x, $bas) {
            $digits = [];
            while ($x > 0) { $digits[] = $x % $bas; $x = intdiv($x, $bas); }
            for ($l = 0, $r = count($digits) - 1; $l < $r; $l++, $r--)
                if ($digits[$l] !== $digits[$r]) return false;
            return true;
        };
        $ans = 0;
        $count = 0;
        for ($length = 1; $count < $n; $length++) {
            $start = 1;
            $halfLen = intdiv($length + 1, 2);
            for ($i = 1; $i < $halfLen; $i++) $start *= 10;
            $end = $start * 10;
            for ($half = $start; $half < $end && $count < $n; $half++) {
                $pal = $half;
                if ($length % 2 === 0) {
                    $x = $half;
                    while ($x > 0) { $pal = $pal * 10 + $x % 10; $x = intdiv($x, 10); }
                } else {
                    $x = intdiv($half, 10);
                    while ($x > 0) { $pal = $pal * 10 + $x % 10; $x = intdiv($x, 10); }
                }
                if ($isPalBase($pal, $k)) { $ans += $pal; $count++; }
            }
        }
        return $ans;
    }
}
