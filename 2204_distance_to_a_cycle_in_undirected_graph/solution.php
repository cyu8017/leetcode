<?php
// LeetCode 2204 - Distance to a Cycle in Undirected Graph
// https://leetcode.com/problems/distance-to-a-cycle-in-undirected-graph/

class Solution {
    function solve($n, $edges) {
        $g = array_fill(0, $n, []);
        $deg = array_fill(0, $n, 0);
        foreach ($edges as $e) {
            $g[$e[0]][] = $e[1];
            $g[$e[1]][] = $e[0];
            $deg[$e[0]]++;
            $deg[$e[1]]++;
        }
        $q = [];
        for ($i = 0; $i < $n; $i++) if ($deg[$i] === 1) $q[] = $i;
        $onCycle = array_fill(0, $n, true);
        $qi = 0;
        while ($qi < count($q)) {
            $u = $q[$qi++];
            $onCycle[$u] = false;
            foreach ($g[$u] as $v) {
                $deg[$v]--;
                if ($deg[$v] === 1) $q[] = $v;
            }
        }
        $ans = array_fill(0, $n, -1);
        $qq = [];
        for ($i = 0; $i < $n; $i++) if ($onCycle[$i]) {
            $ans[$i] = 0;
            $qq[] = $i;
        }
        $qi = 0;
        while ($qi < count($qq)) {
            $u = $qq[$qi++];
            foreach ($g[$u] as $v) if ($ans[$v] === -1) {
                $ans[$v] = $ans[$u] + 1;
                $qq[] = $v;
            }
        }
        return $ans;
    }
}
