<?php
class Node {
    public $val;
    public $left = null;
    public $right = null;
    public $random = null;
    function __construct($val = 0) {
        $this->val = $val;
    }
}

class Solution {
    function copyRandomBinaryTree($root) {
        $copies = new SplObjectStorage();
        $clone = function($node) use (&$clone, $copies) {
            if ($node === null) return null;
            if (!$copies->contains($node)) {
                $copy = new Node($node->val);
                $copies[$node] = $copy;
                $copy->left = $clone($node->left);
                $copy->right = $clone($node->right);
                $copy->random = $clone($node->random);
            }
            return $copies[$node];
        };
        return $clone($root);
    }
}
