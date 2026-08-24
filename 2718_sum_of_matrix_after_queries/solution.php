<?php
// LeetCode 2718 - Sum of Matrix After Queries
// https://leetcode.com/problems/sum-of-matrix-after-queries/

class Solution {
    function matrixSumQueries($n, $queries) {
        $rowDone = array_fill(0, $n, false);
        $colDone = array_fill(0, $n, false);
        $rowsLeft = $n;
        $colsLeft = $n;
        $ans = 0;
        for ($i = count($queries) - 1; $i >= 0; $i--) {
            $type = $queries[$i][0];
            $idx = $queries[$i][1];
            $val = $queries[$i][2];
            if ($type === 0) {
                if (!$rowDone[$idx]) {
                    $ans += $val * $colsLeft;
                    $rowDone[$idx] = true;
                    $rowsLeft--;
                }
            } else {
                if (!$colDone[$idx]) {
                    $ans += $val * $rowsLeft;
                    $colDone[$idx] = true;
                    $colsLeft--;
                }
            }
        }
        return $ans;
    }
}
