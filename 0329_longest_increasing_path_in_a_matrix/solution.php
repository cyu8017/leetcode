<?php
// LeetCode 0329 - Longest Increasing Path in a Matrix
// https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

class Solution {
    /**
     * @param Integer[][] $matrix
     * @return Integer
     */
    function longestIncreasingPath($matrix) {
        if (empty($matrix) || empty($matrix[0])) {
            return 0;
        }

        $rows = count($matrix);
        $cols = count($matrix[0]);
        $directions = [[1, 0], [-1, 0], [0, 1], [0, -1]];
        $memo = [];

        $dfs = function ($row, $col) use (&$dfs, $matrix, $rows, $cols, $directions, &$memo) {
            $key = $row * $cols + $col;
            if (array_key_exists($key, $memo)) {
                return $memo[$key];
            }

            $best = 1;
            foreach ($directions as $direction) {
                $nr = $row + $direction[0];
                $nc = $col + $direction[1];
                if ($nr >= 0 && $nr < $rows && $nc >= 0 && $nc < $cols && $matrix[$nr][$nc] > $matrix[$row][$col]) {
                    $best = max($best, 1 + $dfs($nr, $nc));
                }
            }
            $memo[$key] = $best;
            return $best;
        };

        $answer = 0;
        for ($row = 0; $row < $rows; $row++) {
            for ($col = 0; $col < $cols; $col++) {
                $answer = max($answer, $dfs($row, $col));
            }
        }
        return $answer;
    }
}
