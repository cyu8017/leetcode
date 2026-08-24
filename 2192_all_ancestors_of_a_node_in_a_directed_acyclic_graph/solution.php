<?php
// LeetCode 2192 - All Ancestors of a Node in a Directed Acyclic Graph
// https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution {
    /**
     * @param Integer $n
     * @param Integer[][] $edges
     * @return Integer[][]
     */
    function getAncestors($n, $edges) {
        $g = array_fill(0, $n, []);
        $indeg = array_fill(0, $n, 0);
        foreach ($edges as $e) {
            $g[$e[0]][] = $e[1];
            $indeg[$e[1]]++;
        }
        $anc = array_fill(0, $n, []);
        $q = [];
        for ($i = 0; $i < $n; $i++) if ($indeg[$i] === 0) $q[] = $i;
        while ($q) {
            $u = array_shift($q);
            foreach ($g[$u] as $v) {
                $anc[$v][$u] = true;
                foreach ($anc[$u] as $x => $_) $anc[$v][$x] = true;
                if (--$indeg[$v] === 0) $q[] = $v;
            }
        }
        $ans = [];
        for ($i = 0; $i < $n; $i++) {
            $keys = array_keys($anc[$i]);
            sort($keys);
            $ans[] = $keys;
        }
        return $ans;
    }
}
