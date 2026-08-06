<?php
// LeetCode 1168 - Optimize Water Distribution in a Village
// https://leetcode.com/problems/optimize-water-distribution-in-a-village/

class Solution {
    /**
     * @param Integer $n
     * @param Integer[] $wells
     * @param Integer[][] $pipes
     * @return Integer
     */
    function minCostToSupplyWater($n, $wells, $pipes) {
        $parent = range(0, $n);
        $find = function ($x) use (&$parent, &$find) {
            while ($parent[$x] !== $x) {
                $parent[$x] = $parent[$parent[$x]];
                $x = $parent[$x];
            }
            return $x;
        };
        $edges = [];
        foreach ($wells as $i => $w) $edges[] = [0, $i + 1, $w];
        foreach ($pipes as $p) $edges[] = $p;
        usort($edges, fn($a, $b) => $a[2] <=> $b[2]);
        $ans = 0;
        foreach ($edges as [$a, $b, $cost]) {
            $ra = $find($a); $rb = $find($b);
            if ($ra === $rb) continue;
            $parent[$rb] = $ra;
            $ans += $cost;
        }
        return $ans;
    }
}
