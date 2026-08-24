<?php
// LeetCode 3279 - Maximum Total Area Occupied by Pistons
// https://leetcode.com/problems/maximum-total-area-occupied-by-pistons/

class Solution {
    function maxArea($height, $positions, $directions) {
        $n = count($positions);
        $pos = $positions;
        $dir = str_split($directions);
        $best = 0;
        for ($t = 0; $t <= 2 * $height; $t++) {
            $sum = 0;
            for ($i = 0; $i < $n; $i++) $sum += $pos[$i];
            if ($sum > $best) $best = $sum;
            for ($i = 0; $i < $n; $i++) {
                if ($dir[$i] === 'U') {
                    if ($pos[$i] === $height) { $dir[$i] = 'D'; $pos[$i]--; }
                    else $pos[$i]++;
                } else {
                    if ($pos[$i] === 0) { $dir[$i] = 'U'; $pos[$i]++; }
                    else $pos[$i]--;
                }
            }
        }
        return $best;
    }
}
