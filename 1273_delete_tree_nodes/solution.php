<?php
// LeetCode 1273 - Delete Tree Nodes
// https://leetcode.com/problems/delete-tree-nodes/

class Solution {
    /**
     * @param Integer $nodes
     * @param Integer[] $parent
     * @param Integer[] $value
     * @return Integer
     */
    function deleteTreeNodes($nodes, $parent, $value) {
        $children = array_fill(0, $nodes, []);
        for ($node = 1; $node < $nodes; $node++) {
            $children[$parent[$node]][] = $node;
        }
        $dfs = function ($node) use (&$dfs, $children, $value) {
            $total = $value[$node];
            $count = 1;
            foreach ($children[$node] as $child) {
                [$childSum, $childCount] = $dfs($child);
                $total += $childSum;
                $count += $childCount;
            }
            return [$total, $total === 0 ? 0 : $count];
        };
        return $dfs(0)[1];
    }
}
