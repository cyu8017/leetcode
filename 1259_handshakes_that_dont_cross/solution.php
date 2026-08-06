<?php
// LeetCode 1259 - Handshakes That Don't Cross
// https://leetcode.com/problems/handshakes-that-dont-cross/

class Solution {
    /**
     * @param Integer $numPeople
     * @return Integer
     */
    function numberOfWays($numPeople) {
        $mod = 1000000007;
        $dp = array_fill(0, $numPeople + 1, 0);
        $dp[0] = 1;
        for ($people = 2; $people <= $numPeople; $people += 2) {
            $sum = 0;
            for ($left = 0; $left < $people; $left += 2) {
                $sum = ($sum + $dp[$left] * $dp[$people - 2 - $left]) % $mod;
            }
            $dp[$people] = $sum;
        }
        return $dp[$numPeople];
    }
}
