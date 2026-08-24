<?php
// LeetCode 0907 - Sum of Subarray Minimums
// https://leetcode.com/problems/sum-of-subarray-minimums/

class Solution {
    function sumSubarrayMins($arr) {
        $MOD = 1000000007;
        $n = count($arr);
        $left = array_fill(0, $n, -1);
        $right = array_fill(0, $n, $n);
        $st = [];
        for ($i = 0; $i < $n; $i++) {
            while ($st && $arr[$st[count($st) - 1]] > $arr[$i]) array_pop($st);
            $left[$i] = $st ? $st[count($st) - 1] : -1;
            $st[] = $i;
        }
        $st = [];
        for ($i = $n - 1; $i >= 0; $i--) {
            while ($st && $arr[$st[count($st) - 1]] >= $arr[$i]) array_pop($st);
            $right[$i] = $st ? $st[count($st) - 1] : $n;
            $st[] = $i;
        }
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            $ans = ($ans + $arr[$i] * ($i - $left[$i]) * ($right[$i] - $i)) % $MOD;
        }
        return $ans;
    }
}
