<?php
// LeetCode 0684 - Redundant Connection
// https://leetcode.com/problems/redundant-connection/

class Solution {
    function findRedundantConnection($edges) {
        $find = function (&$parent, $x) {
            while ($parent[$x] !== $x) {
                $parent[$x] = $parent[$parent[$x]];
                $x = $parent[$x];
            }
            return $x;
        };
        $parent = [];
        for ($i = 0; $i <= count($edges); $i++) $parent[$i] = $i;
        foreach ($edges as $edge) {
            $u = $edge[0];
            $v = $edge[1];
            $pu = $find($parent, $u);
            $pv = $find($parent, $v);
            if ($pu === $pv) return [$u, $v];
            $parent[$pu] = $pv;
        }
        return [];
    }
}
