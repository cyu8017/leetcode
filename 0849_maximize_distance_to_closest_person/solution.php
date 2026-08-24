<?php
// LeetCode 0849 - Maximize Distance to Closest Person
// https://leetcode.com/problems/maximize-distance-to-closest-person/

class Solution {
    /**
     * @param Integer[] $seats
     * @return Integer
     */
    function maxDistToClosest($seats) {
        $n = count($seats);
        $prev = -1;
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            if ($seats[$i] === 1) {
                if ($prev === -1) $ans = $i;
                else $ans = max($ans, intdiv($i - $prev, 2));
                $prev = $i;
            }
        }
        return max($ans, $n - 1 - $prev);
    }
}
