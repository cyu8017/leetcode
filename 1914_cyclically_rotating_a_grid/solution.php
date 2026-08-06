<?php
// LeetCode 1914 - Cyclically Rotating a Grid
// https://leetcode.com/problems/cyclically-rotating-a-grid/

class Solution {
    /**
     * @param Integer[][] $grid
     * @param Integer $k
     * @return Integer[][]
     */
    function rotateGrid($grid, $k) {
        $m = count($grid);
        $n = count($grid[0]);
        $layers = intdiv(min($m, $n), 2);

        for ($layer = 0; $layer < $layers; $layer++) {
            $vals = [];
            for ($c = $layer; $c < $n - $layer; $c++) {
                $vals[] = $grid[$layer][$c];
            }
            for ($r = $layer + 1; $r < $m - $layer; $r++) {
                $vals[] = $grid[$r][$n - $layer - 1];
            }
            if ($m - 2 * $layer > 1) {
                for ($c = $n - $layer - 2; $c >= $layer; $c--) {
                    $vals[] = $grid[$m - $layer - 1][$c];
                }
            }
            if ($n - 2 * $layer > 1) {
                for ($r = $m - $layer - 2; $r > $layer; $r--) {
                    $vals[] = $grid[$r][$layer];
                }
            }

            $len = count($vals);
            $shift = $k % $len;
            $vals = array_merge(array_slice($vals, $shift), array_slice($vals, 0, $shift));

            $idx = 0;
            for ($c = $layer; $c < $n - $layer; $c++) {
                $grid[$layer][$c] = $vals[$idx++];
            }
            for ($r = $layer + 1; $r < $m - $layer; $r++) {
                $grid[$r][$n - $layer - 1] = $vals[$idx++];
            }
            if ($m - 2 * $layer > 1) {
                for ($c = $n - $layer - 2; $c >= $layer; $c--) {
                    $grid[$m - $layer - 1][$c] = $vals[$idx++];
                }
            }
            if ($n - 2 * $layer > 1) {
                for ($r = $m - $layer - 2; $r > $layer; $r--) {
                    $grid[$r][$layer] = $vals[$idx++];
                }
            }
        }

        return $grid;
    }
}
