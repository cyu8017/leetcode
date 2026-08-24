<?php
// LeetCode 3241 - Time Taken to Mark All Nodes
// https://leetcode.com/problems/time-taken-to-mark-all-nodes/

class Solution {
    private $tree;
    private $dp;
    private $ans;

    function timeTaken($edges) {
        $n = count($edges) + 1;
        $this->ans = array_fill(0, $n, 0);
        $this->tree = array_fill(0, $n, []);
        $this->dp = [];
        for ($i = 0; $i < $n; $i++) $this->dp[$i] = [[0, 0], [0, 0]];
        foreach ($edges as $e) {
            $this->tree[$e[0]][] = $e[1];
            $this->tree[$e[1]][] = $e[0];
        }
        $this->dfs(0, -1);
        $this->reroot(0, -1, 0);
        return $this->ans;
    }

    private function getTime($u) {
        return $u % 2 === 0 ? 2 : 1;
    }

    private function dfs($u, $prev) {
        $t1 = [0, 0];
        $t2 = [0, 0];
        foreach ($this->tree[$u] as $v) {
            if ($v === $prev) continue;
            $t = $this->dfs($v, $u) + $this->getTime($v);
            if ($t >= $t1[1]) { $t2 = $t1; $t1 = [$v, $t]; }
            else if ($t > $t2[1]) $t2 = [$v, $t];
        }
        $this->dp[$u][0] = $t1;
        $this->dp[$u][1] = $t2;
        return $t1[1];
    }

    private function reroot($u, $prev, $maxTime) {
        $this->ans[$u] = $maxTime;
        if ($this->dp[$u][0][1] > $this->ans[$u]) $this->ans[$u] = $this->dp[$u][0][1];
        foreach ($this->tree[$u] as $v) {
            if ($v === $prev) continue;
            $side = $this->dp[$u][0][1];
            if ($this->dp[$u][0][0] === $v) $side = $this->dp[$u][1][1];
            $newMax = max($maxTime, $side);
            $this->reroot($v, $u, $this->getTime($u) + $newMax);
        }
    }
}
