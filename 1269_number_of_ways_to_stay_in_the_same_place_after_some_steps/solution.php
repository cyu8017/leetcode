<?php
// LeetCode 1269 - Number of Ways to Stay in the Same Place After Some Steps
// https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/

class Solution {
    /**
     * @param Integer $steps
     * @param Integer $arrLen
     * @return Integer
     */
    function numWays($steps, $arrLen) {
        $mod = 1000000007;
        $width = min($arrLen, intdiv($steps, 2) + 1);
        $dp = array_fill(0, $width, 0);
        $dp[0] = 1;
        for ($s = 0; $s < $steps; $s++) {
            $nxt = array_fill(0, $width, 0);
            for ($i = 0; $i < $width; $i++) {
                $nxt[$i] = $dp[$i];
                if ($i > 0) $nxt[$i] = ($nxt[$i] + $dp[$i - 1]) % $mod;
                if ($i + 1 < $width) $nxt[$i] = ($nxt[$i] + $dp[$i + 1]) % $mod;
            }
            $dp = $nxt;
        }
        return $dp[0];
    }
}
