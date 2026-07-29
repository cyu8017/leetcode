<?php
// LeetCode 1034 - Coloring A Border
// https://leetcode.com/problems/coloring-a-border/

class Solution {
    /**
     * @param Integer[][] $grid
     * @param Integer $row
     * @param Integer $col
     * @param Integer $color
     * @return Integer[][]
     */
    function colorBorder($grid, $row, $col, $color) {
        $m = count($grid);
        $n = count($grid[0]);
        $original = $grid[$row][$col];
        $component = [];
        $stack = [[$row, $col]];
        $component[$row . ',' . $col] = [$row, $col];
        while (!empty($stack)) {
            [$r, $c] = array_pop($stack);
            foreach ([[$r + 1, $c], [$r - 1, $c], [$r, $c + 1], [$r, $c - 1]] as $nb) {
                $nr = $nb[0];
                $nc = $nb[1];
                $key = $nr . ',' . $nc;
                if ($nr >= 0 && $nr < $m && $nc >= 0 && $nc < $n && $grid[$nr][$nc] === $original && !isset($component[$key])) {
                    $component[$key] = [$nr, $nc];
                    $stack[] = [$nr, $nc];
                }
            }
        }
        $border = [];
        foreach ($component as $cell) {
            [$r, $c] = $cell;
            foreach ([[$r + 1, $c], [$r - 1, $c], [$r, $c + 1], [$r, $c - 1]] as $nb) {
                $nr = $nb[0];
                $nc = $nb[1];
                if (!($nr >= 0 && $nr < $m && $nc >= 0 && $nc < $n) || !isset($component[$nr . ',' . $nc])) {
                    $border[] = [$r, $c];
                    break;
                }
            }
        }
        foreach ($border as $cell) {
            $grid[$cell[0]][$cell[1]] = $color;
        }
        return $grid;
    }
}
