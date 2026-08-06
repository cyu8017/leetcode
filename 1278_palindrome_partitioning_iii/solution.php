<?php
// LeetCode 1278 - Palindrome Partitioning III
// https://leetcode.com/problems/palindrome-partitioning-iii/

class Solution {
    /**
     * @param String $s
     * @param Integer $k
     * @return Integer
     */
    function palindromePartition($s, $k) {
        $n = strlen($s);
        $cost = array_fill(0, $n, array_fill(0, $n, 0));
        for ($length = 2; $length <= $n; $length++) {
            for ($i = 0; $i <= $n - $length; $i++) {
                $j = $i + $length - 1;
                $cost[$i][$j] = ($length > 2 ? $cost[$i + 1][$j - 1] : 0) + ($s[$i] !== $s[$j] ? 1 : 0);
            }
        }
        $inf = $n + 1;
        $dp = array_fill(0, $k + 1, array_fill(0, $n + 1, $inf));
        $dp[0][0] = 0;
        for ($parts = 1; $parts <= $k; $parts++) {
            for ($end = $parts; $end <= $n; $end++) {
                for ($start = $parts - 1; $start < $end; $start++) {
                    $dp[$parts][$end] = min($dp[$parts][$end], $dp[$parts - 1][$start] + $cost[$start][$end - 1]);
                }
            }
        }
        return $dp[$k][$n];
    }
}
