<?php
// LeetCode 0431 - Encode N-ary Tree to Binary Tree
// https://leetcode.com/problems/encode-n-ary-tree-to-binary-tree/

class Node {
    public $val = null;
    /** @var Node[] */
    public $children = [];
    function __construct($val = null, $children = null) {
        $this->val = $val;
        $this->children = $children ?? [];
    }
}

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
     * @param Node|null $root
     * @return TreeNode|null
     */
    function encodeNaryTree($root) {
        return $this->encode_nary_tree($root);
    }

    /**
     * @param TreeNode|null $root
     * @return Node|null
     */
    function decodeBinaryTree($root) {
        return $this->decode_binary_tree($root);
    }

    /**
     * @param Node|null $root
     * @return TreeNode|null
     */
    function encode_nary_tree($root) {
        if ($root === null) {
            return null;
        }

        $binary = new TreeNode($root->val);
        if (count($root->children) === 0) {
            return $binary;
        }

        $binary->left = $this->encode_nary_tree($root->children[0]);
        $sibling = $binary->left;
        for ($index = 1; $index < count($root->children); $index++) {
            $sibling->right = $this->encode_nary_tree($root->children[$index]);
            $sibling = $sibling->right;
        }
        return $binary;
    }

    /**
     * @param TreeNode|null $root
     * @return Node|null
     */
    function decode_binary_tree($root) {
        if ($root === null) {
            return null;
        }

        $node = new Node($root->val, []);
        $current = $root->left;
        while ($current !== null) {
            $node->children[] = $this->decode_binary_tree($current);
            $current = $current->right;
        }
        return $node;
    }
}
