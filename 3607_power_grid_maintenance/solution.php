<?php
// LeetCode 3607 - Power Grid Maintenance
// https://leetcode.com/problems/power-grid-maintenance/

class Solution {
    private $parent;

    private function find($x) {
        if ($this->parent[$x] !== $x) $this->parent[$x] = $this->find($this->parent[$x]);
        return $this->parent[$x];
    }

    private function unite($a, $b) {
        $ra = $this->find($a);
        $rb = $this->find($b);
        if ($ra !== $rb) {
            if ($ra < $rb) $this->parent[$rb] = $ra;
            else $this->parent[$ra] = $rb;
        }
    }

    function processQueries($c, $connections, $queries) {
        $this->parent = [];
        for ($i = 0; $i <= $c; $i++) $this->parent[$i] = $i;
        foreach ($connections as $e) $this->unite($e[0], $e[1]);
        $online = array_fill(0, $c + 1, true);
        $comp = [];
        for ($i = 1; $i <= $c; $i++) {
            $r = $this->find($i);
            if (!isset($comp[$r])) $comp[$r] = [];
            $comp[$r][] = $i;
        }
        foreach ($comp as &$ids) sort($ids);
        unset($ids);
        $ptr = [];
        $ans = [];
        foreach ($queries as $q) {
            $t = $q[0];
            $x = $q[1];
            if ($t === 2) {
                $online[$x] = false;
                continue;
            }
            if ($online[$x]) {
                $ans[] = $x;
                continue;
            }
            $r = $this->find($x);
            $ids = $comp[$r];
            $p = $ptr[$r] ?? 0;
            while ($p < count($ids) && !$online[$ids[$p]]) $p++;
            $ptr[$r] = $p;
            $ans[] = $p < count($ids) ? $ids[$p] : -1;
        }
        return $ans;
    }
}
