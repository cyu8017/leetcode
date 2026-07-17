<?php
// LeetCode 1878 - Get Biggest Three Rhombus Sums in a Grid
// https://leetcode.com/problems/get-biggest-three-rhombus-sums-in-a-grid/

class Solution {
    /**
     * @param Integer[][] $grid
     * @return Integer[]
     */
    function getBiggestThree($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        $s1 = array_fill(0, $m + 1, array_fill(0, $n + 2, 0));
        $s2 = array_fill(0, $m + 1, array_fill(0, $n + 2, 0));

        for ($i = 1; $i <= $m; $i++) {
            for ($j = 1; $j <= $n; $j++) {
                $value = $grid[$i - 1][$j - 1];
                $s1[$i][$j] = $s1[$i - 1][$j - 1] + $value;
                $s2[$i][$j] = $s2[$i - 1][$j + 1] + $value;
            }
        }

        $rhombusSums = [];
        for ($i = 1; $i <= $m; $i++) {
            for ($j = 1; $j <= $n; $j++) {
                $value = $grid[$i - 1][$j - 1];
                $limit = min($i - 1, $m - $i, $j - 1, $n - $j);
                $rhombusSums[$value] = true;
                for ($k = 1; $k <= $limit; $k++) {
                    $a = $s1[$i + $k][$j] - $s1[$i][$j - $k];
                    $b = $s1[$i][$j + $k] - $s1[$i - $k][$j];
                    $c = $s2[$i][$j - $k] - $s2[$i - $k][$j];
                    $d = $s2[$i + $k][$j] - $s2[$i][$j + $k];
                    $sum = $a + $b + $c + $d - $grid[$i + $k - 1][$j - 1] + $grid[$i - $k - 1][$j - 1];
                    $rhombusSums[$sum] = true;
                }
            }
        }

        $values = array_keys($rhombusSums);
        rsort($values, SORT_NUMERIC);
        return array_slice($values, 0, 3);
    }
}
