<?php
// LeetCode 0051 - N-Queens
// https://leetcode.com/problems/n-queens/

class Solution {
    /**
     * @param Integer $n
     * @return String[][]
     */
    function solveNQueens($n) {
        $result = [];
        $cols = [];
        $diag1 = [];
        $diag2 = [];
        $board = array_fill(0, $n, str_repeat('.', $n));

        $backtrack = function ($row) use (
            &$backtrack,
            $n,
            &$result,
            &$cols,
            &$diag1,
            &$diag2,
            &$board
        ) {
            if ($row === $n) {
                $result[] = $board;
                return;
            }

            for ($col = 0; $col < $n; $col++) {
                if (isset($cols[$col]) || isset($diag1[$row + $col]) || isset($diag2[$row - $col])) {
                    continue;
                }

                $cols[$col] = true;
                $diag1[$row + $col] = true;
                $diag2[$row - $col] = true;

                $rowChars = str_split($board[$row]);
                $rowChars[$col] = 'Q';
                $board[$row] = implode('', $rowChars);

                $backtrack($row + 1);

                unset($cols[$col], $diag1[$row + $col], $diag2[$row - $col]);
                $board[$row] = str_repeat('.', $n);
            }
        };

        $backtrack(0);
        return $result;
    }
}
