<?php
// LeetCode 2852 - Sum of Remoteness of All Cells
// https://leetcode.com/problems/sum-of-remoteness-of-all-cells/

class Solution {
    function sumRemoteness($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        $seen = [];
        for ($i = 0; $i < $m; $i++) $seen[$i] = array_fill(0, $n, false);
        $dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];
        $total = 0;
        for ($i = 0; $i < $m; $i++)
            for ($j = 0; $j < $n; $j++)
                if ($grid[$i][$j] !== -1) $total += $grid[$i][$j];
        $ans = 0;
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($grid[$i][$j] === -1 || $seen[$i][$j]) continue;
                $q = [[$i, $j]];
                $seen[$i][$j] = true;
                $sum = 0;
                $cnt = 0;
                $qi = 0;
                while ($qi < count($q)) {
                    $x = $q[$qi][0];
                    $y = $q[$qi][1];
                    $qi++;
                    $sum += $grid[$x][$y];
                    $cnt++;
                    foreach ($dirs as $d) {
                        $ni = $x + $d[0];
                        $nj = $y + $d[1];
                        if ($ni >= 0 && $nj >= 0 && $ni < $m && $nj < $n && !$seen[$ni][$nj] && $grid[$ni][$nj] !== -1) {
                            $seen[$ni][$nj] = true;
                            $q[] = [$ni, $nj];
                        }
                    }
                }
                $ans += ($total - $sum) * $cnt;
            }
        }
        return $ans;
    }
}
