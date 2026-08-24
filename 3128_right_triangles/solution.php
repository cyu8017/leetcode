<?php
// LeetCode 3128 - Right Triangles
// https://leetcode.com/problems/right-triangles/

class Solution {
    function numberOfRightTriangles($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        $rows = array_fill(0, $m, 0);
        $cols = array_fill(0, $n, 0);
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                $rows[$i] += $grid[$i][$j];
                $cols[$j] += $grid[$i][$j];
            }
        }
        $ans = 0;
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($grid[$i][$j] === 1)
                    $ans += ($rows[$i] - 1) * ($cols[$j] - 1);
            }
        }
        return $ans;
    }
}
