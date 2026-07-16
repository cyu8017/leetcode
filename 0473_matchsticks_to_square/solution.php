<?php
// LeetCode 0473 - Matchsticks to Square
// https://leetcode.com/problems/matchsticks-to-square/

class Solution {
    /**
     * @param int[] $matchsticks
     * @return bool
     */
    function makesquare($matchsticks) {
        if (count($matchsticks) === 0) {
            return false;
        }
        $total = array_sum($matchsticks);
        if ($total % 4 !== 0) {
            return false;
        }
        $side = intdiv($total, 4);
        rsort($matchsticks);

        $dfs = function ($index, $sides) use (&$dfs, $matchsticks, $side) {
            if ($index === count($matchsticks)) {
                return $sides[0] === $side && count(array_unique($sides)) === 1;
            }
            $length = $matchsticks[$index];
            for ($sideIndex = 0; $sideIndex < 4; $sideIndex++) {
                if ($sides[$sideIndex] + $length > $side) {
                    continue;
                }
                if ($sideIndex > 0 && $sides[$sideIndex] === $sides[$sideIndex - 1]) {
                    continue;
                }
                $sides[$sideIndex] += $length;
                if ($dfs($index + 1, $sides)) {
                    return true;
                }
                $sides[$sideIndex] -= $length;
            }
            return false;
        };

        return $dfs(0, [0, 0, 0, 0]);
    }
}
