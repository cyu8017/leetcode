<?php
// LeetCode 1626 - Best Team With No Conflicts
// https://leetcode.com/problems/best-team-with-no-conflicts/

class Solution {
    /**
     * @param Integer[] $scores
     * @param Integer[] $ages
     * @return Integer
     */
    function bestTeamScore($scores, $ages) {
        $n = count($scores);
        $players = [];
        for ($i = 0; $i < $n; $i++) {
            $players[] = [$ages[$i], $scores[$i]];
        }
        usort($players, function ($a, $b) {
            return $a[0] === $b[0] ? $a[1] <=> $b[1] : $a[0] <=> $b[0];
        });
        $dp = array_fill(0, $n, 0);
        $best = 0;
        for ($i = 0; $i < $n; $i++) {
            $score = $players[$i][1];
            $dp[$i] = $score;
            for ($j = 0; $j < $i; $j++) {
                if ($players[$j][1] <= $score) {
                    $dp[$i] = max($dp[$i], $dp[$j] + $score);
                }
            }
            $best = max($best, $dp[$i]);
        }
        return $best;
    }
}
