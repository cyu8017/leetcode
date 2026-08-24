<?php
// LeetCode 3070 - Count Submatrices With Top-Left Element and Sum Less Than k
// https://leetcode.com/problems/count-submatrices-with-top-left-element-and-sum-less-than-k/

class Solution {
    function countSubmatrices($grid, $k) {
        $n = count($grid);
        $m = count($grid[0]);
        $ans = 0;
        $s = [];
        for ($i = 0; $i <= $n; $i++) $s[] = array_fill(0, $m + 1, 0);
        for ($i = 0; $i < $n; $i++) {
            for ($j = 0; $j < $m; $j++) {
                $s[$i + 1][$j + 1] = $s[$i + 1][$j] + $s[$i][$j + 1] - $s[$i][$j] + $grid[$i][$j];
                if ($s[$i + 1][$j + 1] <= $k) $ans++;
            }
        }
        return $ans;
    }
}
