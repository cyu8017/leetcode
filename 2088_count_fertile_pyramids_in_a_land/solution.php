<?php
// LeetCode 2088 - Count Fertile Pyramids in a Land
// https://leetcode.com/problems/count-fertile-pyramids-in-a-land/

class Solution {
    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function countPyramids($grid) {
        $count = function ($g) {
            $m = count($g);
            $n = count($g[0]);
            $dp = [];
            for ($i = 0; $i < $m; $i++) $dp[$i] = $g[$i];
            $ans = 0;
            for ($i = $m - 2; $i >= 0; $i--) {
                for ($j = 1; $j < $n - 1; $j++) {
                    if ($g[$i][$j] === 1) {
                        $dp[$i][$j] = 1 + min($dp[$i + 1][$j - 1], $dp[$i + 1][$j], $dp[$i + 1][$j + 1]);
                        $ans += $dp[$i][$j] - 1;
                    }
                }
            }
            return $ans;
        };
        $ans = $count($grid);
        $m = count($grid);
        $rev = [];
        for ($i = 0; $i < $m; $i++) $rev[$i] = $grid[$m - 1 - $i];
        return $ans + $count($rev);
    }
}
