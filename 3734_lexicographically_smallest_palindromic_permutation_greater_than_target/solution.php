<?php
// LeetCode 3734 - Lexicographically Smallest Palindromic Permutation Greater Than Target
// https://leetcode.com/problems/lexicographically-smallest-palindromic-permutation-greater-than-target/

class Solution {
    function lexPalindromicPermutation($s, $target) {
        $cnt = array_fill(0, 26, 0);
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) $cnt[ord($s[$i]) - 97]++;
        $odd = 0;
        $mid = -1;
        for ($i = 0; $i < 26; $i++) {
            if ($cnt[$i] % 2 === 1) { $odd++; $mid = $i; }
        }
        if ($odd > 1) return "";
        $half = array_fill(0, 26, 0);
        for ($i = 0; $i < 26; $i++) $half[$i] = intdiv($cnt[$i], 2);
        $halfLen = intdiv($n, 2);
        $left = array_fill(0, $halfLen, '');
        $dfs = function($pos, $greater) use (&$dfs, &$half, &$left, $halfLen, $mid, $target) {
            if ($pos === $halfLen) {
                if ($mid >= 0) {
                    if ($greater) return true;
                    return chr(97 + $mid) > $target[$halfLen];
                }
                return $greater;
            }
            $start = $greater ? 0 : (ord($target[$pos]) - 97);
            for ($c = $start; $c < 26; $c++) {
                if ($half[$c] === 0) continue;
                $half[$c]--;
                $left[$pos] = chr(97 + $c);
                if ($dfs($pos + 1, $greater || $c > (ord($target[$pos]) - 97))) return true;
                $half[$c]++;
            }
            return false;
        };
        if (!$dfs(0, false)) return "";
        $res = implode('', $left);
        if ($mid >= 0) $res .= chr(97 + $mid);
        for ($i = $halfLen - 1; $i >= 0; $i--) $res .= $left[$i];
        if ($res <= $target) return "";
        return $res;
    }
}
