<?php
// LeetCode 0558 - Logical OR of Two Binary Grids Represented as Quad-Trees
// https://leetcode.com/problems/logical-or-of-two-binary-grids-represented-as-quad-trees/

class Node {
    public $val = false;
    public $isLeaf = false;
    public $topLeft = null;
    public $topRight = null;
    public $bottomLeft = null;
    public $bottomRight = null;
    function __construct($val = false, $isLeaf = false, $topLeft = null, $topRight = null, $bottomLeft = null, $bottomRight = null) {
        $this->val = $val;
        $this->isLeaf = $isLeaf;
        $this->topLeft = $topLeft;
        $this->topRight = $topRight;
        $this->bottomLeft = $bottomLeft;
        $this->bottomRight = $bottomRight;
    }
}

class Solution {
    function intersect($quadTree1, $quadTree2) {
        if ($quadTree1->isLeaf) return $quadTree1->val ? $quadTree1 : $quadTree2;
        if ($quadTree2->isLeaf) return $quadTree2->val ? $quadTree2 : $quadTree1;
        $topLeft = $this->intersect($quadTree1->topLeft, $quadTree2->topLeft);
        $topRight = $this->intersect($quadTree1->topRight, $quadTree2->topRight);
        $bottomLeft = $this->intersect($quadTree1->bottomLeft, $quadTree2->bottomLeft);
        $bottomRight = $this->intersect($quadTree1->bottomRight, $quadTree2->bottomRight);
        if ($topLeft->isLeaf && $topRight->isLeaf && $bottomLeft->isLeaf && $bottomRight->isLeaf
            && $topLeft->val === $topRight->val && $topRight->val === $bottomLeft->val
            && $bottomLeft->val === $bottomRight->val) {
            return new Node($topLeft->val, true);
        }
        return new Node(false, false, $topLeft, $topRight, $bottomLeft, $bottomRight);
    }
}
