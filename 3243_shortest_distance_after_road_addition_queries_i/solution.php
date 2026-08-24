<?php
// LeetCode 3243 - Shortest Distance After Road Addition Queries I
// https://leetcode.com/problems/shortest-distance-after-road-addition-queries-i/

class Solution {
    private $g;
    private $n;

    function shortestDistanceAfterQueries($n, $queries) {
        $this->n = $n;
        $this->g = array_fill(0, $n, []);
        for ($i = 0; $i < $n - 1; $i++) $this->g[$i][] = $i + 1;
        $ans = [];
        foreach ($queries as $q) {
            $this->g[$q[0]][] = $q[1];
            $ans[] = $this->bfs();
        }
        return $ans;
    }

    private function bfs() {
        $q = [0];
        $vis = array_fill(0, $this->n, false);
        $vis[0] = true;
        for ($d = 0; ; $d++) {
            $k = count($q);
            while ($k-- > 0) {
                $u = array_shift($q);
                if ($u === $this->n - 1) return $d;
                foreach ($this->g[$u] as $v) {
                    if (!$vis[$v]) { $vis[$v] = true; $q[] = $v; }
                }
            }
        }
    }
}
