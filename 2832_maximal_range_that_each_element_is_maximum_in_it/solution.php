<?php
// LeetCode 2832 - Maximal Range That Each Element Is Maximum in It
// https://leetcode.com/problems/maximal-range-that-each-element-is-maximum-in-it/

class Solution {
    function maximumLength($nums) {
        $n = count($nums);
        $left = array_fill(0, $n, 0);
        $right = array_fill(0, $n, 0);
        $st = [];
        for ($i = 0; $i < $n; $i++) {
            while (count($st) && $nums[$st[count($st) - 1]] < $nums[$i]) array_pop($st);
            $left[$i] = count($st) ? $st[count($st) - 1] : -1;
            $st[] = $i;
        }
        $st = [];
        for ($i = $n - 1; $i >= 0; $i--) {
            while (count($st) && $nums[$st[count($st) - 1]] <= $nums[$i]) array_pop($st);
            $right[$i] = count($st) ? $st[count($st) - 1] : $n;
            $st[] = $i;
        }
        $ans = array_fill(0, $n, 0);
        for ($i = 0; $i < $n; $i++) $ans[$i] = $right[$i] - $left[$i] - 1;
        return $ans;
    }
}
