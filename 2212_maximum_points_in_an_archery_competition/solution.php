<?php
// LeetCode 2212 - Maximum Points in an Archery Competition
// https://leetcode.com/problems/maximum-points-in-an-archery-competition/

class Solution {
    function maximumBobPoints($numArrows, $aliceArrows) {
        $bestScore = -1;
        $best = array_fill(0, 12, 0);
        $bob = array_fill(0, 12, 0);
        $dfs = function($i, $remain, $score) use (&$dfs, &$bestScore, &$best, &$bob, $aliceArrows) {
            if ($i === 12) {
                if ($score > $bestScore) {
                    $bestScore = $score;
                    $best = $bob;
                    if ($remain > 0) $best[0] += $remain;
                }
                return;
            }
            $dfs($i + 1, $remain, $score);
            $need = $aliceArrows[$i] + 1;
            if ($remain >= $need) {
                $bob[$i] = $need;
                $dfs($i + 1, $remain - $need, $score + $i);
                $bob[$i] = 0;
            }
        };
        $dfs(0, $numArrows, 0);
        return $best;
    }
}
