<?php
// LeetCode 1182 - Shortest Distance to Target Color
// https://leetcode.com/problems/shortest-distance-to-target-color/

class Solution {
    /**
     * @param Integer[] $colors
     * @param Integer[][] $queries
     * @return Integer[]
     */
    function shortestDistanceColor($colors, $queries) {
        $pos = [];
        foreach ($colors as $i => $c) $pos[$c][] = $i;
        $ans = [];
        foreach ($queries as [$i, $c]) {
            if (!isset($pos[$c])) { $ans[] = -1; continue; }
            $arr = $pos[$c];
            $lo = 0; $hi = count($arr);
            while ($lo < $hi) {
                $mid = ($lo + $hi) >> 1;
                if ($arr[$mid] < $i) $lo = $mid + 1;
                else $hi = $mid;
            }
            $best = PHP_INT_MAX;
            if ($lo < count($arr)) $best = min($best, $arr[$lo] - $i);
            if ($lo > 0) $best = min($best, $i - $arr[$lo - 1]);
            $ans[] = $best === PHP_INT_MAX ? -1 : $best;
        }
        return $ans;
    }
}
