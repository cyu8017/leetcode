<?php
// LeetCode 2246 - Longest Path With Different Adjacent Characters
// https://leetcode.com/problems/longest-path-with-different-adjacent-characters/

class Solution {
    function longestPath($parent, $s) {
        $n = count($parent);
        $g = array_fill(0, $n, []);
        for ($i = 1; $i < $n; $i++) $g[$parent[$i]][] = $i;
        $ans = 1;
        $dfs = function($u) use (&$dfs, &$ans, $g, $s) {
            $best1 = 0;
            $best2 = 0;
            foreach ($g[$u] as $v) {
                $len = $dfs($v);
                if ($s[$v] === $s[$u]) continue;
                if ($len > $best1) { $best2 = $best1; $best1 = $len; }
                else if ($len > $best2) $best2 = $len;
            }
            $ans = max($ans, 1 + $best1 + $best2);
            return 1 + $best1;
        };
        $dfs(0);
        return $ans;
    }
}
