<?php
// LeetCode 1823 - Find the Winner of the Circular Game
// https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution {
    /**
     * @param Integer $n
     * @param Integer $k
     * @return Integer
     */
    function findTheWinner($n, $k) {
        $pos = 0;
        for ($size = 2; $size <= $n; $size++) {
            $pos = ($pos + $k) % $size;
        }
        return $pos + 1;
    }
}
