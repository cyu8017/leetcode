<?php
// LeetCode 0789 - Escape The Ghosts
// https://leetcode.com/problems/escape-the-ghosts/

class Solution {
    /**
     * @param Integer[][] $ghosts
     * @param Integer[] $target
     * @return Boolean
     */
    function escapeGhosts($ghosts, $target) {
        $targetDist = abs($target[0]) + abs($target[1]);
        foreach ($ghosts as $ghost) {
            if (abs($ghost[0] - $target[0]) + abs($ghost[1] - $target[1]) <= $targetDist) {
                return false;
            }
        }
        return true;
    }
}
