<?php
// LeetCode 3459 - Length of Longest V-Shaped Diagonal Segment
// https://leetcode.com/problems/length-of-longest-v-shaped-diagonal-segment/

class Solution {
    function lenOfVDiagonal($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        $dirs = [[1, 1], [1, -1], [-1, -1], [-1, 1]];
        $nextDir = [1, 2, 3, 0];
        $memo = [];
        $key = function($i, $j, $d, $turned, $expect) {
            return (((($i * 101 + $j) * 5 + $d) * 3 + $turned) * 5 + $expect);
        };
        $dfs = null;
        $dfs = function($i, $j, $d, $turned, $expect) use (&$dfs, $m, $n, $grid, $dirs, $nextDir, &$memo, $key) {
            if ($i < 0 || $j < 0 || $i >= $m || $j >= $n || $grid[$i][$j] !== $expect) return 0;
            $k = $key($i, $j, $d, $turned, $expect);
            if (isset($memo[$k])) return $memo[$k];
            $ni = $i + $dirs[$d][0];
            $nj = $j + $dirs[$d][1];
            $nx = $expect === 2 ? 0 : 2;
            $best = 1 + $dfs($ni, $nj, $d, $turned, $nx);
            if ($turned === 0) {
                $nd = $nextDir[$d];
                $ti = $i + $dirs[$nd][0];
                $tj = $j + $dirs[$nd][1];
                $cand = 1 + $dfs($ti, $tj, $nd, 1, $nx);
                if ($cand > $best) $best = $cand;
            }
            $memo[$k] = $best;
            return $best;
        };
        $ans = 0;
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($grid[$i][$j] !== 1) continue;
                for ($d = 0; $d < 4; $d++) {
                    $ni = $i + $dirs[$d][0];
                    $nj = $j + $dirs[$d][1];
                    $best = 1 + $dfs($ni, $nj, $d, 0, 2);
                    if ($best > $ans) $ans = $best;
                }
                if ($ans < 1) $ans = 1;
            }
        }
        return $ans;
    }
}
