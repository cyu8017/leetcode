<?php
// LeetCode 0130 - Surrounded Regions
// https://leetcode.com/problems/surrounded-regions/

class Solution {
    /**
     * @param String[][] $board
     * @return NULL
     */
    function solve(&$board) {
        if (empty($board) || empty($board[0])) {
            return;
        }
        $rows = count($board);
        $columns = count($board[0]);
        $mark = function ($row, $column) use (&$mark, &$board, $rows, $columns) {
            if ($row < 0 || $row >= $rows || $column < 0 || $column >= $columns ||
                $board[$row][$column] !== 'O') {
                return;
            }
            $board[$row][$column] = 'E';
            $mark($row + 1, $column);
            $mark($row - 1, $column);
            $mark($row, $column + 1);
            $mark($row, $column - 1);
        };

        for ($row = 0; $row < $rows; $row++) {
            $mark($row, 0);
            $mark($row, $columns - 1);
        }
        for ($column = 0; $column < $columns; $column++) {
            $mark(0, $column);
            $mark($rows - 1, $column);
        }
        for ($row = 0; $row < $rows; $row++) {
            for ($column = 0; $column < $columns; $column++) {
                if ($board[$row][$column] === 'O') {
                    $board[$row][$column] = 'X';
                } elseif ($board[$row][$column] === 'E') {
                    $board[$row][$column] = 'O';
                }
            }
        }
    }
}
