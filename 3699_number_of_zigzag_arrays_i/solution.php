<?php
// LeetCode 3699 - Number of ZigZag Arrays I
// https://leetcode.com/problems/number-of-zigzag-arrays-i/

class Solution {
    function zigZagArrays($n, $l, $r) {
        $MOD = 1000000007;
        $m = $r - $l + 1;
        if ($n === 1) return $m % $MOD;
        $up = array_fill(0, $m, 1);
        $down = array_fill(0, $m, 1);
        for ($len_ = 2; $len_ <= $n; $len_++) {
            $prefDown = array_fill(0, $m + 1, 0);
            for ($j = 0; $j < $m; $j++) $prefDown[$j + 1] = ($prefDown[$j] + $down[$j]) % $MOD;
            $nup = [];
            for ($j = 0; $j < $m; $j++) $nup[$j] = $prefDown[$j];
            $sufUp = array_fill(0, $m + 1, 0);
            for ($j = $m - 1; $j >= 0; $j--) $sufUp[$j] = ($sufUp[$j + 1] + $up[$j]) % $MOD;
            $ndown = [];
            for ($j = 0; $j < $m; $j++) $ndown[$j] = $sufUp[$j + 1];
            $up = $nup;
            $down = $ndown;
        }
        $ans = 0;
        for ($j = 0; $j < $m; $j++) {
            $ans = ($ans + $up[$j]) % $MOD;
            $ans = ($ans + $down[$j]) % $MOD;
        }
        return $ans;
    }
}
