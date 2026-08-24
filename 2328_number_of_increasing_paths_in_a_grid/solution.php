<?php
// LeetCode 2328 - Number of Increasing Paths in a Grid
// https://leetcode.com/problems/number-of-increasing-paths-in-a-grid/

class Solution {
    private $grid;
    private $dp;
    private $m;
    private $n;

    function countPaths($grid) {
        $MOD = 1000000007;
        $this->grid = $grid;
        $this->m = count($grid);
        $this->n = count($grid[0]);
        $this->dp = array_fill(0, $this->m, array_fill(0, $this->n, 0));
        $ans = 0;
        for ($i = 0; $i < $this->m; ++$i)
            for ($j = 0; $j < $this->n; ++$j)
                $ans = ($ans + $this->dfs($i, $j)) % $MOD;
        return $ans;
    }

    private function dfs($r, $c) {
        if ($this->dp[$r][$c] !== 0) return $this->dp[$r][$c];
        $MOD = 1000000007;
        $res = 1;
        $dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];
        foreach ($dirs as $d) {
            $nr = $r + $d[0];
            $nc = $c + $d[1];
            if ($nr >= 0 && $nr < $this->m && $nc >= 0 && $nc < $this->n && $this->grid[$nr][$nc] > $this->grid[$r][$c])
                $res = ($res + $this->dfs($nr, $nc)) % $MOD;
        }
        $this->dp[$r][$c] = $res;
        return $res;
    }
}
