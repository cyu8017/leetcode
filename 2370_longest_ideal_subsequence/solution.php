<?php
// LeetCode 2370 - Longest Ideal Subsequence
// https://leetcode.com/problems/longest-ideal-subsequence/

class Solution {
    function longestIdealString($s, $k) {
        $dp = array_fill(0, 26, 0);
        $ans = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $c = ord($s[$i]) - 97;
            $best = 0;
            for ($p = 0; $p < 26; $p++)
                if (abs($c - $p) <= $k && $dp[$p] > $best) $best = $dp[$p];
            $dp[$c] = $best + 1;
            $ans = max($ans, $dp[$c]);
        }
        return $ans;
    }
}
