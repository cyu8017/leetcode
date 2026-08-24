<?php
// LeetCode 3736 - Minimum Moves to Equal Array Elements III
// https://leetcode.com/problems/minimum-moves-to-equal-array-elements-iii/

class Solution {
    function minMoves($nums) {
        $mx = 0;
        $s = 0;
        foreach ($nums as $x) {
            $mx = max($mx, $x);
            $s += $x;
        }
        return $mx * count($nums) - $s;
    }
}
