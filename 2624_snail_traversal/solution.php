<?php
// LeetCode 2624 - Snail Traversal
// https://leetcode.com/problems/snail-traversal/

class Solution {
    function snail($arr, $rowsCount, $colsCount) {
        if ($rowsCount * $colsCount !== count($arr)) return [];
        $ans = [];
        for ($r = 0; $r < $rowsCount; $r++) $ans[$r] = array_fill(0, $colsCount, 0);
        $idx = 0;
        for ($c = 0; $c < $colsCount; $c++) {
            if ($c % 2 === 0) {
                for ($r = 0; $r < $rowsCount; $r++) $ans[$r][$c] = $arr[$idx++];
            } else {
                for ($r = $rowsCount - 1; $r >= 0; $r--) $ans[$r][$c] = $arr[$idx++];
            }
        }
        return $ans;
    }
}
