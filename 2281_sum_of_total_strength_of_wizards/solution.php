<?php
// LeetCode 2281 - Sum of Total Strength of Wizards
// https://leetcode.com/problems/sum-of-total-strength-of-wizards/

class Solution {
    function totalStrength($strength) {
        $mod = 1000000007;
        $n = count($strength);
        $left = array_fill(0, $n, 0);
        $right = array_fill(0, $n, 0);
        $stack = [];
        for ($i = 0; $i < $n; $i++) {
            while (count($stack) && $strength[$stack[count($stack) - 1]] >= $strength[$i]) array_pop($stack);
            $left[$i] = count($stack) ? $stack[count($stack) - 1] : -1;
            $stack[] = $i;
        }
        $stack = [];
        for ($i = $n - 1; $i >= 0; $i--) {
            while (count($stack) && $strength[$stack[count($stack) - 1]] > $strength[$i]) array_pop($stack);
            $right[$i] = count($stack) ? $stack[count($stack) - 1] : $n;
            $stack[] = $i;
        }
        $pref = array_fill(0, $n + 1, 0);
        $prefPref = array_fill(0, $n + 2, 0);
        for ($i = 0; $i < $n; $i++) $pref[$i + 1] = ($pref[$i] + $strength[$i]) % $mod;
        for ($i = 0; $i <= $n; $i++) $prefPref[$i + 1] = ($prefPref[$i] + $pref[$i]) % $mod;
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            $l = $left[$i] + 1;
            $r = $right[$i] - 1;
            $leftSum = ($prefPref[$i + 1] - $prefPref[$l] + $mod) % $mod;
            $rightSum = ($prefPref[$r + 2] - $prefPref[$i + 1] + $mod) % $mod;
            $leftCnt = $i - $l + 1;
            $rightCnt = $r - $i + 1;
            $contrib = ($leftCnt * $rightSum - $rightCnt * $leftSum) % $mod;
            if ($contrib < 0) $contrib += $mod;
            $ans = ($ans + $contrib * $strength[$i] % $mod) % $mod;
        }
        return $ans;
    }
}
