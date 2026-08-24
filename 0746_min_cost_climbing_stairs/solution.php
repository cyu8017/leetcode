<?php
// LeetCode 0746 - Min Cost Climbing Stairs
// https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution {
    function minCostClimbingStairs($cost) {
        $a = 0;
        $b = 0;
        for ($i = count($cost) - 1; $i >= 0; $i--) {
            $nextA = $cost[$i] + min($a, $b);
            $b = $a;
            $a = $nextA;
        }
        return min($a, $b);
    }
}
