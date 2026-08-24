<?php
// LeetCode 2322 - Minimum Score After Removals on a Tree
// https://leetcode.com/problems/minimum-score-after-removals-on-a-tree/

class Solution {
    private $g;
    private $nums;
    private $xorv;
    private $inT;
    private $outT;
    private $time;

    function minimumScore($nums, $edges) {
        $n = count($nums);
        $this->nums = $nums;
        $this->g = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $this->g[$e[0]][] = $e[1];
            $this->g[$e[1]][] = $e[0];
        }
        $this->xorv = array_fill(0, $n, 0);
        $this->inT = array_fill(0, $n, 0);
        $this->outT = array_fill(0, $n, 0);
        $this->time = 0;
        $this->dfs(0, -1);
        $total = $this->xorv[0];
        $ans = PHP_INT_MAX;
        for ($i = 1; $i < $n; ++$i) {
            for ($j = $i + 1; $j < $n; ++$j) {
                if ($this->isAncestor($i, $j)) {
                    $a = $this->xorv[$j];
                    $b = $this->xorv[$i] ^ $this->xorv[$j];
                    $c = $total ^ $this->xorv[$i];
                } elseif ($this->isAncestor($j, $i)) {
                    $a = $this->xorv[$i];
                    $b = $this->xorv[$j] ^ $this->xorv[$i];
                    $c = $total ^ $this->xorv[$j];
                } else {
                    $a = $this->xorv[$i];
                    $b = $this->xorv[$j];
                    $c = $total ^ $this->xorv[$i] ^ $this->xorv[$j];
                }
                $mx = max($a, max($b, $c));
                $mn = min($a, min($b, $c));
                $ans = min($ans, $mx - $mn);
            }
        }
        return $ans;
    }

    private function dfs($u, $p) {
        $this->inT[$u] = $this->time++;
        $this->xorv[$u] = $this->nums[$u];
        foreach ($this->g[$u] as $v) if ($v !== $p) {
            $this->dfs($v, $u);
            $this->xorv[$u] ^= $this->xorv[$v];
        }
        $this->outT[$u] = $this->time;
    }

    private function isAncestor($a, $b) {
        return $this->inT[$a] <= $this->inT[$b] && $this->outT[$b] <= $this->outT[$a];
    }
}
