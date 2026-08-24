<?php
// LeetCode 2467 - Most Profitable Path in a Tree
// https://leetcode.com/problems/most-profitable-path-in-a-tree/

class Solution {
    function mostProfitablePath($edges, $bob, $amount) {
        $n = count($amount);
        $g = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $g[$e[0]][] = $e[1];
            $g[$e[1]][] = $e[0];
        }
        $bobTime = array_fill(0, $n, $n);
        $findBob = function ($u, $p, $t) use (&$findBob, &$g, &$bobTime) {
            if ($u === 0) {
                $bobTime[$u] = $t;
                return true;
            }
            foreach ($g[$u] as $v) {
                if ($v === $p) continue;
                if ($findBob($v, $u, $t + 1)) {
                    $bobTime[$u] = $t;
                    return true;
                }
            }
            return false;
        };
        $findBob($bob, -1, 0);
        $ans = PHP_INT_MIN;
        $dfs = function ($u, $p, $t, $income) use (&$dfs, &$g, $amount, &$bobTime, &$ans) {
            $cur = $amount[$u];
            if ($t > $bobTime[$u]) $cur = 0;
            elseif ($t === $bobTime[$u]) $cur = intdiv($cur, 2);
            $income += $cur;
            $isLeaf = true;
            foreach ($g[$u] as $v) {
                if ($v !== $p) {
                    $isLeaf = false;
                    $dfs($v, $u, $t + 1, $income);
                }
            }
            if ($isLeaf && $income > $ans) $ans = $income;
        };
        $dfs(0, -1, 0, 0);
        return $ans;
    }
}
