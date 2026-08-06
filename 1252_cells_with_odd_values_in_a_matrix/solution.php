<?php
// LeetCode 1252 - Cells with Odd Values in a Matrix
// https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/

class Solution {
    /**
     * @param Integer $m
     * @param Integer $n
     * @param Integer[][] $indices
     * @return Integer
     */
    function oddCells($m, $n, $indices) {
        $rows = array_fill(0, $m, 0);
        $cols = array_fill(0, $n, 0);
        foreach ($indices as [$r, $c]) {
            $rows[$r] ^= 1;
            $cols[$c] ^= 1;
        }
        $ans = 0;
        for ($r = 0; $r < $m; $r++) {
            for ($c = 0; $c < $n; $c++) {
                $ans += $rows[$r] ^ $cols[$c];
            }
        }
        return $ans;
    }
}
