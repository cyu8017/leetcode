<?php
// LeetCode 0863 - All Nodes Distance K in Binary Tree
// https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

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
     * @param TreeNode $target
     * @param Integer $k
     * @return Integer[]
     */
    function distanceK($root, $target, $k) {
        $graph = [];
        $add = function($a, $b) use (&$graph) {
            $ida = spl_object_id($a);
            if (!isset($graph[$ida])) $graph[$ida] = [];
            $graph[$ida][] = $b;
        };
        $build = function($node, $parent) use (&$build, $add) {
            if ($node === null) return;
            if ($parent !== null) {
                $add($node, $parent);
                $add($parent, $node);
            }
            $build($node->left, $node);
            $build($node->right, $node);
        };
        $build($root, null);
        $queue = [$target];
        $seen = [spl_object_id($target) => true];
        $dist = 0;
        $qi = 0;
        while ($qi < count($queue)) {
            if ($dist === $k) {
                $vals = [];
                for ($j = $qi; $j < count($queue); $j++) $vals[] = $queue[$j]->val;
                return $vals;
            }
            $size = count($queue) - $qi;
            for ($i = 0; $i < $size; $i++) {
                $node = $queue[$qi++];
                foreach ($graph[spl_object_id($node)] ?? [] as $nei) {
                    $id = spl_object_id($nei);
                    if (!isset($seen[$id])) {
                        $seen[$id] = true;
                        $queue[] = $nei;
                    }
                }
            }
            $dist++;
        }
        return [];
    }
}
