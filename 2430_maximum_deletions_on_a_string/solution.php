<?php
// LeetCode 2430 - Maximum Deletions on a String
// https://leetcode.com/problems/maximum-deletions-on-a-string/

class Solution {
    function deleteString($s) {
        $n = strlen($s);
        $lcp = [];
        for ($i = 0; $i <= $n; $i++) $lcp[] = array_fill(0, $n + 1, 0);
        for ($i = $n - 1; $i >= 0; $i--) {
            for ($j = $n - 1; $j >= 0; $j--) {
                if ($s[$i] === $s[$j]) $lcp[$i][$j] = $lcp[$i + 1][$j + 1] + 1;
            }
        }
        $dp = array_fill(0, $n, 0);
        for ($i = $n - 1; $i >= 0; $i--) {
            $dp[$i] = 1;
            for ($len = 1; $i + 2 * $len <= $n; $len++) {
                if ($lcp[$i][$i + $len] >= $len) $dp[$i] = max($dp[$i], 1 + $dp[$i + $len]);
            }
        }
        return $dp[0];
    }
}
