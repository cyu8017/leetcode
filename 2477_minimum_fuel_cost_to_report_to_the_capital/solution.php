<?php
// LeetCode 2477 - Minimum Fuel Cost to Report to the Capital
// https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital/

class Solution {
    function minimumFuelCost($roads, $seats) {
        $n = count($roads) + 1;
        $g = array_fill(0, $n, []);
        foreach ($roads as $e) {
            $g[$e[0]][] = $e[1];
            $g[$e[1]][] = $e[0];
        }
        $ans = 0;
        $dfs = function ($u, $p) use (&$dfs, &$g, $seats, &$ans) {
            $people = 1;
            foreach ($g[$u] as $v) {
                if ($v !== $p) $people += $dfs($v, $u);
            }
            if ($u !== 0) $ans += intdiv($people + $seats - 1, $seats);
            return $people;
        };
        $dfs(0, -1);
        return $ans;
    }
}
