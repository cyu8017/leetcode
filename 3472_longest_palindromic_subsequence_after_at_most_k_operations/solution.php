<?php
// LeetCode 3472 - Longest Palindromic Subsequence After at Most K Operations
// https://leetcode.com/problems/longest-palindromic-subsequence-after-at-most-k-operations/

class Solution {
    private function distCirc($a, $b) {
        $d = abs(ord($a) - ord($b));
        return min($d, 26 - $d);
    }

    function longestPalindromicSubsequence($s, $k) {
        $n = strlen($s);
        $dp = [];
        for ($i = 0; $i < $n; $i++) {
            $dp[$i] = [];
            for ($j = 0; $j < $n; $j++) $dp[$i][$j] = array_fill(0, $k + 1, -1);
        }
        $dfs = null;
        $dfs = function($i, $j, $ops) use (&$dfs, $s, &$dp) {
            if ($i > $j) return 0;
            if ($i === $j) return 1;
            if ($dp[$i][$j][$ops] !== -1) return $dp[$i][$j][$ops];
            $best = $dfs($i + 1, $j, $ops);
            $best = max($best, $dfs($i, $j - 1, $ops));
            $cost = $this->distCirc($s[$i], $s[$j]);
            if ($cost <= $ops) $best = max($best, 2 + $dfs($i + 1, $j - 1, $ops - $cost));
            return $dp[$i][$j][$ops] = $best;
        };
        return $dfs(0, $n - 1, $k);
    }
}
