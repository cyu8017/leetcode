<?php
// LeetCode 1872 - Stone Game VIII
// https://leetcode.com/problems/stone-game-viii/

class Solution {
    /**
     * @param Integer[] $stones
     * @return Integer
     */
    function stoneGameVIII($stones) {
        $n = count($stones);
        for ($i = 1; $i < $n; $i++) {
            $stones[$i] += $stones[$i - 1];
        }

        $score = $stones[$n - 1];
        for ($i = $n - 2; $i > 0; $i--) {
            $score = max($stones[$i] - $score, $score);
        }
        return $score;
    }
}
