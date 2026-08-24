<?php
// LeetCode 0685 - Redundant Connection II
// https://leetcode.com/problems/redundant-connection-ii/

class Solution {
    function findRedundantDirectedConnection($edges) {
        $find = function (&$uf, $x) {
            while ($uf[$x] !== $x) {
                $uf[$x] = $uf[$uf[$x]];
                $x = $uf[$x];
            }
            return $x;
        };
        $n = count($edges);
        $parent = array_fill(0, $n + 1, 0);
        $cand1 = null;
        $cand2 = null;
        for ($i = 0; $i < $n; $i++) {
            $u = $edges[$i][0];
            $v = $edges[$i][1];
            if ($parent[$v] === 0) $parent[$v] = $u;
            else {
                $cand1 = [$parent[$v], $v];
                $cand2 = [$u, $v];
                $edges[$i] = [-1, -1];
                break;
            }
        }
        $uf = [];
        for ($i = 0; $i <= $n; $i++) $uf[$i] = $i;
        foreach ($edges as $edge) {
            if ($edge[0] < 0) continue;
            $pu = $find($uf, $edge[0]);
            $pv = $find($uf, $edge[1]);
            if ($pu === $pv) return $cand1 !== null ? $cand1 : [$edge[0], $edge[1]];
            $uf[$pu] = $pv;
        }
        return $cand2;
    }
}
