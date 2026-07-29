<?php
// LeetCode 1007 - Minimum Domino Rotations For Equal Row
// https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/

class Solution {
    /**
     * @param Integer[] $tops
     * @param Integer[] $bottoms
     * @return Integer
     */
    function minDominoRotations($tops, $bottoms) {
        $check = function ($target) use ($tops, $bottoms) {
            $rotTop = $rotBot = 0;
            $n = count($tops);
            for ($i = 0; $i < $n; $i++) {
                $t = $tops[$i];
                $b = $bottoms[$i];
                if ($t !== $target && $b !== $target) {
                    return PHP_INT_MAX;
                }
                if ($t !== $target) {
                    $rotTop++;
                }
                if ($b !== $target) {
                    $rotBot++;
                }
            }
            return min($rotTop, $rotBot);
        };
        $ans = min($check($tops[0]), $check($bottoms[0]));
        return $ans === PHP_INT_MAX ? -1 : $ans;
    }
}
