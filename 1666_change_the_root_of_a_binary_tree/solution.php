<?php
// LeetCode 1666 - Change the Root of a Binary Tree
// https://leetcode.com/problems/change-the-root-of-a-binary-tree/

class Solution {
    function flipBinaryTree($root, $leaf) {
        $node = $leaf;
        while ($node !== $root) {
            $parent = $node->parent;
            if ($parent->left === $node) $parent->left = null;
            else $parent->right = null;
            $originalLeft = $node->left;
            $node->left = $parent;
            if ($originalLeft !== null) $node->right = $originalLeft;
            $node = $parent;
        }
        $fixParent = function($cur, $parent) use (&$fixParent) {
            if ($cur === null) return;
            $cur->parent = $parent;
            $fixParent($cur->left, $cur);
            $fixParent($cur->right, $cur);
        };
        $fixParent($leaf, null);
        return $leaf;
    }
}
