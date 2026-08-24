<?php
// LeetCode 0822 - Card Flipping Game
// https://leetcode.com/problems/card-flipping-game/

class Solution {
    /**
     * @param Integer[] $fronts
     * @param Integer[] $backs
     * @return Integer
     */
    function flipgame($fronts, $backs) {
        $same = [];
        $n = count($fronts);
        for ($i = 0; $i < $n; $i++) {
            if ($fronts[$i] === $backs[$i]) $same[$fronts[$i]] = true;
        }
        $best = PHP_INT_MAX;
        foreach ($fronts as $x) if (!isset($same[$x])) $best = min($best, $x);
        foreach ($backs as $x) if (!isset($same[$x])) $best = min($best, $x);
        return $best === PHP_INT_MAX ? 0 : $best;
    }
}
