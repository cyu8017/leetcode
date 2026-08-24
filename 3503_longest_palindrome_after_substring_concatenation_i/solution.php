<?php
// LeetCode 3503 - Longest Palindrome After Substring Concatenation I
// https://leetcode.com/problems/longest-palindrome-after-substring-concatenation-i/

class Solution {
    private function expand($str, &$g, $l, $r) {
        $n = strlen($str);
        while ($l >= 0 && $r < $n && $str[$l] === $str[$r]) {
            $g[$l] = max($g[$l], $r - $l + 1);
            $l--;
            $r++;
        }
    }

    private function calc($str) {
        $n = strlen($str);
        $g = array_fill(0, $n, 0);
        for ($i = 0; $i < $n; $i++) {
            $this->expand($str, $g, $i, $i);
            $this->expand($str, $g, $i, $i + 1);
        }
        return $g;
    }

    function longestPalindrome($s, $t) {
        $m = strlen($s);
        $n = strlen($t);
        $t = strrev($t);
        $g1 = $this->calc($s);
        $g2 = $this->calc($t);
        $ans = 0;
        foreach ($g1 as $v) $ans = max($ans, $v);
        foreach ($g2 as $v) $ans = max($ans, $v);
        $f = [];
        for ($i = 0; $i <= $m; $i++) $f[$i] = array_fill(0, $n + 1, 0);
        for ($i = 1; $i <= $m; $i++) {
            for ($j = 1; $j <= $n; $j++) {
                if ($s[$i - 1] === $t[$j - 1]) {
                    $f[$i][$j] = $f[$i - 1][$j - 1] + 1;
                    $a = $i < $m ? $g1[$i] : 0;
                    $b = $j < $n ? $g2[$j] : 0;
                    $ans = max($ans, $f[$i][$j] * 2 + $a);
                    $ans = max($ans, $f[$i][$j] * 2 + $b);
                }
            }
        }
        return $ans;
    }
}
