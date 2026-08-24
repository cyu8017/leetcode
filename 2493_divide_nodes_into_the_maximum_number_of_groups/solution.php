<?php
// LeetCode 2493 - Divide Nodes Into the Maximum Number of Groups
// https://leetcode.com/problems/divide-nodes-into-the-maximum-number-of-groups/

class Solution {
    function magnificentSets($n, $edges) {
        $g = array_fill(0, $n + 1, []);
        foreach ($edges as $e) {
            $g[$e[0]][] = $e[1];
            $g[$e[1]][] = $e[0];
        }
        $bfsDepth = function ($start) use ($n, &$g) {
            $dist = array_fill(0, $n + 1, -1);
            $q = [$start];
            $dist[$start] = 1;
            $best = 1;
            while (count($q)) {
                $u = array_shift($q);
                if ($dist[$u] > $best) $best = $dist[$u];
                foreach ($g[$u] as $v) {
                    if ($dist[$v] === -1) {
                        $dist[$v] = $dist[$u] + 1;
                        $q[] = $v;
                    }
                }
            }
            return $best;
        };
        $color = array_fill(0, $n + 1, -1);
        $components = [];
        for ($i = 1; $i <= $n; $i++) {
            if ($color[$i] !== -1) continue;
            $comp = [];
            $q = [$i];
            $color[$i] = 0;
            $bipartite = true;
            while (count($q)) {
                $u = array_shift($q);
                $comp[] = $u;
                foreach ($g[$u] as $v) {
                    if ($color[$v] === -1) {
                        $color[$v] = $color[$u] ^ 1;
                        $q[] = $v;
                    } elseif ($color[$v] === $color[$u]) {
                        $bipartite = false;
                    }
                }
            }
            if (!$bipartite) return -1;
            $components[] = $comp;
        }
        $ans = 0;
        foreach ($components as $comp) {
            $best = 0;
            foreach ($comp as $u) $best = max($best, $bfsDepth($u));
            $ans += $best;
        }
        return $ans;
    }
}
