<?php
// LeetCode 1828 - Queries on Number of Points Inside a Circle
// https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle/

class Solution {
    /**
     * @param Integer[][] $points
     * @param Integer[][] $queries
     * @return Integer[]
     */
    function countPoints($points, $queries) {
        $result = [];
        foreach ($queries as $query) {
            [$xq, $yq, $r] = $query;
            $radiusSq = $r * $r;
            $count = 0;
            foreach ($points as $point) {
                [$x, $y] = $point;
                if (($x - $xq) * ($x - $xq) + ($y - $yq) * ($y - $yq) <= $radiusSq) {
                    $count++;
                }
            }
            $result[] = $count;
        }
        return $result;
    }
}
