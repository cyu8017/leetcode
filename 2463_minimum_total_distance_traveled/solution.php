<?php
// LeetCode 2463 - Minimum Total Distance Traveled
// https://leetcode.com/problems/minimum-total-distance-traveled/

class Solution {
    function minimumTotalDistance($robot, $factory) {
        $robots = $robot;
        sort($robots);
        usort($factory, function ($a, $b) { return $a[0] <=> $b[0]; });
        $m = count($robots);
        $pos = [];
        foreach ($factory as $f) {
            for ($c = 0; $c < $f[1]; $c++) $pos[] = $f[0];
        }
        $n = count($pos);
        $INF = intdiv(PHP_INT_MAX, 4);
        $dp = [];
        for ($i = 0; $i <= $m; $i++) $dp[] = array_fill(0, $n + 1, $INF);
        for ($j = 0; $j <= $n; $j++) $dp[0][$j] = 0;
        for ($i = 1; $i <= $m; $i++) {
            for ($j = $i; $j <= $n; $j++) {
                $dp[$i][$j] = $dp[$i][$j - 1];
                $diff = $robots[$i - 1] - $pos[$j - 1];
                if ($diff < 0) $diff = -$diff;
                if ($dp[$i - 1][$j - 1] + $diff < $dp[$i][$j]) $dp[$i][$j] = $dp[$i - 1][$j - 1] + $diff;
            }
        }
        return $dp[$m][$n];
    }
}
