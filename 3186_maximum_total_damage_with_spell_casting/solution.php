<?php
// LeetCode 3186 - Maximum Total Damage With Spell Casting
// https://leetcode.com/problems/maximum-total-damage-with-spell-casting/

class Solution {
    private $power;
    private $cnt;
    private $nxt;
    private $f;
    private $n;

    function maximumTotalDamage($power) {
        $this->n = count($power);
        sort($power);
        $this->power = $power;
        $this->cnt = [];
        $this->nxt = array_fill(0, $this->n, 0);
        $this->f = array_fill(0, $this->n, 0);
        for ($i = 0; $i < $this->n; $i++) {
            $this->cnt[$power[$i]] = ($this->cnt[$power[$i]] ?? 0) + 1;
            $this->nxt[$i] = $this->lowerBound($power[$i] + 3);
        }
        return $this->dfs(0);
    }

    private function lowerBound($x) {
        $lo = 0;
        $hi = $this->n;
        while ($lo < $hi) {
            $mid = ($lo + $hi) >> 1;
            if ($this->power[$mid] < $x) $lo = $mid + 1;
            else $hi = $mid;
        }
        return $lo;
    }

    private function dfs($i) {
        if ($i >= $this->n) return 0;
        if ($this->f[$i] !== 0) return $this->f[$i];
        $a = $this->dfs($i + $this->cnt[$this->power[$i]]);
        $b = $this->power[$i] * $this->cnt[$this->power[$i]] + $this->dfs($this->nxt[$i]);
        return $this->f[$i] = max($a, $b);
    }
}
