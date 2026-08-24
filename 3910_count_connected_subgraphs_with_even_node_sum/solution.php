<?php
// LeetCode 3910 - Count Connected Subgraphs With Even Node Sum
// https://leetcode.com/problems/count-connected-subgraphs-with-even-node-sum/

class Solution {
    public $g;
    public $vis;
    function dfs($u) {
        $this->vis |= 1 << $u;
        foreach ($this->g[$u] as $v) {
            if ((($this->vis >> $v) & 1) === 0) $this->dfs($v);
        }
    }
    function evenSumSubgraphs($nums, $edges) {
        $n = count($nums);
        $this->g = [];
        for ($i = 0; $i < $n; $i++) $this->g[$i] = [];
        foreach ($edges as $e) {
            $this->g[$e[0]][] = $e[1];
            $this->g[$e[1]][] = $e[0];
        }
        $m = (1 << $n) - 1;
        $ans = 0;
        for ($sub = 1; $sub <= $m; $sub++) {
            $s = 0;
            for ($i = 0; $i < $n; $i++) {
                if ((($sub >> $i) & 1) !== 0) $s += $nums[$i];
            }
            if ($s % 2 !== 0) continue;
            $this->vis = $m ^ $sub;
            $start = 0;
            for ($b = 31; $b >= 0; $b--) {
                if (($sub >> $b) & 1) { $start = $b; break; }
            }
            $this->dfs($start);
            if ($this->vis === $m) $ans++;
        }
        return $ans;
    }
}
