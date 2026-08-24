<?php
// LeetCode 0802 - Find Eventual Safe States
// https://leetcode.com/problems/find-eventual-safe-states/

class Solution {
    /**
     * @param Integer[][] $graph
     * @return Integer[]
     */
    function eventualSafeNodes($graph) {
        $n = count($graph);
        $color = array_fill(0, $n, 0);
        $dfs = function($node) use (&$dfs, $graph, &$color) {
            if ($color[$node] !== 0) return $color[$node] === 2;
            $color[$node] = 1;
            foreach ($graph[$node] as $nei) {
                if (!$dfs($nei)) return false;
            }
            $color[$node] = 2;
            return true;
        };
        $ans = [];
        for ($i = 0; $i < $n; $i++) if ($dfs($i)) $ans[] = $i;
        return $ans;
    }
}
