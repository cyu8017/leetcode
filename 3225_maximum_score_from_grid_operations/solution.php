<?php
// LeetCode 3225 - Maximum Score From Grid Operations
// https://leetcode.com/problems/maximum-score-from-grid-operations/

class Solution {
    function maximumScore($grid) {
        $n = count($grid);
        $prefix = [];
        for ($j = 0; $j < $n; $j++) {
            $prefix[$j] = array_fill(0, $n + 1, 0);
            for ($i = 0; $i < $n; $i++) $prefix[$j][$i + 1] = $prefix[$j][$i] + $grid[$i][$j];
        }
        $prevPick = array_fill(0, $n + 1, 0);
        $prevSkip = array_fill(0, $n + 1, 0);
        for ($j = 1; $j < $n; $j++) {
            $currPick = array_fill(0, $n + 1, 0);
            $currSkip = array_fill(0, $n + 1, 0);
            for ($curr = 0; $curr <= $n; $curr++) {
                for ($prev = 0; $prev <= $n; $prev++) {
                    if ($curr > $prev) {
                        $score = $prefix[$j - 1][$curr] - $prefix[$j - 1][$prev];
                        $currPick[$curr] = max($currPick[$curr], $prevSkip[$prev] + $score);
                        $currSkip[$curr] = max($currSkip[$curr], $prevSkip[$prev] + $score);
                    } else {
                        $score = $prefix[$j][$prev] - $prefix[$j][$curr];
                        $currPick[$curr] = max($currPick[$curr], $prevPick[$prev] + $score);
                        $currSkip[$curr] = max($currSkip[$curr], $prevPick[$prev]);
                    }
                }
            }
            $prevPick = $currPick;
            $prevSkip = $currSkip;
        }
        $ans = PHP_INT_MIN;
        foreach ($prevPick as $v) $ans = max($ans, $v);
        return $ans;
    }
}
