<?php
// LeetCode 1895 - Largest Magic Square
// https://leetcode.com/problems/largest-magic-square/

class Solution {
    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function largestMagicSquare($grid) {
        $rows = count($grid);
        $cols = count($grid[0]);
        $rowPrefix = array_fill(0, $rows, array_fill(0, $cols + 1, 0));
        $colPrefix = array_fill(0, $cols, array_fill(0, $rows + 1, 0));

        for ($i = 0; $i < $rows; $i++) {
            for ($j = 0; $j < $cols; $j++) {
                $rowPrefix[$i][$j + 1] = $rowPrefix[$i][$j] + $grid[$i][$j];
                $colPrefix[$j][$i + 1] = $colPrefix[$j][$i] + $grid[$i][$j];
            }
        }

        $rowSum = function ($row, $colStart, $colEnd) use ($rowPrefix) {
            return $rowPrefix[$row][$colEnd + 1] - $rowPrefix[$row][$colStart];
        };
        $colSum = function ($col, $rowStart, $rowEnd) use ($colPrefix) {
            return $colPrefix[$col][$rowEnd + 1] - $colPrefix[$col][$rowStart];
        };
        $isMagic = function ($rowStart, $colStart, $size) use (
            $grid, $rowSum, $colSum
        ) {
            $target = $rowSum($rowStart, $colStart, $colStart + $size - 1);
            for ($row = $rowStart; $row < $rowStart + $size; $row++) {
                if ($rowSum($row, $colStart, $colStart + $size - 1) !== $target) {
                    return false;
                }
            }
            for ($col = $colStart; $col < $colStart + $size; $col++) {
                if ($colSum($col, $rowStart, $rowStart + $size - 1) !== $target) {
                    return false;
                }
            }
            $diag1 = 0;
            $diag2 = 0;
            for ($offset = 0; $offset < $size; $offset++) {
                $diag1 += $grid[$rowStart + $offset][$colStart + $offset];
                $diag2 += $grid[$rowStart + $offset][$colStart + $size - 1 - $offset];
            }
            return $diag1 === $target && $diag2 === $target;
        };

        $limit = min($rows, $cols);
        for ($size = $limit; $size >= 1; $size--) {
            for ($rowStart = 0; $rowStart <= $rows - $size; $rowStart++) {
                for ($colStart = 0; $colStart <= $cols - $size; $colStart++) {
                    if ($isMagic($rowStart, $colStart, $size)) {
                        return $size;
                    }
                }
            }
        }
        return 1;
    }
}
