<?php
// LeetCode 2684 - Maximum Number of Moves in a Grid
// https://leetcode.com/problems/maximum-number-of-moves-in-a-grid/

class Solution {
    function maxMoves($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        $dp = array_fill(0, $m, 0);
        for ($c = $n - 2; $c >= 0; $c--) {
            $ndp = array_fill(0, $m, 0);
            for ($r = 0; $r < $m; $r++) {
                $best = 0;
                for ($dr = -1; $dr <= 1; $dr++) {
                    $nr = $r + $dr;
                    if ($nr >= 0 && $nr < $m && $grid[$nr][$c + 1] > $grid[$r][$c]) {
                        $best = max($best, 1 + $dp[$nr]);
                    }
                }
                $ndp[$r] = $best;
            }
            $dp = $ndp;
        }
        return max($dp);
    }
}
