<?php
// LeetCode 0986 - Interval List Intersections
// https://leetcode.com/problems/interval-list-intersections/

class Solution {
    /**
     * @param Integer[][] $firstList
     * @param Integer[][] $secondList
     * @return Integer[][]
     */
    function intervalIntersection($firstList, $secondList) {
        $i = 0;
        $j = 0;
        $ans = [];
        while ($i < count($firstList) && $j < count($secondList)) {
            $lo = max($firstList[$i][0], $secondList[$j][0]);
            $hi = min($firstList[$i][1], $secondList[$j][1]);
            if ($lo <= $hi) $ans[] = [$lo, $hi];
            if ($firstList[$i][1] < $secondList[$j][1]) $i++;
            else $j++;
        }
        return $ans;
    }
}
