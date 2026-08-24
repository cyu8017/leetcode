<?php
// LeetCode 3677 - Count Binary Palindromic Numbers
// https://leetcode.com/problems/count-binary-palindromic-numbers/

class Solution {
    function countBinaryPalindromes($n) {
        if ($n === 0) return 1;
        $ans = 1;
        $s = '';
        for ($x = $n; $x > 0; $x = intdiv($x, 2)) $s .= (string)($x & 1);
        $s = strrev($s);
        $L = strlen($s);
        for ($len = 1; $len < $L; $len++) {
            $half = intdiv($len + 1, 2);
            $ans += 1 << ($half - 1);
        }
        $half = intdiv($L + 1, 2);
        $prefix = substr($s, 0, $half);
        $start = 1 << ($half - 1);
        $prefVal = 0;
        $pn = strlen($prefix);
        for ($i = 0; $i < $pn; $i++) $prefVal = ($prefVal << 1) | (ord($prefix[$i]) - 48);
        $ans += $prefVal - $start;
        $pal = $prefix;
        for ($i = $half - 1 - ($L % 2); $i >= 0; $i--) $pal .= $prefix[$i];
        $pval = 0;
        $pl = strlen($pal);
        for ($i = 0; $i < $pl; $i++) $pval = ($pval << 1) | (ord($pal[$i]) - 48);
        if ($pval <= $n) $ans++;
        return $ans;
    }
}
