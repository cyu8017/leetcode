<?php
// LeetCode 1884 - Egg Drop With 2 Eggs and N Floors
// https://leetcode.com/problems/egg-drop-with-2-eggs-and-n-floors/

class Solution {
    /**
     * @param Integer $n
     * @return Integer
     */
    function twoEggDrop($n) {
        $moves = 0;
        $covered = 0;
        while ($covered < $n) {
            $moves++;
            $covered += $moves;
        }
        return $moves;
    }
}
