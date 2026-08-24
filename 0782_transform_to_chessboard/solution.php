<?php
// LeetCode 0782 - Transform to Chessboard
// https://leetcode.com/problems/transform-to-chessboard/

class Solution {
    /**
     * @param Integer[][] $board
     * @return Integer
     */
    function movesToChessboard($board) {
        $n = count($board);
        for ($i = 0; $i < $n; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if (($board[0][0] ^ $board[$i][0] ^ $board[0][$j] ^ $board[$i][$j]) !== 0) return -1;
            }
        }
        $rowSum = 0;
        $colSum = 0;
        for ($i = 0; $i < $n; $i++) {
            $rowSum += $board[0][$i];
            $colSum += $board[$i][0];
        }
        if ($rowSum < ($n >> 1) || $rowSum > (($n + 1) >> 1)) return -1;
        if ($colSum < ($n >> 1) || $colSum > (($n + 1) >> 1)) return -1;
        $rowSwap = 0;
        $colSwap = 0;
        for ($i = 0; $i < $n; $i++) {
            if ($board[0][$i] !== $i % 2) $rowSwap++;
            if ($board[$i][0] !== $i % 2) $colSwap++;
        }
        if ($n % 2 === 1) {
            if ($rowSwap % 2 === 1) $rowSwap = $n - $rowSwap;
            if ($colSwap % 2 === 1) $colSwap = $n - $colSwap;
        } else {
            $rowSwap = min($rowSwap, $n - $rowSwap);
            $colSwap = min($colSwap, $n - $colSwap);
        }
        return ($rowSwap + $colSwap) >> 1;
    }
}
