<?php
// LeetCode 0894 - All Possible Full Binary Trees
// https://leetcode.com/problems/all-possible-full-binary-trees/

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
    function allPossibleFBT($n) {
        $memo = [];
        $build = function ($nodes) use (&$build, &$memo) {
            if (array_key_exists($nodes, $memo)) return $memo[$nodes];
            $res = [];
            if ($nodes % 2 === 0) {
                $memo[$nodes] = $res;
                return $res;
            }
            if ($nodes === 1) {
                $res[] = new TreeNode(0);
                $memo[$nodes] = $res;
                return $res;
            }
            for ($left = 1; $left < $nodes; $left += 2) {
                $right = $nodes - 1 - $left;
                foreach ($build($left) as $L) {
                    foreach ($build($right) as $R) {
                        $res[] = new TreeNode(0, $L, $R);
                    }
                }
            }
            $memo[$nodes] = $res;
            return $res;
        };
        $trees = $build($n);
        $toList = function ($root) {
            if ($root === null) return [];
            $result = [];
            $queue = [$root];
            while ($queue) {
                $node = array_shift($queue);
                if ($node === null) {
                    $result[] = null;
                    continue;
                }
                $result[] = $node->val;
                $queue[] = $node->left;
                $queue[] = $node->right;
            }
            while ($result && $result[count($result) - 1] === null) array_pop($result);
            return $result;
        };
        $out = [];
        foreach ($trees as $t) $out[] = $toList($t);
        return $out;
    }
}
