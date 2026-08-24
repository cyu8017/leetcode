<?php
// LeetCode 0573 - Squirrel Simulation
// https://leetcode.com/problems/squirrel-simulation/

class Solution {
    function minDistance($height, $width, $tree, $squirrel, $nuts) {
        $dist = function($a, $b) {
            return abs($a[0] - $b[0]) + abs($a[1] - $b[1]);
        };
        $total = 0;
        $bestSave = PHP_INT_MIN;
        foreach ($nuts as $nut) {
            $treeDist = $dist($tree, $nut);
            $squirrelDist = $dist($squirrel, $nut);
            $total += 2 * $treeDist;
            $bestSave = max($bestSave, $treeDist - $squirrelDist);
        }
        return $total - $bestSave;
    }
}
