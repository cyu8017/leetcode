<?php
// LeetCode 0743 - Network Delay Time
// https://leetcode.com/problems/network-delay-time/

class Solution {
    function networkDelayTime($times, $n, $k) {
        $graph = array_fill(0, $n + 1, []);
        foreach ($times as $edge) $graph[$edge[0]][] = [$edge[1], $edge[2]];
        $INF = intdiv(PHP_INT_MAX, 4);
        $dist = array_fill(0, $n + 1, $INF);
        $dist[$k] = 0;
        $heap = [[0, $k]];
        while (count($heap) > 0) {
            usort($heap, function ($a, $b) { return $a[0] - $b[0]; });
            $item = array_shift($heap);
            $d = $item[0];
            $node = $item[1];
            if ($d > $dist[$node]) continue;
            foreach ($graph[$node] as $e) {
                $nd = $d + $e[1];
                if ($nd < $dist[$e[0]]) {
                    $dist[$e[0]] = $nd;
                    $heap[] = [$nd, $e[0]];
                }
            }
        }
        $ans = 0;
        for ($i = 1; $i <= $n; $i++) $ans = max($ans, $dist[$i]);
        return $ans === $INF ? -1 : $ans;
    }
}
