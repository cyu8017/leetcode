<?php
// LeetCode 0750 - Number Of Corner Rectangles
// https://leetcode.com/problems/number-of-corner-rectangles/

class Solution {
    function countCornerRectangles($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        $ans = 0;
        for ($i = 0; $i < $m; $i++) {
            for ($j = $i + 1; $j < $m; $j++) {
                $count = 0;
                for ($c = 0; $c < $n; $c++) if ($grid[$i][$c] === 1 && $grid[$j][$c] === 1) $count++;
                $ans += intdiv($count * ($count - 1), 2);
            }
        }
        return $ans;
    }
}
