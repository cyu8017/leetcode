<?php

// LeetCode 0200 - Number of Islands
class Solution {
    function numIslands($grid) {
        if (empty($grid)) {
            return 0;
        }

        $rows = count($grid);
        $cols = count($grid[0]);
        $count = 0;

        $dfs = function ($row, $col) use (&$dfs, &$grid, $rows, $cols) {
            if ($row < 0 || $row >= $rows || $col < 0 || $col >= $cols || $grid[$row][$col] !== "1") {
                return;
            }
            $grid[$row][$col] = "0";
            $dfs($row + 1, $col);
            $dfs($row - 1, $col);
            $dfs($row, $col + 1);
            $dfs($row, $col - 1);
        };

        for ($row = 0; $row < $rows; $row++) {
            for ($col = 0; $col < $cols; $col++) {
                if ($grid[$row][$col] === "1") {
                    $count++;
                    $dfs($row, $col);
                }
            }
        }
        return $count;
    }
}