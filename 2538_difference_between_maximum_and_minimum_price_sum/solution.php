<?php
// LeetCode 2538 - Difference Between Maximum and Minimum Price Sum
// https://leetcode.com/problems/difference-between-maximum-and-minimum-price-sum/

class Solution {
    function maxOutput($n, $edges, $price) {
        $g = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $g[$e[0]][] = $e[1];
            $g[$e[1]][] = $e[0];
        }
        $ans = 0;
        $dfs = function($u, $p) use (&$dfs, &$g, $price, &$ans) {
            $maxChild = 0;
            foreach ($g[$u] as $v) {
                if ($v === $p) continue;
                $child = $dfs($v, $u);
                if ($child > $maxChild) $maxChild = $child;
                if ($child > $ans) $ans = $child;
            }
            return $price[$u] + $maxChild;
        };
        $dfs(0, -1);
        return $ans;
    }
}
