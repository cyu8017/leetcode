<?php
// LeetCode 2123 - Minimum Operations to Remove Adjacent Ones in Matrix
// https://leetcode.com/problems/minimum-operations-to-remove-adjacent-ones-in-matrix/

class Solution {
    private $g;
    private $match;

    private function dfs($u, &$seen) {
        foreach ($this->g[$u] as $v) {
            if ($seen[$v]) continue;
            $seen[$v] = true;
            if ($this->match[$v] === -1 || $this->dfs($this->match[$v], $seen)) {
                $this->match[$v] = $u;
                return true;
            }
        }
        return false;
    }

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function minimumOperations($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        $id = [];
        for ($i = 0; $i < $m; $i++) $id[$i] = array_fill(0, $n, -1);
        $cnt = 0;
        for ($i = 0; $i < $m; $i++)
            for ($j = 0; $j < $n; $j++)
                if ($grid[$i][$j] === 1) $id[$i][$j] = $cnt++;
        $this->g = array_fill(0, $cnt, []);
        $dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]];
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($grid[$i][$j] !== 1 || ($i + $j) % 2 !== 0) continue;
                $u = $id[$i][$j];
                foreach ($dirs as $d) {
                    $ni = $i + $d[0];
                    $nj = $j + $d[1];
                    if ($ni >= 0 && $nj >= 0 && $ni < $m && $nj < $n && $grid[$ni][$nj] === 1)
                        $this->g[$u][] = $id[$ni][$nj];
                }
            }
        }
        $this->match = array_fill(0, $cnt, -1);
        $ans = 0;
        for ($u = 0; $u < $cnt; $u++) {
            $ok = false;
            for ($i = 0; $i < $m && !$ok; $i++)
                for ($j = 0; $j < $n; $j++)
                    if ($id[$i][$j] === $u && ($i + $j) % 2 === 0) { $ok = true; break; }
            if (!$ok) continue;
            $seen = array_fill(0, $cnt, false);
            if ($this->dfs($u, $seen)) $ans++;
        }
        return $ans;
    }
}
