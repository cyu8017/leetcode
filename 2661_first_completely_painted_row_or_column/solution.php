<?php
// LeetCode 2661 - First Completely Painted Row or Column
// https://leetcode.com/problems/first-completely-painted-row-or-column/

class Solution {
    function firstCompleteIndex($arr, $mat) {
        $m = count($mat);
        $n = count($mat[0]);
        $posR = array_fill(0, $m * $n + 1, 0);
        $posC = array_fill(0, $m * $n + 1, 0);
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                $posR[$mat[$i][$j]] = $i;
                $posC[$mat[$i][$j]] = $j;
            }
        }
        $rowCnt = array_fill(0, $m, 0);
        $colCnt = array_fill(0, $n, 0);
        for ($i = 0; $i < count($arr); $i++) {
            $r = $posR[$arr[$i]];
            $c = $posC[$arr[$i]];
            $rowCnt[$r]++;
            $colCnt[$c]++;
            if ($rowCnt[$r] === $n || $colCnt[$c] === $m) return $i;
        }
        return -1;
    }
}
