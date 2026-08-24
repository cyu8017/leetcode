<?php
// LeetCode 3563 - Lexicographically Smallest String After Adjacent Removals
// https://leetcode.com/problems/lexicographically-smallest-string-after-adjacent-removals/

class Solution {
    private function isConsec($a, $b) {
        $d = abs(ord($a) - ord($b));
        return $d === 1 || $d === 25;
    }

    function lexicographicallySmallestString($s) {
        $n = strlen($s);
        $dp = [];
        for ($i = 0; $i <= $n; $i++) $dp[$i] = array_fill(0, $n + 1, '');
        for ($length = 1; $length <= $n; $length++) {
            for ($i = 0; $i + $length <= $n; $i++) {
                $j = $i + $length;
                $minStr = $s[$i] . $dp[$i + 1][$j];
                for ($k = $i + 1; $k < $j; $k++) {
                    if ($this->isConsec($s[$i], $s[$k]) && $dp[$i + 1][$k] === '') {
                        $cand = $dp[$k + 1][$j];
                        if ($cand < $minStr) $minStr = $cand;
                    }
                }
                $dp[$i][$j] = $minStr;
            }
        }
        return $dp[0][$n];
    }
}
