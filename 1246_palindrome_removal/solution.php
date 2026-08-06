<?php
// LeetCode 1246 - Palindrome Removal
// https://leetcode.com/problems/palindrome-removal/

class Solution {
    /**
     * @param Integer[] $arr
     * @return Integer
     */
    function minimumMoves($arr) {
        $n = count($arr);
        $dp = array_fill(0, $n, array_fill(0, $n, 0));
        for ($i = 0; $i < $n; $i++) $dp[$i][$i] = 1;
        for ($length = 2; $length <= $n; $length++) {
            for ($i = 0; $i <= $n - $length; $i++) {
                $j = $i + $length - 1;
                $dp[$i][$j] = 1 + $dp[$i + 1][$j];
                if ($arr[$i] === $arr[$i + 1]) {
                    $dp[$i][$j] = min($dp[$i][$j], 1 + ($i + 2 <= $j ? $dp[$i + 2][$j] : 0));
                }
                for ($k = $i + 2; $k <= $j; $k++) {
                    if ($arr[$i] === $arr[$k]) {
                        $dp[$i][$j] = min($dp[$i][$j], $dp[$i + 1][$k - 1] + ($k < $j ? $dp[$k + 1][$j] : 0));
                    }
                }
            }
        }
        return $dp[0][$n - 1];
    }
}
