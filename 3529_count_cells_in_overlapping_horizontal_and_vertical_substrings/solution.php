<?php
// LeetCode 3529 - Count Cells in Overlapping Horizontal and Vertical Substrings
// https://leetcode.com/problems/count-cells-in-overlapping-horizontal-and-vertical-substrings/

class Solution {
    function countCells($grid, $pattern) {
        $m = count($grid);
        $n = count($grid[0]);
        $row = '';
        $col = '';
        for ($i = 0; $i < $m; $i++) for ($j = 0; $j < $n; $j++) $row .= $grid[$i][$j];
        for ($j = 0; $j < $n; $j++) for ($i = 0; $i < $m; $i++) $col .= $grid[$i][$j];
        $hMark = [];
        $vMark = [];
        for ($i = 0; $i < $m; $i++) {
            $hMark[$i] = array_fill(0, $n, false);
            $vMark[$i] = array_fill(0, $n, false);
        }
        $plen = strlen($pattern);
        $rlen = strlen($row);
        for ($i = 0; $i + $plen <= $rlen; $i++) {
            if (substr($row, $i, $plen) === $pattern) {
                for ($t = 0; $t < $plen; $t++) {
                    $pos = $i + $t;
                    $hMark[intdiv($pos, $n)][$pos % $n] = true;
                }
            }
        }
        $clen = strlen($col);
        for ($i = 0; $i + $plen <= $clen; $i++) {
            if (substr($col, $i, $plen) === $pattern) {
                for ($t = 0; $t < $plen; $t++) {
                    $pos = $i + $t;
                    $vMark[$pos % $m][intdiv($pos, $m)] = true;
                }
            }
        }
        $ans = 0;
        for ($i = 0; $i < $m; $i++) for ($j = 0; $j < $n; $j++)
            if ($hMark[$i][$j] && $vMark[$i][$j]) $ans++;
        return $ans;
    }
}
