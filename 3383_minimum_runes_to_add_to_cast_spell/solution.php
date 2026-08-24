<?php
// LeetCode 3383 - Minimum Runes to Add to Cast Spell
// https://leetcode.com/problems/minimum-runes-to-add-to-cast-spell/

class Solution {
    public $g;
    public $rg;
    public $vis;
    public $order;
    public $comp;
    public $cid;

    function dfs1($u) {
        $this->vis[$u] = true;
        foreach ($this->g[$u] as $v) if (!$this->vis[$v]) $this->dfs1($v);
        $this->order[] = $u;
    }

    function dfs2($u) {
        $this->comp[$u] = $this->cid;
        foreach ($this->rg[$u] as $v) if ($this->comp[$v] === -1) $this->dfs2($v);
    }

    function minRunesToAdd($n, $crystals, $flowFrom, $flowTo) {
        $this->g = array_fill(0, $n, []);
        $this->rg = array_fill(0, $n, []);
        for ($i = 0; $i < count($flowFrom); $i++) {
            $a = $flowFrom[$i];
            $b = $flowTo[$i];
            $this->g[$a][] = $b;
            $this->rg[$b][] = $a;
        }
        $this->vis = array_fill(0, $n, false);
        $this->order = [];
        for ($i = 0; $i < $n; $i++) if (!$this->vis[$i]) $this->dfs1($i);
        $this->comp = array_fill(0, $n, -1);
        $this->cid = 0;
        for ($i = $n - 1; $i >= 0; $i--) {
            $u = $this->order[$i];
            if ($this->comp[$u] === -1) {
                $this->dfs2($u);
                $this->cid++;
            }
        }
        $hasCrystal = array_fill(0, $this->cid, false);
        foreach ($crystals as $c) $hasCrystal[$this->comp[$c]] = true;
        $indeg = array_fill(0, $this->cid, 0);
        for ($u = 0; $u < $n; $u++) {
            foreach ($this->g[$u] as $v) {
                if ($this->comp[$u] !== $this->comp[$v]) $indeg[$this->comp[$v]]++;
            }
        }
        $ans = 0;
        for ($i = 0; $i < $this->cid; $i++) {
            if ($indeg[$i] === 0 && !$hasCrystal[$i]) $ans++;
        }
        return $ans;
    }
}
