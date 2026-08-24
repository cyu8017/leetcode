<?php
// LeetCode 3882 - Minimum XOR Path in a Grid
// https://leetcode.com/problems/minimum-xor-path-in-a-grid/

class Solution {
    function minXor($grid) {
        $rows = count($grid);
        $cols = count($grid[0]);
        $dp = [];
        for ($c = 0; $c < $cols; $c++) $dp[$c] = array_fill(0, 1024, false);
        for ($row = 0; $row < $rows; $row++) {
            $left = array_fill(0, 1024, false);
            for ($col = 0; $col < $cols; $col++) {
                $next = array_fill(0, 1024, false);
                $value = $grid[$row][$col];
                if ($row === 0 && $col === 0) {
                    $next[$value] = true;
                } else {
                    for ($xorv = 0; $xorv < 1024; $xorv++) {
                        if ($dp[$col][$xorv] || $left[$xorv]) $next[$xorv ^ $value] = true;
                    }
                }
                $dp[$col] = $next;
                $left = $next;
            }
        }
        for ($xorv = 0; $xorv < 1024; $xorv++) {
            if ($dp[$cols - 1][$xorv]) return $xorv;
        }
        return -1;
    }
}
