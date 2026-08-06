<?php
// LeetCode 1275 - Find Winner on a Tic Tac Toe Game
// https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/

class Solution {
    /**
     * @param Integer[][] $moves
     * @return String
     */
    function tictactoe($moves) {
        $board = array_fill(0, 3, array_fill(0, 3, 0));
        foreach ($moves as $i => [$r, $c]) {
            $board[$r][$c] = $i % 2 === 0 ? 1 : -1;
        }
        $lines = $board;
        for ($c = 0; $c < 3; $c++) {
            $lines[] = [$board[0][$c], $board[1][$c], $board[2][$c]];
        }
        $lines[] = [$board[0][0], $board[1][1], $board[2][2]];
        $lines[] = [$board[0][2], $board[1][1], $board[2][0]];
        foreach ($lines as $line) {
            $s = array_sum($line);
            if (abs($s) === 3) return $s === 3 ? 'A' : 'B';
        }
        return count($moves) === 9 ? 'Draw' : 'Pending';
    }
}
