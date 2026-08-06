<?php
// LeetCode 1135 - Connecting Cities With Minimum Cost
// https://leetcode.com/problems/connecting-cities-with-minimum-cost/

class Solution {
    /**
     * @param Integer $n
     * @param Integer[][] $connections
     * @return Integer
     */
    function minimumCost($n, $connections) {
        usort($connections, fn($a, $b) => $a[2] <=> $b[2]);
        $parent = range(0, $n);
        $find = function ($x) use (&$parent, &$find) {
            if ($parent[$x] !== $x) $parent[$x] = $find($parent[$x]);
            return $parent[$x];
        };
        $cost = 0;
        $edges = 0;
        foreach ($connections as [$a, $b, $c]) {
            $ra = $find($a);
            $rb = $find($b);
            if ($ra === $rb) continue;
            $parent[$ra] = $rb;
            $cost += $c;
            $edges++;
            if ($edges === $n - 1) return $cost;
        }
        return -1;
    }
}
