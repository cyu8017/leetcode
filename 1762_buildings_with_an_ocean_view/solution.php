<?php
// LeetCode 1762 - Buildings With an Ocean View
// https://leetcode.com/problems/buildings-with-an-ocean-view/

class Solution {
    /**
     * @param Integer[] $heights
     * @return Integer[]
     */
    function findBuildings($heights) {
        $ans = [];
        $tallest = 0;
        for ($i = count($heights) - 1; $i >= 0; $i--) {
            if ($heights[$i] > $tallest) {
                $ans[] = $i;
                $tallest = $heights[$i];
            }
        }
        return array_reverse($ans);
    }
}
