<?php
// LeetCode 0847 - Shortest Path Visiting All Nodes
// https://leetcode.com/problems/shortest-path-visiting-all-nodes/

class Solution {
    /**
     * @param Integer[][] $graph
     * @return Integer
     */
    function shortestPathLength($graph) {
        $n = count($graph);
        $target = (1 << $n) - 1;
        $queue = [];
        $seen = [];
        for ($i = 0; $i < $n; $i++) {
            $queue[] = [$i, 1 << $i, 0];
            $seen[($i << 20) | (1 << $i)] = true;
        }
        $qi = 0;
        while ($qi < count($queue)) {
            $node = $queue[$qi][0];
            $mask = $queue[$qi][1];
            $dist = $queue[$qi][2];
            $qi++;
            if ($mask === $target) return $dist;
            foreach ($graph[$node] as $nxt) {
                $nmask = $mask | (1 << $nxt);
                $state = ($nxt << 20) | $nmask;
                if (!isset($seen[$state])) {
                    $seen[$state] = true;
                    $queue[] = [$nxt, $nmask, $dist + 1];
                }
            }
        }
        return -1;
    }
}
