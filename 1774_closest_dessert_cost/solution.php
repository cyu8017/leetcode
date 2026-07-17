<?php
// LeetCode 1774 - Closest Dessert Cost
// https://leetcode.com/problems/closest-dessert-cost/

class Solution {
    /**
     * @param Integer[] $baseCosts
     * @param Integer[] $toppingCosts
     * @param Integer $target
     * @return Integer
     */
    function closestCost($baseCosts, $toppingCosts, $target) {
        $best = PHP_INT_MAX / 2;

        $dfs = function ($i, $cur) use (&$dfs, &$best, $toppingCosts, $target) {
            $curDiff = abs($cur - $target);
            $bestDiff = abs($best - $target);
            if ($curDiff < $bestDiff || ($curDiff == $bestDiff && $cur < $best)) {
                $best = $cur;
            }
            if ($i === count($toppingCosts) || $cur >= $target) {
                return;
            }
            $dfs($i + 1, $cur);
            $dfs($i + 1, $cur + $toppingCosts[$i]);
            $dfs($i + 1, $cur + 2 * $toppingCosts[$i]);
        };

        foreach ($baseCosts as $base) {
            $dfs(0, $base);
        }
        return $best;
    }
}
