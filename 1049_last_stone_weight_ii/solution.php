<?php
// LeetCode 1049 - Last Stone Weight II
// https://leetcode.com/problems/last-stone-weight-ii/

class Solution {
    /**
     * @param Integer[] $stones
     * @return Integer
     */
    function lastStoneWeightII($stones) {
        $total = array_sum($stones);
        $reachable = [0 => true];
        foreach ($stones as $stone) {
            $next = $reachable;
            foreach ($reachable as $s => $_) {
                $next[$s + $stone] = true;
            }
            $reachable = $next;
        }
        $best = $total;
        foreach ($reachable as $s => $_) {
            $best = min($best, abs($total - 2 * $s));
        }
        return $best;
    }
}
