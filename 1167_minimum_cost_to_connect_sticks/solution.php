<?php
// LeetCode 1167 - Minimum Cost to Connect Sticks
// https://leetcode.com/problems/minimum-cost-to-connect-sticks/

class Solution {
    /**
     * @param Integer[] $sticks
     * @return Integer
     */
    function connectSticks($sticks) {
        if (count($sticks) <= 1) return 0;
        $heap = new SplMinHeap();
        foreach ($sticks as $s) $heap->insert($s);
        $ans = 0;
        while ($heap->count() > 1) {
            $cost = $heap->extract() + $heap->extract();
            $ans += $cost;
            $heap->insert($cost);
        }
        return $ans;
    }
}
