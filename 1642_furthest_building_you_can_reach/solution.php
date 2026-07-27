<?php
// LeetCode 1642 - Furthest Building You Can Reach
// https://leetcode.com/problems/furthest-building-you-can-reach/

class Solution {
    /**
     * @param Integer[] $heights
     * @param Integer $bricks
     * @param Integer $ladders
     * @return Integer
     */
    function furthestBuilding($heights, $bricks, $ladders) {
        $climbs = new SplMinHeap();
        $n = count($heights);
        for ($i = 0; $i < $n - 1; $i++) {
            $d = $heights[$i + 1] - $heights[$i];
            if ($d <= 0) {
                continue;
            }
            $climbs->insert($d);
            if ($climbs->count() > $ladders) {
                $bricks -= $climbs->extract();
            }
            if ($bricks < 0) {
                return $i;
            }
        }
        return $n - 1;
    }
}
