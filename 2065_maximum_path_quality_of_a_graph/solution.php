<?php
// LeetCode 2065 - Maximum Path Quality of a Graph
// https://leetcode.com/problems/maximum-path-quality-of-a-graph/

class Solution {
    /**
     * @param Integer[] $values
     * @param Integer[][] $edges
     * @param Integer $maxTime
     * @return Integer
     */
    function maximalPathQuality($values, $edges, $maxTime) {
        $n = count($values);
        $g = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $g[$e[0]][] = [$e[1], $e[2]];
            $g[$e[1]][] = [$e[0], $e[2]];
        }
        $ans = 0;
        $vis = array_fill(0, $n, 0);
        $dfs = null;
        $dfs = function ($u, $time, $quality) use (&$dfs, &$ans, &$vis, $g, $values, $maxTime) {
            if ($time > $maxTime) return;
            $first = $vis[$u] === 0;
            if ($first) $quality += $values[$u];
            $vis[$u]++;
            if ($u === 0) $ans = max($ans, $quality);
            foreach ($g[$u] as $e) $dfs($e[0], $time + $e[1], $quality);
            $vis[$u]--;
        };
        $dfs(0, 0, 0);
        return $ans;
    }
}
