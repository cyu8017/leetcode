<?php
// LeetCode 1908 - Game of Nim
// https://leetcode.com/problems/game-of-nim/

class Solution {
    function nimGame($piles) {
        $xor = 0;
        foreach ($piles as $p) {
            $xor ^= $p;
        }
        return $xor !== 0;
    }
}
