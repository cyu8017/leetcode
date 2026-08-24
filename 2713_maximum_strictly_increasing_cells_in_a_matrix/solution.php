<?php
// LeetCode 2713 - Maximum Strictly Increasing Cells in a Matrix
// https://leetcode.com/problems/maximum-strictly-increasing-cells-in-a-matrix/

class Solution {
    function maxIncreasingCells($mat) {
        $m = count($mat);
        $n = count($mat[0]);
        $cells = [];
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) $cells[] = [$mat[$i][$j], $i, $j];
        }
        usort($cells, function($a, $b) { return $a[0] <=> $b[0]; });
        $rowMax = array_fill(0, $m, 0);
        $colMax = array_fill(0, $n, 0);
        $dp = [];
        for ($i = 0; $i < $m; $i++) $dp[$i] = array_fill(0, $n, 0);
        $ans = 0;
        $len = count($cells);
        for ($i = 0; $i < $len; ) {
            $j = $i;
            while ($j < $len && $cells[$j][0] === $cells[$i][0]) $j++;
            $buf = [];
            for ($k = $i; $k < $j; $k++) {
                $r = $cells[$k][1];
                $c = $cells[$k][2];
                $best = max($rowMax[$r], $colMax[$c]);
                $dp[$r][$c] = $best + 1;
                $ans = max($ans, $dp[$r][$c]);
                $buf[] = [$r, $c, $dp[$r][$c]];
            }
            foreach ($buf as $t) {
                $rowMax[$t[0]] = max($rowMax[$t[0]], $t[2]);
                $colMax[$t[1]] = max($colMax[$t[1]], $t[2]);
            }
            $i = $j;
        }
        return $ans;
    }
}
