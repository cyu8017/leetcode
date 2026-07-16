<?php
// LeetCode 0529 - Minesweeper
// https://leetcode.com/problems/minesweeper/

class Solution {
    /** @var int[][] */
    private array $directions = [
        [-1, -1], [-1, 0], [-1, 1],
        [0, -1],           [0, 1],
        [1, -1],  [1, 0],  [1, 1],
    ];

    /**
     * @param String[][] $board
     * @param Integer[] $click
     * @return String[][]
     */
    function updateBoard($board, $click) {
        return $this->update_board($board, $click);
    }

    /**
     * @param String[][] $board
     * @param Integer[] $click
     * @return String[][]
     */
    function update_board($board, $click) {
        $rows = count($board);
        $cols = count($board[0]);
        [$row, $col] = $click;

        if ($board[$row][$col] === 'M') {
            $board[$row][$col] = 'X';
            return $board;
        }

        $this->reveal($board, $row, $col, $rows, $cols);
        return $board;
    }

    /**
     * @param String[][] $board
     * @param int $r
     * @param int $c
     * @param int $rows
     * @param int $cols
     * @return int
     */
    private function countMines($board, $r, $c, $rows, $cols) {
        $total = 0;
        foreach ($this->directions as [$dr, $dc]) {
            $nr = $r + $dr;
            $nc = $c + $dc;
            if ($nr >= 0 && $nr < $rows && $nc >= 0 && $nc < $cols && $board[$nr][$nc] === 'M') {
                $total++;
            }
        }
        return $total;
    }

    /**
     * @param String[][] $board
     * @param int $r
     * @param int $c
     * @param int $rows
     * @param int $cols
     */
    private function reveal(&$board, $r, $c, $rows, $cols) {
        if ($r < 0 || $r >= $rows || $c < 0 || $c >= $cols || $board[$r][$c] !== 'E') {
            return;
        }
        $mines = $this->countMines($board, $r, $c, $rows, $cols);
        $board[$r][$c] = $mines === 0 ? 'B' : (string)$mines;
        if ($mines !== 0) {
            return;
        }
        foreach ($this->directions as [$dr, $dc]) {
            $this->reveal($board, $r + $dr, $c + $dc, $rows, $cols);
        }
    }
}
