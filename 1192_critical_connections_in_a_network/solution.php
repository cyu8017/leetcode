<?php
// LeetCode 1192 - Critical Connections in a Network
// https://leetcode.com/problems/critical-connections-in-a-network/

class Solution {
    /**
     * @param Integer $n
     * @param Integer[][] $connections
     * @return Integer[][]
     */
    function criticalConnections($n, $connections) {
        $graph = array_fill(0, $n, []);
        foreach ($connections as [$a, $b]) {
            $graph[$a][] = $b;
            $graph[$b][] = $a;
        }
        $disc = array_fill(0, $n, -1);
        $low = array_fill(0, $n, -1);
        $time = 0;
        $bridges = [];
        $dfs = function ($node, $parent) use (&$dfs, &$graph, &$disc, &$low, &$time, &$bridges) {
            $disc[$node] = $low[$node] = $time++;
            foreach ($graph[$node] as $nxt) {
                if ($nxt === $parent) continue;
                if ($disc[$nxt] === -1) {
                    $dfs($nxt, $node);
                    $low[$node] = min($low[$node], $low[$nxt]);
                    if ($low[$nxt] > $disc[$node]) $bridges[] = [$node, $nxt];
                } else {
                    $low[$node] = min($low[$node], $disc[$nxt]);
                }
            }
        };
        $dfs(0, -1);
        return array_map(fn($e) => [min($e[0], $e[1]), max($e[0], $e[1])], $bridges);
    }
}
