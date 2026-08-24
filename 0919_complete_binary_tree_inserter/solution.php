<?php
// LeetCode 0919 - Complete Binary Tree Inserter
// https://leetcode.com/problems/complete-binary-tree-inserter/

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

if (!function_exists('listToTree')) {
    function listToTree($values) {
        if (!$values) return null;
        $root = new TreeNode($values[0]);
        $queue = [$root];
        $i = 1;
        $n = count($values);
        while ($queue && $i < $n) {
            $node = array_shift($queue);
            if ($i < $n) {
                if ($values[$i] !== null) {
                    $node->left = new TreeNode($values[$i]);
                    $queue[] = $node->left;
                }
                $i++;
            }
            if ($i < $n) {
                if ($values[$i] !== null) {
                    $node->right = new TreeNode($values[$i]);
                    $queue[] = $node->right;
                }
                $i++;
            }
        }
        return $root;
    }
}

if (!function_exists('treeToList')) {
    function treeToList($root) {
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
            if ($node->left !== null || $node->right !== null) {
                $queue[] = $node->left;
                $queue[] = $node->right;
            }
        }
        while ($result && $result[count($result) - 1] === null) array_pop($result);
        return $result;
    }
}

class CBTInserter {
    private $root;
    private $parents;

    function __construct($root) {
        if (is_array($root)) $root = listToTree($root);
        $this->root = $root;
        $this->parents = [];
        $q = [$root];
        while ($q) {
            $node = array_shift($q);
            if ($node->left !== null) $q[] = $node->left;
            else {
                $this->parents[] = $node;
                break;
            }
            if ($node->right !== null) $q[] = $node->right;
            else {
                $this->parents[] = $node;
                break;
            }
        }
        while ($q) $this->parents[] = array_shift($q);
    }

    function insert($val) {
        $parent = $this->parents[0];
        $child = new TreeNode($val);
        if ($parent->left === null) $parent->left = $child;
        else {
            $parent->right = $child;
            array_shift($this->parents);
        }
        $this->parents[] = $child;
        return $parent->val;
    }

    function get_root() {
        return treeToList($this->root);
    }

    function getRoot() {
        return $this->root;
    }
}
