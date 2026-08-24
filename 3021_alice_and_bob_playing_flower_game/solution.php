<?php
// LeetCode 3021 - Alice and Bob Playing Flower Game
// https://leetcode.com/problems/alice-and-bob-playing-flower-game/

class Solution {
    function flowerGame($n, $m) {
        $a1 = intdiv($n + 1, 2);
        $b1 = intdiv($m + 1, 2);
        $a2 = intdiv($n, 2);
        $b2 = intdiv($m, 2);
        return $a1 * $b2 + $a2 * $b1;
    }
}
