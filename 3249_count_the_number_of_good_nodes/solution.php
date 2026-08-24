<?php
// LeetCode 3249 - Count the Number of Good Nodes
// https://leetcode.com/problems/count-the-number-of-good-nodes/

class Solution {
    private $g;
    private $ans;

    function countGoodNodes($edges) {
        $n = count($edges) + 1;
        $this->g = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $this->g[$e[0]][] = $e[1];
            $this->g[$e[1]][] = $e[0];
        }
        $this->ans = 0;
        $this->dfs(0, -1);
        return $this->ans;
    }

    private function dfs($a, $fa) {
        $pre = -1;
        $cnt = 1;
        $ok = 1;
        foreach ($this->g[$a] as $b) {
            if ($b !== $fa) {
                $cur = $this->dfs($b, $a);
                $cnt += $cur;
                if ($pre < 0) $pre = $cur;
                else if ($pre !== $cur) $ok = 0;
            }
        }
        $this->ans += $ok;
        return $cnt;
    }
}
