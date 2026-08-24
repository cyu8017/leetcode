<?php
// LeetCode 0036 - Valid Sudoku
// https://leetcode.com/problems/valid-sudoku/

class Solution {
    /**
     * @param String[][] $board
     * @return Boolean
     */
    function isValidSudoku($board) {
        $rows = array_fill(0, 9, []);
        $cols = array_fill(0, 9, []);
        $boxes = array_fill(0, 9, []);

        for ($r = 0; $r < 9; $r++) {
            for ($c = 0; $c < 9; $c++) {
                $value = $board[$r][$c];
                if ($value === ".") {
                    continue;
                }

                $box = intdiv($r, 3) * 3 + intdiv($c, 3);
                if (isset($rows[$r][$value]) || isset($cols[$c][$value]) || isset($boxes[$box][$value])) {
                    return false;
                }

                $rows[$r][$value] = true;
                $cols[$c][$value] = true;
                $boxes[$box][$value] = true;
            }
        }

        return true;
    }
}
