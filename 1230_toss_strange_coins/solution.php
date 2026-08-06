<?php
// LeetCode 1230 - Toss Strange Coins
// https://leetcode.com/problems/toss-strange-coins/

class Solution {
    /**
     * @param Float[] $prob
     * @param Integer $target
     * @return Float
     */
    function probabilityOfHeads($prob, $target) {
        $dp = array_fill(0, $target + 1, 0.0);
        $dp[0] = 1.0;
        foreach ($prob as $p) {
            for ($heads = $target; $heads >= 0; $heads--) {
                $dp[$heads] = $dp[$heads] * (1 - $p) + ($heads ? $dp[$heads - 1] * $p : 0);
            }
        }
        return $dp[$target];
    }
}
