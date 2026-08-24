<?php
// LeetCode 0810 - Chalkboard XOR Game
// https://leetcode.com/problems/chalkboard-xor-game/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Boolean
     */
    function xorGame($nums) {
        $x = 0;
        foreach ($nums as $num) $x ^= $num;
        return $x === 0 || count($nums) % 2 === 0;
    }
}
