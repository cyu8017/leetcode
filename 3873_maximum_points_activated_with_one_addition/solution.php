<?php
// LeetCode 3873 - Maximum Points Activated With One Addition
// https://leetcode.com/problems/maximum-points-activated-with-one-addition/

class Solution {
    public $p;
    public $size;
    function find($x) {
        if (!isset($this->p[$x])) { $this->p[$x] = $x; $this->size[$x] = 1; }
        if ($this->p[$x] !== $x) $this->p[$x] = $this->find($this->p[$x]);
        return $this->p[$x];
    }
    function unite($a, $b) {
        $pa = $this->find($a);
        $pb = $this->find($b);
        if ($pa === $pb) return false;
        if ($this->size[$pa] > $this->size[$pb]) {
            $this->p[$pb] = $pa;
            $this->size[$pa] += $this->size[$pb];
        } else {
            $this->p[$pa] = $pb;
            $this->size[$pb] += $this->size[$pa];
        }
        return true;
    }
    function maxActivated($points) {
        $this->p = [];
        $this->size = [];
        $m = 3000000000;
        foreach ($points as $pt) $this->unite($pt[0], $pt[1] + $m);
        $cnt = [];
        foreach ($points as $pt) {
            $r = $this->find($pt[0]);
            $cnt[$r] = ($cnt[$r] ?? 0) + 1;
        }
        $mx1 = 0;
        $mx2 = 0;
        foreach ($cnt as $x) {
            if ($mx1 < $x) { $mx2 = $mx1; $mx1 = $x; }
            else if ($mx2 < $x) $mx2 = $x;
        }
        return $mx1 + $mx2 + 1;
    }
}
