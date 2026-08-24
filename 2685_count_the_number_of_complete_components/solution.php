<?php
// LeetCode 2685 - Count the Number of Complete Components
// https://leetcode.com/problems/count-the-number-of-complete-components/

class Solution {
    function countCompleteComponents($n, $edges) {
        $g = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $g[$e[0]][] = $e[1];
            $g[$e[1]][] = $e[0];
        }
        $vis = array_fill(0, $n, false);
        $ans = 0;
        $dfs = function($u, &$nodes) use (&$dfs, &$g, &$vis) {
            $vis[$u] = true;
            $nodes[] = $u;
            foreach ($g[$u] as $v) if (!$vis[$v]) $dfs($v, $nodes);
        };
        for ($i = 0; $i < $n; $i++) {
            if ($vis[$i]) continue;
            $nodes = [];
            $dfs($i, $nodes);
            $ecount = 0;
            foreach ($nodes as $u) $ecount += count($g[$u]);
            $ecount = intdiv($ecount, 2);
            $sz = count($nodes);
            if ($ecount === intdiv($sz * ($sz - 1), 2)) $ans++;
        }
        return $ans;
    }
}
