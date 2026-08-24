<?php
// LeetCode 3585 - Find Weighted Median Node in Tree
// https://leetcode.com/problems/find-weighted-median-node-in-tree/

class Solution {
    function findMedian($n, $edges, $queries) {
        $g = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $g[$e[0]][] = [$e[1], $e[2]];
            $g[$e[1]][] = [$e[0], $e[2]];
        }
        $ans = array_fill(0, count($queries), 0);
        for ($qi = 0; $qi < count($queries); $qi++) {
            $u = $queries[$qi][0];
            $v = $queries[$qi][1];
            $parent = array_fill(0, $n, -2);
            $pw = array_fill(0, $n, 0);
            $parent[$u] = -1;
            $q = [$u];
            while (count($q)) {
                $x = array_shift($q);
                if ($x === $v) break;
                foreach ($g[$x] as $e) {
                    if ($parent[$e[0]] === -2) {
                        $parent[$e[0]] = $x;
                        $pw[$e[0]] = $e[1];
                        $q[] = $e[0];
                    }
                }
            }
            $nodes = [$v];
            $weights = [];
            $cur = $v;
            while ($cur !== $u) {
                $weights[] = $pw[$cur];
                $cur = $parent[$cur];
                $nodes[] = $cur;
            }
            $nodes = array_reverse($nodes);
            $weights = array_reverse($weights);
            $total = 0;
            foreach ($weights as $w) $total += $w;
            $need = intdiv($total + 1, 2);
            $sum = 0;
            $med = $u;
            for ($i = 0; $i < count($weights); $i++) {
                $sum += $weights[$i];
                $med = $nodes[$i + 1];
                if ($sum >= $need) break;
            }
            $ans[$qi] = $med;
        }
        return $ans;
    }
}
