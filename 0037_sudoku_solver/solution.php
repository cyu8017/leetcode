// LeetCode 0037 - Sudoku Solver
// https://leetcode.com/problems/sudoku-solver/

class Solution {
    /**
     * @param String[][] $board
     * @return NULL
     */
    function solveSudoku(&$board) {
        $rows = array_fill(0, 9, []);
        $cols = array_fill(0, 9, []);
        $boxes = array_fill(0, 9, []);
        $empty = [];

        for ($r = 0; $r < 9; $r++) {
            for ($c = 0; $c < 9; $c++) {
                $value = $board[$r][$c];
                if ($value === ".") {
                    $empty[] = [$r, $c];
                    continue;
                }
                $box = intdiv($r, 3) * 3 + intdiv($c, 3);
                $rows[$r][$value] = true;
                $cols[$c][$value] = true;
                $boxes[$box][$value] = true;
            }
        }

        $backtrack = function ($index) use (&$board, &$rows, &$cols, &$boxes, &$empty, &$backtrack) {
            if ($index === count($empty)) {
                return true;
            }

            [$r, $c] = $empty[$index];
            $box = intdiv($r, 3) * 3 + intdiv($c, 3);
            for ($digit = 1; $digit <= 9; $digit++) {
                $digitStr = (string) $digit;
                if (isset($rows[$r][$digitStr]) || isset($cols[$c][$digitStr]) || isset($boxes[$box][$digitStr])) {
                    continue;
                }

                $board[$r][$c] = $digitStr;
                $rows[$r][$digitStr] = true;
                $cols[$c][$digitStr] = true;
                $boxes[$box][$digitStr] = true;

                if ($backtrack($index + 1)) {
                    return true;
                }

                $board[$r][$c] = ".";
                unset($rows[$r][$digitStr], $cols[$c][$digitStr], $boxes[$box][$digitStr]);
            }

            return false;
        };

        $backtrack(0);
    }
}
