<?php
// LeetCode 2484 - Count Palindromic Subsequences
// https://leetcode.com/problems/count-palindromic-subsequences/

class Solution {
    function countPalindromes($s) {
        $mod = 1000000007;
        $n = strlen($s);
        $pref = [];
        $suf = [];
        for ($i = 0; $i < $n; $i++) {
            $row = [];
            for ($a = 0; $a < 10; $a++) $row[] = array_fill(0, 10, 0);
            $pref[] = $row;
            $row2 = [];
            for ($a = 0; $a < 10; $a++) $row2[] = array_fill(0, 10, 0);
            $suf[] = $row2;
        }
        $cnt = array_fill(0, 10, 0);
        for ($i = 0; $i < $n; $i++) {
            if ($i > 0) {
                for ($a = 0; $a < 10; $a++)
                    for ($b = 0; $b < 10; $b++) $pref[$i][$a][$b] = $pref[$i - 1][$a][$b];
            }
            $d = ord($s[$i]) - 48;
            for ($a = 0; $a < 10; $a++) $pref[$i][$a][$d] += $cnt[$a];
            $cnt[$d]++;
        }
        $cnt = array_fill(0, 10, 0);
        for ($i = $n - 1; $i >= 0; $i--) {
            if ($i + 1 < $n) {
                for ($a = 0; $a < 10; $a++)
                    for ($b = 0; $b < 10; $b++) $suf[$i][$a][$b] = $suf[$i + 1][$a][$b];
            }
            $d = ord($s[$i]) - 48;
            for ($a = 0; $a < 10; $a++) $suf[$i][$a][$d] += $cnt[$a];
            $cnt[$d]++;
        }
        $ans = 0;
        for ($i = 2; $i < $n - 2; $i++) {
            for ($a = 0; $a < 10; $a++) {
                for ($b = 0; $b < 10; $b++) {
                    $ans = ($ans + $pref[$i - 1][$a][$b] * $suf[$i + 1][$a][$b]) % $mod;
                }
            }
        }
        return $ans;
    }
}
