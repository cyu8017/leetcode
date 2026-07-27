<?php
// LeetCode 1631 - Path With Minimum Effort
// https://leetcode.com/problems/path-with-minimum-effort/

class Solution {
    /**
     * @param Integer[][] $heights
     * @return Integer
     */
    function minimumEffortPath($heights) {
        $m = count($heights);
        $n = count($heights[0]);
        $dist = array_fill(0, $m, array_fill(0, $n, PHP_INT_MAX));
        $dist[0][0] = 0;
        $heap = new SplMinHeap();
        $heap->insert([0, 0, 0]);
        $dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];
        while (!$heap->isEmpty()) {
            [$effort, $i, $j] = $heap->extract();
            if ($i === $m - 1 && $j === $n - 1) {
                return $effort;
            }
            if ($effort !== $dist[$i][$j]) {
                continue;
            }
            foreach ($dirs as $d) {
                $x = $i + $d[0];
                $y = $j + $d[1];
                if ($x >= 0 && $x < $m && $y >= 0 && $y < $n) {
                    $nd = max($effort, abs($heights[$i][$j] - $heights[$x][$y]));
                    if ($nd < $dist[$x][$y]) {
                        $dist[$x][$y] = $nd;
                        $heap->insert([$nd, $x, $y]);
                    }
                }
            }
        }
        return 0;
    }
}
