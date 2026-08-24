<?php
// LeetCode 3035 - Maximum Palindromes After Operations
// https://leetcode.com/problems/maximum-palindromes-after-operations/

class Solution {
    private function popcount($x) {
        $c = 0;
        while ($x !== 0) { $c += $x & 1; $x >>= 1; }
        return $c;
    }

    function maxPalindromesAfterOperations($words) {
        $s = 0;
        $mask = 0;
        foreach ($words as $w) {
            $s += strlen($w);
            for ($i = 0; $i < strlen($w); $i++) $mask ^= 1 << (ord($w[$i]) - 97);
        }
        $s -= $this->popcount($mask);
        usort($words, function($a, $b) { return strlen($a) <=> strlen($b); });
        $ans = 0;
        foreach ($words as $w) {
            $s -= intdiv(strlen($w), 2) * 2;
            if ($s < 0) break;
            $ans++;
        }
        return $ans;
    }
}
