<?php
// LeetCode 2872 - Maximum Number of K-Divisible Components
// https://leetcode.com/problems/maximum-number-of-k-divisible-components/

class Solution {
    function maxKDivisibleComponents($n, $edges, $values, $k) {
        $g = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $g[$e[0]][] = $e[1];
            $g[$e[1]][] = $e[0];
        }
        $ans = 0;
        $dfs = function($u, $p) use (&$dfs, &$g, &$values, $k, &$ans) {
            $sum = $values[$u] % $k;
            foreach ($g[$u] as $v) {
                if ($v === $p) continue;
                $sum = ($sum + $dfs($v, $u)) % $k;
            }
            if ($sum === 0) $ans++;
            return $sum;
        };
        $dfs(0, -1);
        return $ans;
    }
}
