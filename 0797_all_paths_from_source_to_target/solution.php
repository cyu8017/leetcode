<?php
// LeetCode 0797 - All Paths From Source to Target
// https://leetcode.com/problems/all-paths-from-source-to-target/

class Solution {
    /**
     * @param Integer[][] $graph
     * @return Integer[][]
     */
    function allPathsSourceTarget($graph) {
        $target = count($graph) - 1;
        $answer = [];
        $path = [0];
        $dfs = function($node) use (&$dfs, $graph, $target, &$answer, &$path) {
            if ($node === $target) {
                $answer[] = $path;
                return;
            }
            foreach ($graph[$node] as $nei) {
                $path[] = $nei;
                $dfs($nei);
                array_pop($path);
            }
        };
        $dfs(0);
        return $answer;
    }
}
