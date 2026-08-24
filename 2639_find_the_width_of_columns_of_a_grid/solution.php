<?php
// LeetCode 2639 - Find the Width of Columns of a Grid
// https://leetcode.com/problems/find-the-width-of-columns-of-a-grid/

class Solution {
    function findColumnWidth($grid) {
        $n = count($grid[0]);
        $ans = array_fill(0, $n, 0);
        $width = function($x) {
            if ($x === 0) return 1;
            $w = 0;
            if ($x < 0) { $w++; $x = -$x; }
            while ($x > 0) { $w++; $x = intdiv($x, 10); }
            return $w;
        };
        foreach ($grid as $row) {
            for ($j = 0; $j < $n; $j++) $ans[$j] = max($ans[$j], $width($row[$j]));
        }
        return $ans;
    }
}
