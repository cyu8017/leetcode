<?php
// LeetCode 2925 - Maximum Score After Applying Operations on a Tree
// https://leetcode.com/problems/maximum-score-after-applying-operations-on-a-tree/

class Solution {
    function maximumScoreAfterOperations($edges, $values) {
        $n = count($values);
        $g = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $g[$e[0]][] = $e[1];
            $g[$e[1]][] = $e[0];
        }
        $total = 0;
        foreach ($values as $v) $total += $v;
        $dfs = function($u, $p) use (&$dfs, &$g, &$values) {
            $sumKids = 0;
            $isLeaf = true;
            foreach ($g[$u] as $v) {
                if ($v === $p) continue;
                $isLeaf = false;
                $sumKids += $dfs($v, $u);
            }
            if ($isLeaf) return $values[$u];
            return $values[$u] < $sumKids ? $values[$u] : $sumKids;
        };
        return $total - $dfs(0, -1);
    }
}
