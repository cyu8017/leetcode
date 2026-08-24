<?php
// LeetCode 0427 - Construct Quad Tree
// https://leetcode.com/problems/construct-quad-tree/

class Node {
    public $val = false;
    public $isLeaf = false;
    public $topLeft = null;
    public $topRight = null;
    public $bottomLeft = null;
    public $bottomRight = null;
    function __construct(
        $val = false,
        $isLeaf = false,
        $topLeft = null,
        $topRight = null,
        $bottomLeft = null,
        $bottomRight = null
    ) {
        $this->val = $val;
        $this->isLeaf = $isLeaf;
        $this->topLeft = $topLeft;
        $this->topRight = $topRight;
        $this->bottomLeft = $bottomLeft;
        $this->bottomRight = $bottomRight;
    }
}

class Solution {
    /**
     * @param Integer[][] $grid
     * @return Node
     */
    function construct($grid) {
        return $this->build($grid, 0, 0, count($grid));
    }

    /**
     * @param Integer[][] $grid
     * @param int $row
     * @param int $col
     * @param int $size
     * @return Node
     */
    private function build($grid, $row, $col, $size) {
        if ($size === 1) {
            return new Node($grid[$row][$col] === 1, true);
        }

        $half = intdiv($size, 2);
        $topLeft = $this->build($grid, $row, $col, $half);
        $topRight = $this->build($grid, $row, $col + $half, $half);
        $bottomLeft = $this->build($grid, $row + $half, $col, $half);
        $bottomRight = $this->build($grid, $row + $half, $col + $half, $half);

        if (
            $topLeft->isLeaf && $topRight->isLeaf && $bottomLeft->isLeaf && $bottomRight->isLeaf &&
            $topLeft->val === $topRight->val && $topLeft->val === $bottomLeft->val && $topLeft->val === $bottomRight->val
        ) {
            return new Node($topLeft->val, true);
        }

        return new Node(true, false, $topLeft, $topRight, $bottomLeft, $bottomRight);
    }
}
