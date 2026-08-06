<?php
// LeetCode 1140 - Stone Game II
// https://leetcode.com/problems/stone-game-ii/

class Solution {
    /**
     * @param Integer[] $piles
     * @return Integer
     */
    function stoneGameII($piles) {
        $n = count($piles);
        $suffix = array_fill(0, $n + 1, 0);
        for ($i = $n - 1; $i >= 0; $i--) {
            $suffix[$i] = $suffix[$i + 1] + $piles[$i];
        }
        $memo = [];
        $dp = function ($i, $m) use (&$dp, &$memo, $n, $suffix) {
            if ($i >= $n) return 0;
            $key = "$i,$m";
            if (isset($memo[$key])) return $memo[$key];
            if ($i + 2 * $m >= $n) return $memo[$key] = $suffix[$i];
            $best = 0;
            for ($x = 1; $x <= 2 * $m; $x++) {
                $best = max($best, $suffix[$i] - $dp($i + $x, max($m, $x)));
            }
            return $memo[$key] = $best;
        };
        return $dp(0, 1);
    }
}
