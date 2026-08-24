<?php
// LeetCode 2146 - K Highest Ranked Items Within a Price Range
// https://leetcode.com/problems/k-highest-ranked-items-within-a-price-range/

class Solution {
    /**
     * @param Integer[][] $grid
     * @param Integer[] $pricing
     * @param Integer[] $start
     * @param Integer $k
     * @return Integer[][]
     */
    function highestRankedKItems($grid, $pricing, $start, $k) {
        $m = count($grid);
        $n = count($grid[0]);
        $low = $pricing[0];
        $high = $pricing[1];
        $vis = [];
        for ($i = 0; $i < $m; $i++) $vis[$i] = array_fill(0, $n, false);
        $q = [[$start[0], $start[1], 0]];
        $vis[$start[0]][$start[1]] = true;
        $cands = [];
        $dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];
        while ($q) {
            [$r, $c, $d] = array_shift($q);
            if ($grid[$r][$c] >= $low && $grid[$r][$c] <= $high)
                $cands[] = [$d, $grid[$r][$c], $r, $c];
            foreach ($dirs as $dir) {
                $nr = $r + $dir[0];
                $nc = $c + $dir[1];
                if ($nr >= 0 && $nr < $m && $nc >= 0 && $nc < $n && !$vis[$nr][$nc] && $grid[$nr][$nc] !== 0) {
                    $vis[$nr][$nc] = true;
                    $q[] = [$nr, $nc, $d + 1];
                }
            }
        }
        usort($cands, function($a, $b) {
            if ($a[0] !== $b[0]) return $a[0] - $b[0];
            if ($a[1] !== $b[1]) return $a[1] - $b[1];
            if ($a[2] !== $b[2]) return $a[2] - $b[2];
            return $a[3] - $b[3];
        });
        if ($k > count($cands)) $k = count($cands);
        $ans = [];
        for ($i = 0; $i < $k; $i++) $ans[] = [$cands[$i][2], $cands[$i][3]];
        return $ans;
    }
}
