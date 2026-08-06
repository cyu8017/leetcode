<?php

class Solution {
    /**
     * @param Integer[][] $points
     * @return Integer
     */
    function maxPoints($points) {
        $m = count($points);
        $n = count($points[0]);
        $dp = $points[0];
        for ($r = 1; $r < $m; $r++) {
            $left = array_fill(0, $n, 0);
            $right = array_fill(0, $n, 0);
            $left[0] = $dp[0];
            for ($c = 1; $c < $n; $c++) {
                $left[$c] = max($left[$c - 1] - 1, $dp[$c]);
            }
            $right[$n - 1] = $dp[$n - 1];
            for ($c = $n - 2; $c >= 0; $c--) {
                $right[$c] = max($right[$c + 1] - 1, $dp[$c]);
            }
            $next = [];
            for ($c = 0; $c < $n; $c++) {
                $next[$c] = $points[$r][$c] + max($left[$c], $right[$c]);
            }
            $dp = $next;
        }
        return max($dp);
    }
}
