<?php
// LeetCode 2492 - Minimum Score of a Path Between Two Cities
// https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/

class Solution {
    function minScore($n, $roads) {
        $g = array_fill(0, $n + 1, []);
        foreach ($roads as $r) {
            $g[$r[0]][] = [$r[1], $r[2]];
            $g[$r[1]][] = [$r[0], $r[2]];
        }
        $vis = array_fill(0, $n + 1, false);
        $ans = 1 << 30;
        $q = [1];
        $vis[1] = true;
        while (count($q)) {
            $u = array_shift($q);
            foreach ($g[$u] as $e) {
                $v = $e[0];
                $w = $e[1];
                if ($w < $ans) $ans = $w;
                if (!$vis[$v]) {
                    $vis[$v] = true;
                    $q[] = $v;
                }
            }
        }
        return $ans;
    }
}
