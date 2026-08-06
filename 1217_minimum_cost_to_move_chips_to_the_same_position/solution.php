<?php
// LeetCode 1217 - Minimum Cost to Move Chips to The Same Position
// https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/

class Solution {
    /**
     * @param Integer[] $position
     * @return Integer
     */
    function minCostToMoveChips($position) {
        $odd = 0;
        foreach ($position as $x) if ($x & 1) $odd++;
        return min($odd, count($position) - $odd);
    }
}
