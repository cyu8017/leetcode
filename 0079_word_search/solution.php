<?php
// LeetCode 0079 - Word Search
// https://leetcode.com/problems/word-search/

class Solution {
    /**
     * @param String[][] $board
     * @param String $word
     * @return Boolean
     */
    function exist($board, $word) {
        $rows = count($board);
        $cols = count($board[0]);

        $dfs = function ($row, $col, $index) use (&$board, &$word, &$rows, &$cols, &$dfs) {
            if ($index === strlen($word)) {
                return true;
            }
            if (
                $row < 0
                || $col < 0
                || $row >= $rows
                || $col >= $cols
                || $board[$row][$col] !== $word[$index]
            ) {
                return false;
            }

            $temp = $board[$row][$col];
            $board[$row][$col] = '#';

            $found = $dfs($row + 1, $col, $index + 1)
                || $dfs($row - 1, $col, $index + 1)
                || $dfs($row, $col + 1, $index + 1)
                || $dfs($row, $col - 1, $index + 1);

            $board[$row][$col] = $temp;
            return $found;
        };

        for ($row = 0; $row < $rows; $row++) {
            for ($col = 0; $col < $cols; $col++) {
                if ($dfs($row, $col, 0)) {
                    return true;
                }
            }
        }

        return false;
    }
}
