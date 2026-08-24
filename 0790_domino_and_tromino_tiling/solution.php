<?php
// LeetCode 0790 - Domino and Tromino Tiling
// https://leetcode.com/problems/domino-and-tromino-tiling/

class Solution {
    /**
     * @param Integer $n
     * @return Integer
     */
    function numTilings($n) {
        $MOD = 1000000007;
        if ($n === 1) return 1;
        if ($n === 2) return 2;
        $dp = array_fill(0, $n + 1, 0);
        $dp[1] = 1;
        $dp[2] = 2;
        $dp[3] = 5;
        for ($i = 4; $i <= $n; $i++) $dp[$i] = (2 * $dp[$i - 1] + $dp[$i - 3]) % $MOD;
        return $dp[$n];
    }
}
