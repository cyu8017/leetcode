<?php
// LeetCode 0366 - Find Leaves of Binary Tree
// https://leetcode.com/problems/find-leaves-of-binary-tree/

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
     * @param TreeNode|array|null $root
     * @return Integer[][]
     */
    function findLeaves($root) {
        return $this->find_leaves($root);
    }

    /**
     * @param TreeNode|array|null $root
     * @return Integer[][]
     */
    function find_leaves($root) {
        if (is_array($root)) {
            $root = $this->listToTree($root);
        }

        $layers = [];
        $dfs = function ($node) use (&$dfs, &$layers) {
            if ($node === null) {
                return -1;
            }

            $height = max($dfs($node->left), $dfs($node->right)) + 1;
            if (!array_key_exists($height, $layers)) {
                $layers[$height] = [];
            }
            $layers[$height][] = $node->val;
            return $height;
        };

        $dfs($root);
        return array_values($layers);
    }

    private function listToTree($values) {
        if ($values === null || count($values) === 0) {
            return null;
        }

        $root = new TreeNode($values[0]);
        $queue = [$root];
        $index = 1;
        $count = count($values);
        while ($index < $count) {
            $node = array_shift($queue);
            if ($index < $count && $values[$index] !== null) {
                $node->left = new TreeNode($values[$index]);
                $queue[] = $node->left;
            }
            $index++;
            if ($index < $count && $values[$index] !== null) {
                $node->right = new TreeNode($values[$index]);
                $queue[] = $node->right;
            }
            $index++;
        }
        return $root;
    }
}
