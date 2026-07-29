<?php
// LeetCode 1059 - All Paths from Source Lead to Destination
// https://leetcode.com/problems/all-paths-from-source-lead-to-destination/

class Solution {
    /**
     * @param Integer $n
     * @param Integer[][] $edges
     * @param Integer $source
     * @param Integer $destination
     * @return Boolean
     */
    function leadsToDestination($n, $edges, $source, $destination) {
        $graph = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $graph[$e[0]][] = $e[1];
        }
        $state = array_fill(0, $n, 0);
        $dfs = null;
        $dfs = function ($node) use (&$dfs, &$graph, &$state, $destination) {
            if (count($graph[$node]) === 0) {
                return $node === $destination;
            }
            if ($state[$node] === 1) {
                return false;
            }
            if ($state[$node] === 2) {
                return true;
            }
            $state[$node] = 1;
            foreach ($graph[$node] as $nxt) {
                if (!$dfs($nxt)) {
                    return false;
                }
            }
            $state[$node] = 2;
            return true;
        };
        return $dfs($source);
    }
}
