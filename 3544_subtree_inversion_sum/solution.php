<?php
// LeetCode 3544 - Subtree Inversion Sum
// https://leetcode.com/problems/subtree-inversion-sum/

class Solution {
    private $graph;
    private $parent;
    private $nums;
    private $k;
    private $memo;

    private function dp($u, $steps, $inv) {
        $key = $u . ',' . $steps . ',' . ($inv ? 1 : 0);
        if (isset($this->memo[$key])) return $this->memo[$key];
        $num = $this->nums[$u];
        if ($inv) $num = -$num;
        $negNum = -$num;
        foreach ($this->graph[$u] as $v) {
            if ($v === $this->parent[$u]) continue;
            $this->parent[$v] = $u;
            $ns = $steps + 1;
            if ($ns > $this->k) $ns = $this->k;
            $num += $this->dp($v, $ns, $inv);
            if ($steps === $this->k) $negNum += $this->dp($v, 1, !$inv);
        }
        $res = $num;
        if ($steps === $this->k && $negNum > $res) $res = $negNum;
        return $this->memo[$key] = $res;
    }

    function subtreeInversionSum($edges, $nums, $k) {
        $n = count($edges) + 1;
        $this->graph = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $this->graph[$e[0]][] = $e[1];
            $this->graph[$e[1]][] = $e[0];
        }
        $this->parent = array_fill(0, $n, -1);
        $this->nums = $nums;
        $this->k = $k;
        $this->memo = [];
        return $this->dp(0, $k, false);
    }
}
