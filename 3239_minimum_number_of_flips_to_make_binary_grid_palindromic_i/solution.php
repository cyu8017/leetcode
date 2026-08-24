<?php
// LeetCode 3239 - Minimum Number of Flips to Make Binary Grid Palindromic I
// https://leetcode.com/problems/minimum-number-of-flips-to-make-binary-grid-palindromic-i/

class Solution {
    function minFlips($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        $cnt1 = 0;
        $cnt2 = 0;
        foreach ($grid as $row) {
            for ($j = 0; $j * 2 < $n; $j++) if ($row[$j] !== $row[$n - $j - 1]) $cnt1++;
        }
        for ($j = 0; $j < $n; $j++) {
            for ($i = 0; $i * 2 < $m; $i++) if ($grid[$i][$j] !== $grid[$m - $i - 1][$j]) $cnt2++;
        }
        return min($cnt1, $cnt2);
    }
}
