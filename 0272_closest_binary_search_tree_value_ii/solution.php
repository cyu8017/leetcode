<?php
// LeetCode 0272 - Closest Binary Search Tree Value II
// https://leetcode.com/problems/closest-binary-search-tree-value-ii/

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
     * @param Float $target
     * @param Integer $k
     * @return Integer[]
     */
    function closestKValues($root, $target, $k) {
        $values = [];
        $this->inorder($root, $values);

        $lo = 0;
        $hi = count($values);
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi, 2);
            if ($values[$mid] < $target) {
                $lo = $mid + 1;
            } else {
                $hi = $mid;
            }
        }

        $left = $lo - 1;
        $right = $lo;
        $result = [];
        while (count($result) < $k) {
            if ($right >= count($values) ||
                ($left >= 0 && abs($values[$left] - $target) <= abs($values[$right] - $target))) {
                $result[] = $values[$left];
                $left--;
            } else {
                $result[] = $values[$right];
                $right++;
            }
        }
        return $result;
    }

    private function inorder($node, &$values) {
        if ($node === null) {
            return;
        }
        $this->inorder($node->left, $values);
        $values[] = $node->val;
        $this->inorder($node->right, $values);
    }
}
