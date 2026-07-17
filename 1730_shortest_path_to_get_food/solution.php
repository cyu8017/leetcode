<?php
// LeetCode 1730 - Shortest Path to Get Food
// https://leetcode.com/problems/shortest-path-to-get-food/

class Solution {
    /**
     * @param String[][] $grid
     * @return Integer
     */
    function getFood($grid) {
        $rows = count($grid);
        $cols = count($grid[0]);
        $queue = [];
        $seen = array_fill(0, $rows, array_fill(0, $cols, false));
        for ($r = 0; $r < $rows; $r++) {
            for ($c = 0; $c < $cols; $c++) {
                if ($grid[$r][$c] === '*') {
                    $queue[] = [$r, $c, 0];
                    $seen[$r][$c] = true;
                }
            }
        }
        $dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];
        $head = 0;
        while ($head < count($queue)) {
            [$r, $c, $d] = $queue[$head++];
            if ($grid[$r][$c] === '#') {
                return $d;
            }
            foreach ($dirs as [$dr, $dc]) {
                $nr = $r + $dr;
                $nc = $c + $dc;
                if ($nr >= 0 && $nr < $rows && $nc >= 0 && $nc < $cols && !$seen[$nr][$nc] && $grid[$nr][$nc] !== 'X') {
                    $seen[$nr][$nc] = true;
                    $queue[] = [$nr, $nc, $d + 1];
                }
            }
        }
        return -1;
    }
}
