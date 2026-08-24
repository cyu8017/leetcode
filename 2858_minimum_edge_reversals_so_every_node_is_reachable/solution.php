<?php
// LeetCode 2858 - Minimum Edge Reversals So Every Node Is Reachable
// https://leetcode.com/problems/minimum-edge-reversals-so-every-node-is-reachable/

class Solution {
    function minEdgeReversals($n, $edges) {
        $g = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $g[$e[0]][] = [$e[1], 0];
            $g[$e[1]][] = [$e[0], 1];
        }
        $ans = array_fill(0, $n, 0);
        $dfs1 = function($u, $p) use (&$dfs1, &$g, &$ans) {
            foreach ($g[$u] as $ew) {
                $v = $ew[0];
                $ww = $ew[1];
                if ($v === $p) continue;
                $ans[0] += $ww;
                $dfs1($v, $u);
            }
        };
        $dfs2 = function($u, $p) use (&$dfs2, &$g, &$ans) {
            foreach ($g[$u] as $ew) {
                $v = $ew[0];
                $ww = $ew[1];
                if ($v === $p) continue;
                $ans[$v] = $ww === 0 ? $ans[$u] + 1 : $ans[$u] - 1;
                $dfs2($v, $u);
            }
        };
        $dfs1(0, -1);
        $dfs2(0, -1);
        return $ans;
    }
}
