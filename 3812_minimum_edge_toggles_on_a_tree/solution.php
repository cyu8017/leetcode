<?php
// LeetCode 3812 - Minimum Edge Toggles on a Tree
// https://leetcode.com/problems/minimum-edge-toggles-on-a-tree/

class Solution {
    function minimumFlips($n, $edges, $start, $target) {
        $g = array_fill(0, $n, []);
        for ($i = 0; $i < $n - 1; $i++) {
            $a = $edges[$i][0];
            $b = $edges[$i][1];
            $g[$a][] = [$b, $i];
            $g[$b][] = [$a, $i];
        }
        $ans = [];
        $dfs = function($a, $fa) use (&$dfs, &$ans, $g, $start, $target) {
            $rev = $start[$a] !== $target[$a];
            foreach ($g[$a] as $e) {
                $b = $e[0];
                $i = $e[1];
                if ($b !== $fa && $dfs($b, $a)) {
                    $ans[] = $i;
                    $rev = !$rev;
                }
            }
            return $rev;
        };
        if ($dfs(0, -1)) return [-1];
        sort($ans);
        return $ans;
    }
}
