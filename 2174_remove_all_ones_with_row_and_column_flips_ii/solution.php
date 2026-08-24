<?php
// LeetCode 2174 - Remove All Ones With Row and Column Flips II
// https://leetcode.com/problems/remove-all-ones-with-row-and-column-flips-ii/

class Solution {
    private $grid;
    private $ones;
    private $m;
    private $n;
    private $ans;

    private function dfs($idx, $flips) {
        if ($flips >= $this->ans) return;
        while ($idx < count($this->ones) && $this->grid[$this->ones[$idx][0]][$this->ones[$idx][1]] === 0) $idx++;
        if ($idx === count($this->ones)) {
            $this->ans = $flips;
            return;
        }
        $r = $this->ones[$idx][0];
        $c = $this->ones[$idx][1];
        $changed = [];
        for ($j = 0; $j < $this->n; $j++) {
            if ($this->grid[$r][$j] === 1) {
                $this->grid[$r][$j] = 0;
                $changed[] = [$r, $j];
            }
        }
        $this->dfs($idx + 1, $flips + 1);
        foreach ($changed as $p) $this->grid[$p[0]][$p[1]] = 1;
        $changed = [];
        for ($i = 0; $i < $this->m; $i++) {
            if ($this->grid[$i][$c] === 1) {
                $this->grid[$i][$c] = 0;
                $changed[] = [$i, $c];
            }
        }
        $this->dfs($idx + 1, $flips + 1);
        foreach ($changed as $p) $this->grid[$p[0]][$p[1]] = 1;
    }

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function removeOnes($grid) {
        $this->grid = $grid;
        $this->m = count($grid);
        $this->n = count($grid[0]);
        $this->ones = [];
        for ($i = 0; $i < $this->m; $i++)
            for ($j = 0; $j < $this->n; $j++)
                if ($grid[$i][$j] === 1) $this->ones[] = [$i, $j];
        if (!$this->ones) return 0;
        $this->ans = $this->m + $this->n;
        $this->dfs(0, 0);
        return $this->ans;
    }
}
