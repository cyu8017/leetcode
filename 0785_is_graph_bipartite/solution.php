<?php
// LeetCode 0785 - Is Graph Bipartite?
// https://leetcode.com/problems/is-graph-bipartite/

class Solution {
    /**
     * @param Integer[][] $graph
     * @return Boolean
     */
    function isBipartite($graph) {
        $n = count($graph);
        $color = array_fill(0, $n, -1);
        $dfs = function($node, $c) use (&$dfs, &$color, $graph) {
            $color[$node] = $c;
            foreach ($graph[$node] as $nei) {
                if ($color[$nei] === -1) {
                    if (!$dfs($nei, $c ^ 1)) return false;
                } elseif ($color[$nei] === $c) {
                    return false;
                }
            }
            return true;
        };
        for ($node = 0; $node < $n; $node++) {
            if ($color[$node] === -1 && !$dfs($node, 0)) return false;
        }
        return true;
    }
}
