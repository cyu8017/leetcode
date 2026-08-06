<?php
// LeetCode 1510 - Stone Game IV
// https://leetcode.com/problems/stone-game-iv/

class Solution {
    /**
     * @param Integer $n
     * @return Boolean
     */
    function winnerSquareGame($n) {
        $win = array_fill(0, $n + 1, false);
        for ($value = 1; $value <= $n; $value++) {
            for ($root = 1; $root * $root <= $value; $root++) {
                if (!$win[$value - $root * $root]) {
                    $win[$value] = true;
                    break;
                }
            }
        }
        return $win[$n];
    }
}
