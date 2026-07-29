<?php
// LeetCode 1033 - Moving Stones Until Consecutive
// https://leetcode.com/problems/moving-stones-until-consecutive/

class Solution {
    /**
     * @param Integer $a
     * @param Integer $b
     * @param Integer $c
     * @return Integer[]
     */
    function numMovesStones($a, $b, $c) {
        $arr = [$a, $b, $c];
        sort($arr);
        $x = $arr[0];
        $y = $arr[1];
        $z = $arr[2];
        if ($z - $x === 2) {
            $minMoves = 0;
        } elseif ($y - $x <= 2 || $z - $y <= 2) {
            $minMoves = 1;
        } else {
            $minMoves = 2;
        }
        return [$minMoves, $z - $x - 2];
    }
}
