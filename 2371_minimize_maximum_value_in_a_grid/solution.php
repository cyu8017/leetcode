<?php
// LeetCode 2371 - Minimize Maximum Value in a Grid
// https://leetcode.com/problems/minimize-maximum-value-in-a-grid/

class Solution {
    function minScore($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        $arr = [];
        for ($i = 0; $i < $m; $i++)
            for ($j = 0; $j < $n; $j++)
                $arr[] = [$grid[$i][$j], $i, $j];
        usort($arr, function($a, $b) { return $a[0] - $b[0]; });
        $rowMax = array_fill(0, $m, 0);
        $colMax = array_fill(0, $n, 0);
        $ans = array_fill(0, $m, array_fill(0, $n, 0));
        foreach ($arr as $cel) {
            $val = max($rowMax[$cel[1]], $colMax[$cel[2]]) + 1;
            $ans[$cel[1]][$cel[2]] = $val;
            $rowMax[$cel[1]] = $val;
            $colMax[$cel[2]] = $val;
        }
        return $ans;
    }
}
