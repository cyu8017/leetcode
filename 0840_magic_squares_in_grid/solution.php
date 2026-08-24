<?php
// LeetCode 0840 - Magic Squares In Grid
// https://leetcode.com/problems/magic-squares-in-grid/

class Solution {
    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function numMagicSquaresInside($grid) {
        $rows = count($grid);
        $cols = count($grid[0]);
        if ($rows < 3 || $cols < 3) return 0;
        $magic = function($r, $c) use ($grid) {
            $vals = [];
            for ($i = 0; $i < 3; $i++) for ($j = 0; $j < 3; $j++) $vals[] = $grid[$r + $i][$c + $j];
            sort($vals);
            for ($i = 0; $i < 9; $i++) if ($vals[$i] !== $i + 1) return false;
            return $grid[$r][$c] + $grid[$r][$c + 1] + $grid[$r][$c + 2] === 15
                && $grid[$r + 1][$c] + $grid[$r + 1][$c + 1] + $grid[$r + 1][$c + 2] === 15
                && $grid[$r + 2][$c] + $grid[$r + 2][$c + 1] + $grid[$r + 2][$c + 2] === 15
                && $grid[$r][$c] + $grid[$r + 1][$c] + $grid[$r + 2][$c] === 15
                && $grid[$r][$c + 1] + $grid[$r + 1][$c + 1] + $grid[$r + 2][$c + 1] === 15
                && $grid[$r][$c + 2] + $grid[$r + 1][$c + 2] + $grid[$r + 2][$c + 2] === 15
                && $grid[$r][$c] + $grid[$r + 1][$c + 1] + $grid[$r + 2][$c + 2] === 15
                && $grid[$r][$c + 2] + $grid[$r + 1][$c + 1] + $grid[$r + 2][$c] === 15;
        };
        $ans = 0;
        for ($i = 0; $i < $rows - 2; $i++) {
            for ($j = 0; $j < $cols - 2; $j++) {
                if ($magic($i, $j)) $ans++;
            }
        }
        return $ans;
    }
}
