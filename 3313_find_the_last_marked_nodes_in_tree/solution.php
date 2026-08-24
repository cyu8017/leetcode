<?php
// LeetCode 3313 - Find the Last Marked Nodes in Tree
// https://leetcode.com/problems/find-the-last-marked-nodes-in-tree/

class Solution {
    function lastMarkedNodes($edges) {
        $n = count($edges) + 1;
        $g = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $g[$e[0]][] = $e[1];
            $g[$e[1]][] = $e[0];
        }
        $ru = $this->bfs(0, $g, $n);
        $u = $ru[0];
        $ru = $this->bfs($u, $g, $n);
        $v = $ru[0];
        $du = $ru[1];
        $dv = $this->bfs($v, $g, $n)[1];
        $ans = [];
        for ($i = 0; $i < $n; $i++) $ans[$i] = $du[$i] >= $dv[$i] ? $u : $v;
        return $ans;
    }

    function bfs($start, $g, $n) {
        $dist = array_fill(0, $n, -1);
        $q = [$start];
        $dist[$start] = 0;
        $far = $start;
        $head = 0;
        while ($head < count($q)) {
            $u = $q[$head++];
            if ($dist[$u] > $dist[$far]) $far = $u;
            foreach ($g[$u] as $v) {
                if ($dist[$v] === -1) {
                    $dist[$v] = $dist[$u] + 1;
                    $q[] = $v;
                }
            }
        }
        return [$far, $dist];
    }
}
