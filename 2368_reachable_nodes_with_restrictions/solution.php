<?php
// LeetCode 2368 - Reachable Nodes With Restrictions
// https://leetcode.com/problems/reachable-nodes-with-restrictions/

class Solution {
    function reachableNodes($n, $edges, $restricted) {
        $ban = [];
        foreach ($restricted as $x) $ban[$x] = true;
        $g = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $g[$e[0]][] = $e[1];
            $g[$e[1]][] = $e[0];
        }
        $ans = 0;
        $vis = array_fill(0, $n, false);
        $q = [0];
        $vis[0] = true;
        while (count($q) > 0) {
            $u = array_shift($q);
            $ans++;
            foreach ($g[$u] as $v) {
                if (!$vis[$v] && !isset($ban[$v])) {
                    $vis[$v] = true;
                    $q[] = $v;
                }
            }
        }
        return $ans;
    }
}
