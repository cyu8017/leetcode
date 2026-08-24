<?php
// LeetCode 2214 - Minimum Health to Beat Game
// https://leetcode.com/problems/minimum-health-to-beat-game/

class Solution {
    function solve($damage, $armor) {
        $sum = 0;
        $mx = 0;
        foreach ($damage as $d) { $sum += $d; $mx = max($mx, $d); }
        return $sum - min($armor, $mx) + 1;
    }
}
