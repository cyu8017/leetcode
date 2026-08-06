<?php
// LeetCode 1165 - Single-Row Keyboard
// https://leetcode.com/problems/single-row-keyboard/

class Solution {
    /**
     * @param String $keyboard
     * @param String $word
     * @return Integer
     */
    function calculateTime($keyboard, $word) {
        $pos = [];
        for ($i = 0; $i < strlen($keyboard); $i++) $pos[$keyboard[$i]] = $i;
        $ans = 0; $prev = 0;
        for ($i = 0; $i < strlen($word); $i++) {
            $ans += abs($pos[$word[$i]] - $prev);
            $prev = $pos[$word[$i]];
        }
        return $ans;
    }
}
