<?php
// LeetCode 0956 - Tallest Billboard
// https://leetcode.com/problems/tallest-billboard/

class Solution {
    function tallestBillboard($rods) {
        $dp = [0 => 0];
        foreach ($rods as $rod) {
            $cur = $dp;
            foreach ($cur as $diff => $taller) {
                $key1 = $diff + $rod;
                $dp[$key1] = max($dp[$key1] ?? 0, $taller + $rod);
                $nd = abs($diff - $rod);
                $nt = $diff >= $rod ? $taller : $taller - $diff + $rod;
                $dp[$nd] = max($dp[$nd] ?? 0, $nt);
            }
        }
        return $dp[0] ?? 0;
    }
}
