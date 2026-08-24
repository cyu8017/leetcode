<?php
// LeetCode 3502 - Minimum Cost to Reach Every Position
// https://leetcode.com/problems/minimum-cost-to-reach-every-position/

class Solution {
    function minCosts($cost) {
        $n = count($cost);
        $ans = array_fill(0, $n, 0);
        $mi = $cost[0];
        for ($i = 0; $i < $n; $i++) {
            $mi = min($mi, $cost[$i]);
            $ans[$i] = $mi;
        }
        return $ans;
    }
}
