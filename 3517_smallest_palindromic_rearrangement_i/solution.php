<?php
// LeetCode 3517 - Smallest Palindromic Rearrangement I
// https://leetcode.com/problems/smallest-palindromic-rearrangement-i/

class Solution {
    function smallestPalindrome($s) {
        $cnt = array_fill(0, 26, 0);
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) $cnt[ord($s[$i]) - 97]++;
        $t = '';
        $ch = '';
        for ($i = 0; $i < 26; $i++) {
            $c = chr(97 + $i);
            $v = intdiv($cnt[$i], 2);
            $t .= str_repeat($c, $v);
            $cnt[$i] -= $v * 2;
            if ($cnt[$i] === 1) $ch = $c;
        }
        $sb = $t;
        if ($ch !== '') $sb .= $ch;
        for ($i = strlen($t) - 1; $i >= 0; $i--) $sb .= $t[$i];
        return $sb;
    }
}
