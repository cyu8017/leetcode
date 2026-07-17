<?php
// LeetCode 1740 - Find Distance in a Binary Tree
// https://leetcode.com/problems/find-distance-in-a-binary-tree/

class TreeNode {
    public $val = 0;
    public $left = null;
    public $right = null;
    function __construct($val = 0, $left = null, $right = null) {
        $this->val = $val;
        $this->left = $left;
        $this->right = $right;
    }
}

class Solution {
    /**
     * @param TreeNode $root
     * @param Integer $p
     * @param Integer $q
     * @return Integer
     */
    function findDistance($root, $p, $q) {
        $graph = [];
        $this->dfs($root, null, $graph);
        $queue = [[$p, 0]];
        $seen = [$p => true];
        while (!empty($queue)) {
            [$node, $dist] = array_shift($queue);
            if ($node === $q) {
                return $dist;
            }
            foreach ($graph[$node] as $nei) {
                if (!isset($seen[$nei])) {
                    $seen[$nei] = true;
                    $queue[] = [$nei, $dist + 1];
                }
            }
        }
        return -1;
    }

    private function dfs($node, $parent, &$graph) {
        if ($node === null) {
            return;
        }
        if (!isset($graph[$node->val])) {
            $graph[$node->val] = [];
        }
        if ($parent !== null) {
            $graph[$node->val][] = $parent->val;
            $graph[$parent->val][] = $node->val;
        }
        $this->dfs($node->left, $node, $graph);
        $this->dfs($node->right, $node, $graph);
    }
}
