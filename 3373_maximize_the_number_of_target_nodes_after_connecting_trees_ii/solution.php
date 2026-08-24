<?php
// LeetCode 3373 - Maximize the Number of Target Nodes After Connecting Trees II
// https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-ii/

class Solution {
    function buildTree($n, $edges) {
        $g = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $g[$e[0]][] = $e[1];
            $g[$e[1]][] = $e[0];
        }
        return $g;
    }

    function bipartiteCount($g, &$color) {
        $n = count($g);
        $color = array_fill(0, $n, -1);
        $q = [0];
        $color[0] = 0;
        $cnt = [1, 0];
        $head = 0;
        while ($head < count($q)) {
            $u = $q[$head++];
            foreach ($g[$u] as $v) {
                if ($color[$v] === -1) {
                    $color[$v] = $color[$u] ^ 1;
                    $cnt[$color[$v]]++;
                    $q[] = $v;
                }
            }
        }
        return $cnt;
    }

    function maxTargetNodes($edges1, $edges2) {
        $n = count($edges1) + 1;
        $m = count($edges2) + 1;
        $g1 = $this->buildTree($n, $edges1);
        $g2 = $this->buildTree($m, $edges2);
        $color1 = [];
        $color2 = [];
        $c1 = $this->bipartiteCount($g1, $color1);
        $c2 = $this->bipartiteCount($g2, $color2);
        $best2 = max($c2[0], $c2[1]);
        $ans = [];
        for ($i = 0; $i < $n; $i++) $ans[$i] = $c1[$color1[$i]] + $best2;
        return $ans;
    }
}
