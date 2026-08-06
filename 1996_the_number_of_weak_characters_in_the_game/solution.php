<?php
// LeetCode 1996 - The Number of Weak Characters in the Game
// https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/

class Solution {
    /**
     * @param Integer[][] $properties
     * @return Integer
     */
    function numberOfWeakCharacters($properties) {
        usort($properties, function ($a, $b) {
            if ($a[0] !== $b[0]) {
                return $a[0] <=> $b[0];
            }
            return $b[1] <=> $a[1];
        });
        $ans = 0;
        $maxDef = 0;
        for ($i = count($properties) - 1; $i >= 0; $i--) {
            if ($properties[$i][1] < $maxDef) {
                $ans++;
            } else {
                $maxDef = $properties[$i][1];
            }
        }
        return $ans;
    }
}
