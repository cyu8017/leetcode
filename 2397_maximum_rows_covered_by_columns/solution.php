<?php
// LeetCode 2397 - Maximum Rows Covered by Columns
// https://leetcode.com/problems/maximum-rows-covered-by-columns/

class Solution {
    private $matrix;
    private $m;
    private $n;
    private $numSelect;
    private $ans;

    function maximumRows($matrix, $numSelect) {
        $this->matrix = $matrix;
        $this->m = count($matrix);
        $this->n = count($matrix[0]);
        $this->numSelect = $numSelect;
        $this->ans = 0;
        $this->dfs(0, 0, 0);
        return $this->ans;
    }

    private function dfs($col, $chosen, $mask) {
        if ($chosen === $this->numSelect) {
            $covered = 0;
            for ($i = 0; $i < $this->m; $i++) {
                $ok = true;
                for ($j = 0; $j < $this->n; $j++) {
                    if ($this->matrix[$i][$j] === 1 && (($mask >> $j) & 1) === 0) {
                        $ok = false;
                        break;
                    }
                }
                if ($ok) $covered++;
            }
            $this->ans = max($this->ans, $covered);
            return;
        }
        if ($col === $this->n) return;
        $this->dfs($col + 1, $chosen + 1, $mask | (1 << $col));
        $this->dfs($col + 1, $chosen, $mask);
    }
}
