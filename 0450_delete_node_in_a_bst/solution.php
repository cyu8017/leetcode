<?php
// LeetCode 0450 - Delete Node in a BST
// https://leetcode.com/problems/delete-node-in-a-bst/

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
     * @param TreeNode|null $root
     * @param int $key
     * @return TreeNode|null
     */
    function deleteNode($root, $key) {
        if ($root === null) {
            return null;
        }
        if ($key < $root->val) {
            $root->left = $this->deleteNode($root->left, $key);
        } elseif ($key > $root->val) {
            $root->right = $this->deleteNode($root->right, $key);
        } else {
            if ($root->left === null) {
                return $root->right;
            }
            if ($root->right === null) {
                return $root->left;
            }
            $successor = $root->right;
            while ($successor->left !== null) {
                $successor = $successor->left;
            }
            $root->val = $successor->val;
            $root->right = $this->deleteNode($root->right, $successor->val);
        }
        return $root;
    }
}
