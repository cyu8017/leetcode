<?php
// LeetCode 3147 - Taking Maximum Energy From the Mystic Dungeon
// https://leetcode.com/problems/taking-maximum-energy-from-the-mystic-dungeon/

class Solution {
    function maximumEnergy($energy, $k) {
        $ans = -(1 << 30);
        $n = count($energy);
        for ($i = $n - $k; $i < $n; $i++) {
            for ($j = $i, $s = 0; $j >= 0; $j -= $k) {
                $s += $energy[$j];
                $ans = max($ans, $s);
            }
        }
        return $ans;
    }
}
