<?php
// LeetCode 3789 - Minimum Cost to Acquire Required Items
// https://leetcode.com/problems/minimum-cost-to-acquire-required-items/

class Solution {
    function minimumCost($cost1, $cost2, $costBoth, $need1, $need2) {
        $a = $need1 * $cost1 + $need2 * $cost2;
        $b = $costBoth * max($need1, $need2);
        $mn = min($need1, $need2);
        $c = $costBoth * $mn + ($need1 - $mn) * $cost1 + ($need2 - $mn) * $cost2;
        return min($a, min($b, $c));
    }
}
