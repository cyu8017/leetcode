<?php
// LeetCode 2608 - Shortest Cycle in a Graph
// https://leetcode.com/problems/shortest-cycle-in-a-graph/

class Solution {
    function findShortestCycle($n, $edges) {
        $g = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $g[$e[0]][] = $e[1];
            $g[$e[1]][] = $e[0];
        }
        $INF = 1000000000;
        $ans = $INF;
        for ($start = 0; $start < $n; $start++) {
            $dist = array_fill(0, $n, -1);
            $parent = array_fill(0, $n, -1);
            $q = [$start];
            $dist[$start] = 0;
            while ($q) {
                $u = array_shift($q);
                foreach ($g[$u] as $v) {
                    if ($dist[$v] < 0) {
                        $dist[$v] = $dist[$u] + 1;
                        $parent[$v] = $u;
                        $q[] = $v;
                    } else if ($parent[$u] !== $v) {
                        $c = $dist[$u] + $dist[$v] + 1;
                        if ($c < $ans) $ans = $c;
                    }
                }
            }
        }
        return $ans === $INF ? -1 : $ans;
    }
}
