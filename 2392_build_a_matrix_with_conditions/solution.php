<?php
// LeetCode 2392 - Build a Matrix With Conditions
// https://leetcode.com/problems/build-a-matrix-with-conditions/

class Solution {
    function buildMatrix($k, $rowConditions, $colConditions) {
        $rowOrder = $this->topo($k, $rowConditions);
        $colOrder = $this->topo($k, $colConditions);
        if ($rowOrder === null || $colOrder === null) return [];
        $rowPos = array_fill(0, $k + 1, 0);
        $colPos = array_fill(0, $k + 1, 0);
        for ($i = 0; $i < $k; $i++) {
            $rowPos[$rowOrder[$i]] = $i;
            $colPos[$colOrder[$i]] = $i;
        }
        $ans = array_fill(0, $k, array_fill(0, $k, 0));
        for ($v = 1; $v <= $k; $v++) $ans[$rowPos[$v]][$colPos[$v]] = $v;
        return $ans;
    }

    private function topo($k, $conds) {
        $g = array_fill(0, $k + 1, []);
        $indeg = array_fill(0, $k + 1, 0);
        foreach ($conds as $c) {
            $g[$c[0]][] = $c[1];
            $indeg[$c[1]]++;
        }
        $q = [];
        for ($i = 1; $i <= $k; $i++) if ($indeg[$i] === 0) $q[] = $i;
        $order = [];
        $head = 0;
        while ($head < count($q)) {
            $u = $q[$head++];
            $order[] = $u;
            foreach ($g[$u] as $v) {
                if (--$indeg[$v] === 0) $q[] = $v;
            }
        }
        if (count($order) !== $k) return null;
        return $order;
    }
}
