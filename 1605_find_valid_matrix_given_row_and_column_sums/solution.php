<?php
// LeetCode 1605 - Find Valid Matrix Given Row and Column Sums
// https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums/

class Solution {
    /**
     * @param Integer[] $rowSum
     * @param Integer[] $colSum
     * @return Integer[][]
     */
    function restoreMatrix($rowSum, $colSum) {
        $m = count($rowSum);
        $n = count($colSum);
        $ans = array_fill(0, $m, array_fill(0, $n, 0));
        $i = $j = 0;
        while ($i < $m && $j < $n) {
            $x = min($rowSum[$i], $colSum[$j]);
            $ans[$i][$j] = $x;
            $rowSum[$i] -= $x;
            $colSum[$j] -= $x;
            if ($rowSum[$i] === 0) {
                $i++;
            }
            if ($colSum[$j] === 0) {
                $j++;
            }
        }
        return $ans;
    }
}
