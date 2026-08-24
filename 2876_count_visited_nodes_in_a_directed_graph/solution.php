<?php
// LeetCode 2876 - Count Visited Nodes in a Directed Graph
// https://leetcode.com/problems/count-visited-nodes-in-a-directed-graph/

class Solution {
    function countVisitedNodes($edgesList) {
        $n = count($edgesList);
        $edges = $edgesList;
        $ans = array_fill(0, $n, 0);
        $state = array_fill(0, $n, 0);
        $stack = [];
        $dfs = function($u) use (&$dfs, &$edges, &$ans, &$state, &$stack) {
            $state[$u] = 1;
            $stack[] = $u;
            $v = $edges[$u];
            if ($state[$v] === 0) $dfs($v);
            else if ($state[$v] === 1) {
                $idx = count($stack) - 1;
                while ($stack[$idx] !== $v) $idx--;
                $cyc = count($stack) - $idx;
                for ($i = $idx; $i < count($stack); $i++) $ans[$stack[$i]] = $cyc;
            }
            if ($ans[$u] === 0) $ans[$u] = $ans[$edges[$u]] + 1;
            $state[$u] = 2;
            array_pop($stack);
        };
        for ($i = 0; $i < $n; $i++) if ($state[$i] === 0) $dfs($i);
        return $ans;
    }
}
