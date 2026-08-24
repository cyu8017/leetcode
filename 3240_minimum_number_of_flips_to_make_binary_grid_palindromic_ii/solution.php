<?php
// LeetCode 3240 - Minimum Number of Flips to Make Binary Grid Palindromic II
// https://leetcode.com/problems/minimum-number-of-flips-to-make-binary-grid-palindromic-ii/

class Solution {
    function minFlips($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        $ans = 0;
        for ($i = 0; $i < intdiv($m, 2); $i++) {
            for ($j = 0; $j < intdiv($n, 2); $j++) {
                $x = $m - $i - 1;
                $y = $n - $j - 1;
                $cnt1 = $grid[$i][$j] + $grid[$x][$j] + $grid[$i][$y] + $grid[$x][$y];
                $ans += min($cnt1, 4 - $cnt1);
            }
        }
        if ($m % 2 === 1 && $n % 2 === 1) $ans += $grid[intdiv($m, 2)][intdiv($n, 2)];
        $diff = 0;
        $ones = 0;
        if ($m % 2 === 1) {
            for ($j = 0; $j < intdiv($n, 2); $j++) {
                if ($grid[intdiv($m, 2)][$j] === $grid[intdiv($m, 2)][$n - $j - 1]) $ones += $grid[intdiv($m, 2)][$j] * 2;
                else $diff += 1;
            }
        }
        if ($n % 2 === 1) {
            for ($i = 0; $i < intdiv($m, 2); $i++) {
                if ($grid[$i][intdiv($n, 2)] === $grid[$m - $i - 1][intdiv($n, 2)]) $ones += $grid[$i][intdiv($n, 2)] * 2;
                else $diff += 1;
            }
        }
        if ($ones % 4 === 0 || $diff > 0) $ans += $diff;
        else $ans += 2;
        return $ans;
    }
}
