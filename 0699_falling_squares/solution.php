<?php
// LeetCode 0699 - Falling Squares
// https://leetcode.com/problems/falling-squares/

class Solution {
    function fallingSquares($positions) {
        $intervals = [];
        $answer = [];
        $maxHeight = 0;
        foreach ($positions as $pos) {
            $left = $pos[0];
            $side = $pos[1];
            $right = $left + $side;
            $bas = 0;
            foreach ($intervals as $it) {
                if ($it[1] > $left && $it[0] < $right) $bas = max($bas, $it[2]);
            }
            $height = $bas + $side;
            $intervals[] = [$left, $right, $height];
            $maxHeight = max($maxHeight, $height);
            $answer[] = $maxHeight;
        }
        return $answer;
    }
}
