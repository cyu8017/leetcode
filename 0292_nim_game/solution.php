<?php
// LeetCode 0292 - Nim Game
// https://leetcode.com/problems/nim-game/

class Solution {
    /**
     * @param Integer $n
     * @return Boolean
     */
    function canWinNim($n) {
        return $n % 4 !== 0;
    }
}
