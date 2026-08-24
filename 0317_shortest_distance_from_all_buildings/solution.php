<?php
// LeetCode 0317 - Shortest Distance from All Buildings
// https://leetcode.com/problems/shortest-distance-from-all-buildings/

class Solution {
    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function shortestDistance($grid) {
        if (empty($grid)) {
            return -1;
        }

        $rows = count($grid);
        $cols = count($grid[0]);
        $buildings = 0;
        foreach ($grid as $row) {
            foreach ($row as $cell) {
                if ($cell === 1) {
                    $buildings++;
                }
            }
        }

        $distances = array_fill(0, $rows, array_fill(0, $cols, 0));
        $reach = array_fill(0, $rows, array_fill(0, $cols, 0));
        $directions = [[1, 0], [-1, 0], [0, 1], [0, -1]];

        for ($row = 0; $row < $rows; $row++) {
            for ($col = 0; $col < $cols; $col++) {
                if ($grid[$row][$col] !== 1) {
                    continue;
                }
                $queue = [[$row, $col, 0]];
                $visited = ["$row,$col" => true];
                while (!empty($queue)) {
                    [$currentRow, $currentCol, $distance] = array_shift($queue);
                    foreach ($directions as [$dr, $dc]) {
                        $nr = $currentRow + $dr;
                        $nc = $currentCol + $dc;
                        if ($nr < 0 || $nr >= $rows || $nc < 0 || $nc >= $cols) {
                            continue;
                        }
                        if ($grid[$nr][$nc] !== 0) {
                            continue;
                        }
                        $key = "$nr,$nc";
                        if (isset($visited[$key])) {
                            continue;
                        }
                        $visited[$key] = true;
                        $distances[$nr][$nc] += $distance + 1;
                        $reach[$nr][$nc]++;
                        $queue[] = [$nr, $nc, $distance + 1];
                    }
                }
            }
        }

        $best = PHP_INT_MAX;
        for ($row = 0; $row < $rows; $row++) {
            for ($col = 0; $col < $cols; $col++) {
                if ($grid[$row][$col] === 0 && $reach[$row][$col] === $buildings) {
                    $best = min($best, $distances[$row][$col]);
                }
            }
        }
        return $best === PHP_INT_MAX ? -1 : $best;
    }
}
