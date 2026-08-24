<?php
// LeetCode 0794 - Valid Tic-Tac-Toe State
// https://leetcode.com/problems/valid-tic-tac-toe-state/

class Solution {
    /**
     * @param String[] $board
     * @return Boolean
     */
    function validTicTacToe($board) {
        $x = 0;
        $o = 0;
        foreach ($board as $row) {
            $len = strlen($row);
            for ($i = 0; $i < $len; $i++) {
                $ch = $row[$i];
                if ($ch === 'X') $x++;
                elseif ($ch === 'O') $o++;
            }
        }
        if ($o > $x || $x - $o > 1) return false;
        $win = function($player) use ($board) {
            for ($i = 0; $i < 3; $i++) {
                if ($board[$i][0] === $player && $board[$i][1] === $player && $board[$i][2] === $player) return true;
                if ($board[0][$i] === $player && $board[1][$i] === $player && $board[2][$i] === $player) return true;
            }
            if ($board[0][0] === $player && $board[1][1] === $player && $board[2][2] === $player) return true;
            if ($board[0][2] === $player && $board[1][1] === $player && $board[2][0] === $player) return true;
            return false;
        };
        $xWin = $win('X');
        $oWin = $win('O');
        if ($xWin && $oWin) return false;
        if ($xWin && $x !== $o + 1) return false;
        if ($oWin && $x !== $o) return false;
        return true;
    }
}
