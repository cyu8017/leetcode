<?php
// LeetCode 3820 - Pythagorean Distance Nodes in a Tree
// https://leetcode.com/problems/pythagorean-distance-nodes-in-a-tree/

class Solution {
    function specialNodes($n, $edges, $x, $y, $z) {
        $g = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $g[$e[0]][] = $e[1];
            $g[$e[1]][] = $e[0];
        }
        $bfs = function($start) use ($n, $g) {
            $dist = array_fill(0, $n, 1000000000);
            $q = [$start];
            $dist[$start] = 0;
            for ($qi = 0; $qi < count($q); $qi++) {
                $u = $q[$qi];
                foreach ($g[$u] as $v) {
                    if ($dist[$v] > $dist[$u] + 1) {
                        $dist[$v] = $dist[$u] + 1;
                        $q[] = $v;
                    }
                }
            }
            return $dist;
        };
        $d1 = $bfs($x);
        $d2 = $bfs($y);
        $d3 = $bfs($z);
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            $a = [$d1[$i], $d2[$i], $d3[$i]];
            sort($a);
            $x0 = $a[0]; $x1 = $a[1]; $x2 = $a[2];
            if ($x0 * $x0 + $x1 * $x1 === $x2 * $x2) $ans++;
        }
        return $ans;
    }
}
