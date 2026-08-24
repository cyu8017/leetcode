<?php
// LeetCode 2384 - Largest Palindromic Number
// https://leetcode.com/problems/largest-palindromic-number/

class Solution {
    function largestPalindromic($num) {
        $freq = array_fill(0, 10, 0);
        $n = strlen($num);
        for ($i = 0; $i < $n; $i++) $freq[ord($num[$i]) - 48]++;
        $left = '';
        for ($d = 9; $d >= 0; $d--) {
            $pairs = intdiv($freq[$d], 2);
            $left .= str_repeat(strval($d), $pairs);
            $freq[$d] %= 2;
        }
        $mid = '';
        for ($d = 9; $d >= 0; $d--) {
            if ($freq[$d] > 0) { $mid = strval($d); break; }
        }
        if ($left === '') return $mid === '' ? '0' : $mid;
        if ($left[0] === '0') return $mid === '' ? '0' : $mid;
        return $left . $mid . strrev($left);
    }
}
