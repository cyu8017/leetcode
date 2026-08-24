<?php
// LeetCode 3212 - Count Submatrices With Equal Frequency of X and Y
// https://leetcode.com/problems/count-submatrices-with-equal-frequency-of-x-and-y/

class Solution {
    function numberOfSubmatrices($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        $s = [];
        for ($i = 0; $i <= $m; $i++) {
            $s[$i] = [];
            for ($j = 0; $j <= $n; $j++) $s[$i][$j] = [0, 0];
        }
        $ans = 0;
        for ($i = 1; $i <= $m; $i++) {
            for ($j = 1; $j <= $n; $j++) {
                $s[$i][$j][0] = $s[$i - 1][$j][0] + $s[$i][$j - 1][0] - $s[$i - 1][$j - 1][0];
                if ($grid[$i - 1][$j - 1] === 'X') $s[$i][$j][0]++;
                $s[$i][$j][1] = $s[$i - 1][$j][1] + $s[$i][$j - 1][1] - $s[$i - 1][$j - 1][1];
                if ($grid[$i - 1][$j - 1] === 'Y') $s[$i][$j][1]++;
                if ($s[$i][$j][0] > 0 && $s[$i][$j][0] === $s[$i][$j][1]) $ans++;
            }
        }
        return $ans;
    }
}
